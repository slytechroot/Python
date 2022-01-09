"""Functions:
- if we have a chunk of code that we need to re-use several times, it makes sense to collect our code together
as a 'function'
 
 - we can use 'def' to create a function
"""
str1 = {'test', 'me', 'you', 'home', 'sky', 'eggs'}

hi = str1[0:5]
print (hi)

print(hi.upper()) #convert all to upper case. Function .lower() will do the opposite

str1a = str1[:] #copy a string
print (str1a)

print (str1a.split()) #split according to white space

print (str1a.replace('cat','black cat')) #replace cat of str1a with black cat