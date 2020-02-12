number=int(input("enter a number:"))
string=str(number)
rev_string=string[::-1]
print("reversed:",rev_string)
if string==rev_string:
    print("number is pallindrome")
else:
    print("number is not pallindrome")
