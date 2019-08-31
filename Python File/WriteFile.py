f = open("MyInfo.txt","w") #if file doesn't exists it will create otherwise it will write
while True:
	line = input("Enter : ")
	if(line == "-1"):
		break
	else:
		f.write(line)
		f.write("\n")

f.close()