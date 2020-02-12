a=int(input("enter a number:"))
b=1
c=0
while b<=a:
    if a%b==0:
        c=c+1
    b=b+1
if c<=2:
    print("the number is prime")
else:
    print("the number is composite")
