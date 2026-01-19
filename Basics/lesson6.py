#if elif else

name=input("Enter your name: ")
name=name.strip().title() #we can chain methods like this
#strip to remove spaces and title to capitalize first letter of each word

number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))

if number1>number2:
    print(f"{name}'s first number ({number1}) is greater than second number ({number2})")
elif number1<number2:
    print(f"{name}'s second number ({number2}) is greater than first number ({number1})")
else:
    print(f"{name}'s both numbers are equal: {number1} = {number2}")