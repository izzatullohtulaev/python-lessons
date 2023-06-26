x = int(input("Number: "))
if x<0:
    print(False)
else:
    temp = str(x)
    temp = temp[::-1]
    if str(x) == temp:
        print(True)
    else:
        print(False)