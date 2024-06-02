import time

stime = time.time()
 
f = open('newfile.bin', 'rb')
binary_code = f.read()
code = ''.join(format(byte, '08b') for byte in binary_code)
f.close()

f = open("dict.txt", "r")
coder = f.read()
f.close()

codeList = {}
coder = coder[1:-1]

pairs = coder.split(", ")

for pair in pairs:
		value, key = pair.split(": ")
		value = value[1:-1]
		key = key[1:-1]
		codeList[key] = value
		
		
text = ""
symbol = ""		
for i in code:
	symbol += i
	if codeList.get(symbol) != None:
		if "\\" in  codeList.get(symbol):
			text += codeList.get(symbol).encode().decode("unicode_escape")
			symbol = ""
		else:
			text += codeList.get(symbol)
			symbol = ""
		
f = open("finish.txt", "w")
f.write(text)
f.close()

etime = time.time()

print(etime - stime)