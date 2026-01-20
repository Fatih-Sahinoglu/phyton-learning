#decorator just name it can be anything like x

def decorator(func): #decorator function for using func
    def wrapper(*args,**kwargs): #maybe if have some value I dont know
        print(f"{func.__name__} is called") #func.__name__ get function's real name
        result=func(*args,**kwargs) #start func evn if it have some parameters
        print("END")
        return result 
    return wrapper #careful NOT wrapper() just wrapper

@decorator #after first func will go decorator function
def hello():
    print("Hello, World!")

hello()

print()

@decorator
def sum(x,y): #this have parameters but thanks to wrapper it also work
    print(x+y) 

sum(13,23)