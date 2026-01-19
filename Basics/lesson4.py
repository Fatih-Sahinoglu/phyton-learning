# Escape characters
print("He said, \"Hello!\"")
#Using \ allows to use special characters
print("Line1\nLine2")  # New line
print("Column1\tColumn2")  # Tab space

text="Hi, it's a lesson about strings."

print(text[0])  # First character
print(text[-1]) # Last character
print(len(text)) # Length of the string

print(text[5:15])  # Substring from index 5 to 14
print(text[:10])   # First 10 characters
print(text[10:])  # From index 10 to the end

text2="Let's learn Python."
print(text + text2)  # Concatenation of two strings BUT no space
print(text + " " + text2)  # Concatenation with space OR
print(text,text2) # Using comma adds space automatically but it's not string concatenation

#in- not in
print('lesson' in text)  # Check if 'lesson' is in the text (TRUE)
print('python' not in text)  #Check if 'python' is not in the text (TRUE)

print(text.upper())  # Convert to uppercase
print(text.lower())  # Convert to lowercase
print(text.replace("strings", "texts"))  # Replace substring
print(text.split(" "))  # Split string into a list by spaces

# Formatting strings
name = "Fatih"
age = 20
print(f"My name is {name} and I am {age} years old.")  # Using f-strings

pi=3.14159
print(f"Value of pi: {pi:.2f}")  # Formatting float to 2 decimal places
#3,14
