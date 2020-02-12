#write a program to take a user input of five numbers in a list and find a prime
prime=[]
for i in range(1,30):
    for j in range(2,i):
        if i % j==0:
            break
    else:
        prime.append(i)
print(prime)