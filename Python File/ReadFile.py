f = open("FamilyInfo.txt","r")
while True:
	line = f.readline()
	if line == "":
		print("\n File End Using While Loop\n\n")
		break
	else:
		print(line)
f.seek(0,0)

# Another Way Of Reading File Is Using For Loop

for line in f:
	print(line)
print("\n File End Using For Loop\n\n")
f.close()


# Another Way Of Reading File Without Loop

with open("FamilyInfo.txt",'r') as f:  
    line = f.read();  
    print(line) 