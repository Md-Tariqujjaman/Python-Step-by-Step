x = int(input("input your number: "))
y = list(range(2,x))
prime_list = []

for i in y:
    if i==2:
        prime_list.append(i)
    else:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            prime_list.append(i)

print(prime_list)