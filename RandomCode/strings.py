#strings in python
str1 = "Hello, I have a cat."
print(str1)
print(type(str1))

str2 = 8
print(type(str2))

str3 = "She has a hot-hair."

#concatenate
print(str1 + str3)

#space between strings
print(str1 + " " + str3)

c = " ".join([str1, str3])
print(c)

#string operations
print(len(str1)) #how long is my string?

#print first letter of str1
print(str1[0])
print(str1[-20])

#isolate Hello
str1 = "Hello, I have a cat."
print(str1[:5]) #start index to end-1

#Let's print out I have a cat
print(str1[7:20])
#or
print(str1[7:])

#copy a string
str1a = str1[:]
print(str1a)

hi = str1[0:5]
print(hi)

#Usage of function .lower() will do the opposite
print(hi.upper()) #convert all to upper cases.

str1a = str1[:] #copy a string

print(str1a)
print(str1a.split()) #split according to white space

print(str1.replace('cat','black cat'))
#replace cat of str1a with black cat














