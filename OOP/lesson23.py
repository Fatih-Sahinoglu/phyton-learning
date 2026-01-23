#OOP

class friend: #creating class
    name="Fatih" #property

    def __init__(self): #constructor method
        self.surname=input(f"What is your surname {self.name} ?\n")
        #self.x = x is property of this class and we creating this in constructor

    def ques(self): #method // self for accessesing class's properties
        print(f"Then, hello {self.name} {self.surname}")

obj=friend() #creating an object and calling constructor if it exist

obj.ques() #using method (obj.name also work for properties)

obj.name="hitaf" #changed
del obj.name #deleted properties compeletly
del obj #deleted object compeletly

#Some magic / dunder methods
class Person:
    def __init__(self,n,a): #when creating object you will write some values
        self.name=n #and it will create properties for this class
        self.age=a

    def __str__(self): #This one also start when obj created
        return f"Name: {self.name}\nAge: {self.age}"
    
obj1=Person("Fatih",20) 
#Normally returns this properties is not readable BUT thanks to __str__ this transform readable version
print(obj1) #for see return














