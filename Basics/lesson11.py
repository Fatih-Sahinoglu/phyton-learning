#List Comprehension
list1 = [1, 2, 3, 4, 5]

[print(i,end=" ") for i in list1] #write all elements of list1

list2=[item for item in list1 if item%2==0] #create a new list with even numbers from list1

list3=[item for item in list1 if item !=3] #create a new list without number 3

numbers=[i for i in range(1,11) if i<8] #create a list with numbers from 1 to 7