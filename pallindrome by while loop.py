x=int(input("enter a number"))
a=x
dig=0
rev=0
while (x>0):
        dig=x%10
        rev=rev*10+dig
        x=x//10
print("the reverse no. is ", rev)
if rev==a:
    print("is pallindrome")
else:
    print("no pallindrome")