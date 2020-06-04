
x = int(input("value: "))
y = list(range(2,x))
for i in y:
    if x%i==0:
    	print(x, "is not a prime number")
    	break
else:
    print(x, "is a prime number")