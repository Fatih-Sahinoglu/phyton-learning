#List ----------------------------------------

fruit=["apple","banana","cherry","orange","apple"]
#list is ordered, changeable, and allows duplicate values
#list can have items of different data types
mylist=[20,"Fatih",True,3.14]
#----------------------------------------

print(fruit)  # Output the entire list one by one
print(fruit[0])  # Output the first item

print(fruit.index("cherry"))  # Output the index of the item with value "cherry"
print(fruit.count("apple"))  # Output the number of times "apple" appears in the list
print(len(fruit))  # Output the length of the list

print(fruit[2:4])  # Output items from index 2 to 3
#Careful about these indexes, the last index is not included

fruit[4]="kiwi"  # Change the value at index 4
fruit[0:2]=["grape","mango"]  # Change values from index 0 to 1
#----------------------------------------

#add items to a list------------------------------------------------
new_fruit=fruit+["pear","peach"] # Combine two lists

fruit.append("watermelon")  # Add an item to the end of the list
fruit.insert(1,"strawberry")  # Insert an item at a specific index
fruit.extend(["kiwi","pineapple"])  # Add multiple items to the end of the list
#----------------------------------------

#copy a list----------------------------------------
fruit_copy=fruit.copy()
fruit_copy2=list(fruit)
fruit_copy3=fruit[:]
#----------------------------------------

#remove items from a list----------------------------------------
fruit.remove("banana")  # Remove a specific item BUT only the first one
fruit.pop()  # Remove the last item

del fruit[0]  # Delete the item at index 0
del fruit # Delete the entire list completely gone

fruit.clear()  # Clear all items from the list, but the list still exists
#----------------------------------------

#nested lists----------------------------------------
import copy # Import the copy module for deep copying

list1 = [[1, 2], [3, 4, 5]] # A list containing nested lists
list2 = copy.deepcopy(list1) # Create a deep copy of list1

list2[0][0] = 99 # Modify an element in the copied list
list2[0][1]=100

print("Original List:", list1) # Output the original list
print("Modified Copy:", list2) # Output the modified copy
#----------------------------------------

#Sorting a list----------------------------------------
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # Sort the list
numbers.sort(reverse=True)  # Sort the list in reverse order
numbers.reverse()  # Reverse the order of the list

words = ["banana", "apple", "Cherry"]
words.sort()  # Sort the list alphabetically BUT uppercase letters come first
words.sort(key=str.lower)  # Sort the list alphabetically ignoring case