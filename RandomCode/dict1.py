dict = {'Japan':'Tokyo','China':'Beijing', 'South Korea':'Seoul', 'North Korea':'Pyongyang', 'a':3}

#print (dict)

#print (len(dict))  #how many key value pairs

#print ("\nDict2")
dict2 = dict.copy()  #make a copy of the dictionary
#print(dict2)

#del dict2['a'] #del - removes both the key and value. 
#print(dict2)

#print(dict.keys())
#print(dict.values())

#add new key - value pair
#dict[key] = value

#assign string "Hong Kong" to dict2 index of "HK Sar"
dict2["HK Sar"]="Hong Kong"
#assign key of 10 and value of 'bullseye'
dict2[10] = "bullseye"
print (dict2)

#validate if a given key - 'x' is in my dictionary. We will use 'in'
#!!!! this does not WORK as expected!
print ('x' not in dict)

#print value of key "China"
print(dict2["China"])

#sort alphabetically the dict dictionary
print(sorted(dict))





