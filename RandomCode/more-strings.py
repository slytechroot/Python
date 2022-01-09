#create a list from scratch
contact = [] #empty list

contact.append("Gary")
contact.append("Mary")

print (contact)

##add several items to a list - EXTEND the list as a collection of items
contact.extend(['Ray', 'Tia', 3, 8, 21])
print(contact)

#insert item at index 2. See results how Molly was added before 'Ray'
contact.insert(2, "Molly")
print(contact)

