f = open("red.bmp","rb")
f2 = open("new.bmp","wb")
f.seek(0,2)
end = f.tell()
end+=1
f.seek(0)
for i in range(0,55):
	byte = f.read(1)
	#intValue = int.from_bytes(bytes, byteorder='big')
	#single_byte = i.to_bytes(1, byteorder='big', signed=True) 
	f2.write(byte)

#f.seek(55)
for i in range(55,end):
	bytes = f.read(1)
	intValue = int.from_bytes(bytes, byteorder='big')
	if intValue!=0:
		intValue = 190
		singleByte = intValue.to_bytes(1, byteorder='big', signed=False)
		f2.write(singleByte)
	else:
		singleByte = intValue.to_bytes(1, byteorder='big', signed=False)
		f2.write(singleByte)




'''f.seek(5)
bytes = f.read(1)
i = int.from_bytes(bytes, byteorder='big')
print(i)'''