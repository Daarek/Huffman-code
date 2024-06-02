import time

stime=time.time()

def build (text):
	
	textArray = list(text)
	symbolList = []
	weightList = []
	
	for symbol in textArray:
		    if symbol in symbolList:
		    	weightList[symbolList.index(symbol)] += 1
		    else:
		    	symbolList.append(symbol)
		    	weightList.append(1)
		    	
	class Node:
		def __init__ (self, parentNode, leftNode, rightNode, name, weight):
			self.parentNode = parentNode
			self.leftNode = leftNode
			self.rightNode = rightNode
			self.name = ""
			self.weight = 0
			
	nodeList = list(symbolList)
	nodeWeight = list(weightList)
			
	while(len(nodeList) != 1 ):
		
		rightChild = nodeList[nodeWeight.index(min(nodeWeight))]
		rightWeight = min(nodeWeight)
		nodeWeight.remove(min(nodeWeight))
		nodeList.remove(rightChild)
		leftChild = nodeList[nodeWeight.index(min(nodeWeight))]
		leftWeight = min(nodeWeight)
		nodeWeight.remove(min(nodeWeight))
		nodeList.remove(leftChild)
		
		nodeList.append(Node(None, leftChild, 	rightChild, None, leftWeight + rightWeight))
		nodeWeight.append(leftWeight + rightWeight)
		
		
		if type(leftChild) == str:
			nodeList[-1].name = nodeList[-1].name + leftChild
		else:
			nodeList[-1].name = nodeList[-1].name + leftChild.name
			leftChild.parentNode = nodeList[-1]
			
		if type(rightChild) == str:
			nodeList[-1].name = nodeList[-1].name + rightChild
		else:
			nodeList[-1].name = nodeList[-1].name + rightChild.name
			rightChild.parentNode = nodeList[-1]
		
			
	codeList = []
	root = nodeList[-1]
	for i in range (len(symbolList)):
		def buildNumber (symb, topNode):
			if (type(topNode.leftNode) == str and topNode.leftNode == symb):
				return "0"
			if (type(topNode.rightNode) == str and topNode.rightNode == symb):
				return "1"	
			if type(topNode.leftNode) != str:
				if symb in topNode.leftNode.name:
					return "0" + buildNumber (symb, topNode.leftNode)
			if type(topNode.rightNode) != str:
				if symb in topNode.rightNode.name:
					return "1" + buildNumber (symb, topNode.rightNode)
		codeList.append(buildNumber(symbolList[i], root))
	return(codeList)

f =  open("/storage/emulated/0/codes/Huffman/file.txt", "r")
txt = f.read()
f.close()
textArray = list(txt)
symbolList = []

for symbol in textArray:
	if symbol in symbolList:
		pass
	else:
		symbolList.append(symbol)
		
codeList = build(txt)

codeDict = dict(zip(symbolList, codeList))

compressedTxt = ""

for i in range (len(txt)):
	compressedTxt += codeDict.get(txt[i])


result = bytearray()

for i in range(0, len(compressedTxt), 8):
    byte = compressedTxt[i:i+8]
    byte_value = int(byte, 2) 
    result.append(byte_value)


file = open("newfile.bin", "wb")
file.write(result)
file.close()
txt = ""
for i in codeDict:
	txt += i
	txt += codeDict.get(i)
file = open("dict.txt", "w")
file.write(str(codeDict))
file.close()

etime = time.time()
print(" " + str(etime-stime))