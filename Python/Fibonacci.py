n=20
f=1
p=0
print(p, end="")
for i in range(1,n+1):
	print(" ,"+str(f), end="")
	f=f+p
	p=f-p