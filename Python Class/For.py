a = ['hello','abdullah',147,655]
print(a)

for i in a:
	if i == a[0] or i == a[1]:
		print(i)


b = list(range(1,200))
print(b)
total = 0
for i in b:
	if i % 3 == 0 or i % 5 == 0:
		total += i
print(total)


#b = lists(range(1,20))but not including 20