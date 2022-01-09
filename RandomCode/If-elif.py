x = input("x: ")
if int(x) > 4:
    print("x is greater than 4.")
else:
    print("x is smaller than 4. ")
    

#or, this also works:
    x = input("x: ")
if int(x) > 4:
    print("x is greater than 4.")
elif int(x) == 4:
    print("x is equal than 4. ")
elif int(x) < 4:
    print("x is smaller than 4. ")