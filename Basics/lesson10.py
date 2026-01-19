#for loop
#break and continue statements same

#list usage in for loop-----------------------
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item,end=" ")
else:
    print("Loop is over") #also as same as while loop


#range() function usage in for loop-----------------
for x in range(0,5,2): #range(start,stop,step) default start=0 step=1
    print(x,end=" ") #0 2 4


#pass-------------------------------------
for x in range(5):
    if x==3:
        pass #it will do nothing also ... is same as pass
    print(x,end=" ") #0 1 2 3 4


#nested for loop---------------------------
num=[0,1]
place=["first","second"]
for outer in num:
    for inner in place:
        print(outer,inner)

#nested list and nested for loop----------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element,end=" ")
    print()