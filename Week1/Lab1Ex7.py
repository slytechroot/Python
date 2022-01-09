#To Do: Create a program that calculates the cost of these three rooms.
#1.	Create variables for length and width of each room.
#2.	Create variable for area of each room, calculate the area.
#3.	Create a variable for total areas of 3 rooms; calculate the total areas of 3 rooms
#4.	Use * operator to determine the cost of flooring; cost per square foot * total areas
#5.	Use print() to show the cost of flooring.

#room_area = length * width

living_Length = int(input ('What is the length of the 1st room: '))
living_Width = int(input ('What is the width of the 1st room: '))
living_area = living_Length * living_Width
print (living_area)

master_Length = int(input ('What is the length of the 2nd room: '))
master_Width = int(input ('What is the width of the 2nd room: '))
master_area = master_Length * master_Width
print (master_area)

kitchen_Length = int(input ('What is the length of the 3rd room: '))
kitchen_Width = int(input ('What is the width of the 3rd room: '))
kitchen_area = kitchen_Length * kitchen_Width
print (kitchen_area)

total_area = living_area + master_area + kitchen_area
print ('\nThe total area of all 3 rooms is: ',total_area)

flooring_cost = float(living_area * total_area)
print ('\nThe total flooring cost for all 3 rooms is: ',flooring_cost)
