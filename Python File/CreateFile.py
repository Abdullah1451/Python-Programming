f = open("MyInfo.txt","x") #'x' create a file if the file doesnot exists and if exists it will give error
print("position of file pointer : ",f.tell())
f.close();
