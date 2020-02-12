#Draw a pattern of asteric(*) in half pyramid
rows=6
for i in range(rows,0,-1):
    for j in range(0,i-1):
        print("*",end="")
    print("\r")
