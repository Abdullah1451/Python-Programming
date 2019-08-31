'''class BitmapHeader:
	 
	bfType
	int bfSize;	
	short bfReserved1;
	short bfReserved2;
	int bfOdisBits;


class BitmapInfoHeader:
	int biSize;
	int  biWidth;
	int biHeight;
	short biPlanes;
	short biBitCount;
	int biCompression;
	int biSizeImage;
	int biXPelsPerMeter;
	int biYPelsPerMeter;
	int biClrUsed;
	int biClrImportant;
'''

class RGB:
	def __init__(self, b, g, r):
		self.b = b 
		self.g = g
		self.r = r


f = open("clue.bmp","rb")
f2 = open("verdict1.bmp","wb")

f.seek(0,2)
end = f.tell()
print(end)

padding = 640%4
print("padding"+str(padding))
f.seek(0)
rgb = []

for i in range(0,54):
	byte = f.read(1)
	#intValue = int.from_bytes(bytes, byteorder='big')
	#single_byte = i.to_bytes(1, byteorder='big', signed=True) 
	f2.write(byte)


print(f.tell())
end=307200
for i in range(0,end):
	bytes = f.read(1)
	intValue = int.from_bytes(bytes, byteorder='big')

	bytes = f.read(1)
	intValue1 = int.from_bytes(bytes, byteorder='big')

	bytes = f.read(1)
	intValue2 = int.from_bytes(bytes, byteorder='big')

	rgb.append(RGB(intValue, intValue1, intValue2))
	if i % 17 == 0:
		x=0
		temp=0
		while x<padding:
			temp = f.read(1)
			x+=1
	
i=0
for obj in rgb:
	if obj.b == 0 and obj.g == 0:
		#print("yo")
		obj.b = 255
		singleByte = obj.b.to_bytes(1, byteorder='big', signed=False)
		f2.write(singleByte)

		obj.g = 255
		singleByte = obj.g.to_bytes(1, byteorder='big', signed=False)
		f2.write(singleByte)	

		obj.r = 255
		singleByte = obj.r.to_bytes(1, byteorder='big', signed=False)
		f2.write(singleByte)

	else:
		#print("no")
		avg = obj.b + obj.g + obj.r
		avg = int(avg/3)
		#print(avg)
		if avg <=234:
			avg -= 40
			obj.b = avg
			singleByte = obj.b.to_bytes(1, byteorder='big', signed=False)
			f2.write(singleByte)
		
			obj.g = avg
			singleByte = obj.g.to_bytes(1, byteorder='big', signed=False)
			f2.write(singleByte)
		
			obj.r = avg
			singleByte = obj.r.to_bytes(1, byteorder='big', signed=False)
			f2.write(singleByte)

		else:
			obj.b = avg
			singleByte = obj.b.to_bytes(1, byteorder='big', signed=False)
			f2.write(singleByte)
		
			obj.g = avg
			singleByte = obj.g.to_bytes(1, byteorder='big', signed=False)
			f2.write(singleByte)
		
			obj.r = avg
			singleByte = obj.r.to_bytes(1, byteorder='big', signed=False)
			f2.write(singleByte)


	i+=1

	if i % 17 == 0:
		x=0
		temp=0
		while x<padding:
			singleByte = temp.to_bytes(1, byteorder='big', signed=False)
			f2.write(singleByte)
			x+=1
