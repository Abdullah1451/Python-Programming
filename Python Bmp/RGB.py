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


f = open("red2.bmp","rb")
f2 = open("new2.bmp","wb")

f.seek(0,2)
end = f.tell()
print(end)

padding = 17%4
f.seek(0)
rgb = []

for i in range(0,54):
	byte = f.read(1)
	#intValue = int.from_bytes(bytes, byteorder='big')
	#single_byte = i.to_bytes(1, byteorder='big', signed=True) 
	f2.write(byte)


print(f.tell())
end=578
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
	obj.b = 150
	singleByte = obj.b.to_bytes(1, byteorder='big', signed=False)
	f2.write(singleByte)

	obj.g = 100
	singleByte = obj.g.to_bytes(1, byteorder='big', signed=False)
	f2.write(singleByte)

	obj.r = 50
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
