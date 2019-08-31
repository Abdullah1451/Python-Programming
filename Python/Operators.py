a=20
b=10
x=True
y=False

print("Expected = 30  ",(a+b))

print("Expected = 10  ",(a-b))

print("Expected = 200  ",(a*b))

print("Expected = 2  ",(a/b))

print("Expected = 0  ",(a%b))

print("Expected = 160000  ",(a**4))

print("Expected = 7  ",(a//3))

a+=b
print("Expected = 30  ",(a))

a-=b
print("Expected = 20  ",(a))

a*=b
print("Expected = 200  ",(a))

a/=b
print("Expected = 20  ",(a))

a%=b
print("Expected = 0  ",(a))

a=20
a//=3
print("a=20,,,,Expected = 7  ",(a))

a=20
a**=2
print("a=20,,,,Expected = 400  ",(a))

y&=x
print("Expected = false  ",(bool(y)))

x|=y
print("Expected = true  ",(bool(x)))

x^=y
print("Expected = true  ",(bool(x)))

b<<=2
print("Expected = 40  ",(b))

b>>=2
print("Expected = 10  ",(b))

print("Expected = false  ",(a==b))

print("Expected = true  ",(a!=b))

print("Expected = false  ",(a<b))

print("Expected = true  ",(a>b))

print("Expected = false  ",(a<=b))

print("Expected = true ",(a>=b))

x=True
y=False
print("Expected = false  ",(bool(y and x)))

print("Expected = true  ",(bool(x or y)))

print("Expected = true  ",(not(a==b)))