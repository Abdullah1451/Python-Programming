with open("red.bmp", "rb") as f:
	for i in f:
		bn = bin(i)
		print(int(bn, 2))	







'''fo = open("foo.txt", "r")
print ("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fo.readline()
print ("Read Line: %s" % (line))

# Again set the pointer to the beginning
fo.seek(4, 0)
line = fo.readline()
print ("Read Line: %s" % (line))

# Close opend file
fo.close()
'''




'''import io
binary_stream = io.BytesIO()
# Binary data and strings are different types, so a str
# must be encoded to binary using ascii, utf-8, or other.
binary_stream.write("Hello, world!\n".encode('ascii'))
binary_stream.write("Hello, world!\n".encode('utf-8'))

# Move cursor back to the beginning of the buffer
binary_stream.seek(0)

# Read all data from the buffer
stream_data = binary_stream.read()

# The stream_data is type 'bytes', immutable
print(type(stream_data))////////////////////////
print(stream_data)//////////////////////////

# To modify the actual contents of the existing buffer
# use getbuffer() to get an object you can modify.
# Modifying this object updates the underlying BytesIO buffer
mutable_buffer = binary_stream.getbuffer()
print(type(mutable_buffer))  # class 'memoryview'///////////////////////
mutable_buffer[0] = 0xFF

# Re-read the original stream. Contents will be modified
# because we modified the mutable buffer
binary_stream.seek(0)
print(binary_stream.read())/////////////////////////////


<class 'bytes'>
b'Hello, world!\nHello, world!\n'
<class 'memoryview'>
b'\xffello, world!\nHello, world!\n'
'''