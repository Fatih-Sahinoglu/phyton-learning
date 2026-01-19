#Dictinoraies in Python

car={"brand":"BMW",
     "model":"X5",
     "year":2020 
    }
#Dictionaries are unordered, changeable and indexed collection of items
#Dictionaries do not allow duplicate keys
#after last key:value no comma is needed but allowed
#Keys must be strings, numbers or tuples (immutable types)
#Values can be of any data type


#Accessing elements in a dictionary---------------------------------------
print(car) #Print the entire dictionary

print(car.keys()) #Print all keys in the dictionary
print(car.values()) #Print all values in the dictionary

print(car["brand"]) #Print value of the key "brand" (BMW)
print(car.get("model")) #Another way to get value of the key "model"

car["color"]="Black" #Add new key:value pair or change

car.items() #Print all key:value pairs in the dictionary in a list of tuples
#[('brand', 'BMW'), ('model', 'X5'), ('year', 2020), ('color', 'Black')]

del car["year"] #Remove key:value pair with key "year"
del car #Deleting the dictionary completely

car.clear() #Clears the dictionary but keeps the dictionary itself
#----------------------------------------------------------------------


#Dictionary operations-----------------------------------------------------
print(len(car)) #Length of the dictionary (number of key:value pairs)

"brand" in car #Check if "brand" KEY exists in the dictionary

car.update({"year":2021}) #Update or create value of key "year"

car.pop("model") #Remove key:value pair with key "model"
car.popitem() #Removes the last inserted key:value pair

car2=car.copy() #Create a copy of the dictionary

keys=["apple","banana","cherry"]
values=0
fruit_dict=dict.fromkeys(keys,values) #Create a dictionary from two lists

car.setdefault("model","X3") #If "model" key does not exist, create it with value "X3"
#if it exists, get the value of "model" key
#----------------------------------------------------------------------