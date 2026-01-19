#some basic operations in Python
a=3
b=2
print(a**b) #Exponentiation
print(a//b) #Floor division


#comparing values
a==b #equal to
a!=b #not equal to


#logical operators
note=49

if note>=90 and note<=100: 
    print("A")
elif note>=80 and note<90:
    print("B")
elif not(note>=80 and note<90):
    print("C")
elif note<100 or note>0:
    print("Invalid note")
