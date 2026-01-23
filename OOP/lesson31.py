#Static Methods

class Math:

    @staticmethod #This is static method so it here just for categorizing
    def add(x,y):
        return x+y
    
    @staticmethod
    def sub(x,y):
        return x-y
    
    @staticmethod
    def multiply(x,y):
        return x*y
    
    @staticmethod
    def div(x,y):
        return x/y

#Because they are static method we dont have to create a object just class.method is enough
print(Math.add(12,3))
print(Math.sub(12,3))
print(Math.multiply(12,3))
print(Math.div(12,3))