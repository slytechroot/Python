def f1():
    print (5)
    
def f2():
    print (7)
    
x = f1()
y = f2()

print (x)
# will equal 'None' because f1() does not return a value

print (y)
# will equal 'None' because f2() does not return a value

print (f2())
#why we do get a 'None' here

