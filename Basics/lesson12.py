#Tuple

# A tuple is is ordered can have same elements multiple times and unchangeable.
cities = ("New York", "Los Angeles", "Chicago", "Houston", "Phoenix","New York")

complex_tuple = ("Hello", 42, 3.14, True, None)
#Tuple can contain different data types

#Accessing elements in a tuple---------------------------------------
print(cities) #Print the entire tuple
print(cities[0]) #Print the first element of the tuple
print(cities[1:4]) #Print elements from index 1 to 3
#----------------------------------------------------------------------


#Tuple operations-----------------------------------------------------
print(len(cities)) #Length of the tuple
cities=cities + ("Philadelphia",) #Adding an element to the tuple (creates a new tuple)
cities=cities*2 #Repeating the tuple

del complex_tuple #Deleting the tuple completely
cities.count("New York") #Count how many "New York" in the tuple
cities.index("Chicago") #Find index of "Chicago" in the tuple
#----------------------------------------------------------------------


#Modifying a tuple (indirectly)---------------------------------------
temp = list(cities) #Convert tuple to list
temp[0] = "San Francisco" #Modify the list
cities = tuple(temp) #Convert list back to tuple
#----------------------------------------------------------------------

numbers = (1, 2, 3, 4, 5)
(x, y, z, *a) = numbers #Unpacking the tuple into variables
#because of the * operator, a will be a list containing all remaining elements
print(x, y, z, a)