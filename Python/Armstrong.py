n=54744
t=n
l=len(str(n))
a=[]
for i in range(0,l):
	temp=t%10
	temp=temp**l
	a.append(temp)
	t=t//10

sum=0

for i in range(0,l):
	sum+=a[i]


if n==sum:
	print("Yes, you entered "+str(n)+" and the sum is "+str(sum))
else:
	print("No, you entered "+str(n)+" and the sum is "+str(sum))
