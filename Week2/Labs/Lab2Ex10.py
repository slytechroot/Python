"""
1.Given the string: “PythonPython”. Write a Python program
that split the string into 2 equal sub-strings, then display the substrings.
"""

strng1 = "PythonPython"
print(strng1)

s_first = strng1[0:len(strng1)//2]

s_second = strng1[len(strng1)//2 if len(strng1)%2 == 0
                  else((len(strng1)//2)+1):]

print(s_first)
print(s_second)















