chara=input("Enter a character: ")
vowels = "AEIOUaeiou"
if len(chara) != 1:
    print("Error: Please enter a single character.")
else:
    if chara.isalpha():
        if chara.isupper():
            if chara in vowels:
                print(chara," is an uppercase vowel.")
            else:
                print(chara," is an uppercase consonant.")
        else:
            if chara in vowels:
                print(chara," is a lowercase vowel.")
            else:
                print(chara," is a lowercase consonant.")
        
    elif chara.isdigit():
        if int(chara) % 2==0:
            print(chara," is an even digit.")
        else:
            print(chara," is an odd digit.")
    else:
        print(chara," is a special character.")

