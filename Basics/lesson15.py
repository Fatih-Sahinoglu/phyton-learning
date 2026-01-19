cars={
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020,
    "color": "Blue"   
}
#One of key or value-------------------------------------
for item in cars: #only keys
    print(item)

for item in cars: #only values
    print(cars[item])

#also cars.values() and cars.keys() can be used
#------------------------------------------------------

#Both keys and values-----------------------------------
for key,value in cars.items():
    print(f"{key} - {value}")
#------------------------------------------------------

#Nested dictionaries-------------------------------------
friends={
    "friend1":{ 
        "name":"Fatih",
        "age":21
    },
    "friend2":{
        "name":"Selen",
        "age":20
    }
}
cars={
    "humans":friends #adding nested dictionary as a value even though not meaningful
}
print(friends["friend1"]["name"]) #Accessing nested dictionary value

for outer_key,outer_value in friends.items():
    print(outer_key) #friend1, friend2
    for inner_key in outer_value:
        print(inner_key," : ",outer_value[inner_key]) #name : Fatih, age : 21 etc.