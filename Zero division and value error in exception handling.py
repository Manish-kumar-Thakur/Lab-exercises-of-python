try:
    x=int(input("enter a first num: "))
    y=int(input("enter a second num: "))
    print("The result is: ",x/y)
except ZeroDivisionError:
    print("Plz do not provide zero for y")
except ValueError:
    print("Plz provide numeric value")
