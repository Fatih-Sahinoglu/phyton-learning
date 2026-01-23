letters=["a\n","b\n","c\n"]

with open("File_Handling/lesson36/write.txt","w",encoding="utf-8") as f:
    f.writable() #True we can write

    f.write("How you doin?\n") #for ending line \n
    f.write("Joey\n")

    f.writelines(letters) #write all list elements one by one

with open("File_Handling/lesson36/write.txt","a",encoding="utf-8") as f:
    f.write("\nAdding text after letters\n")


with open("File_Handling/lesson36/write.txt","r",encoding="utf-8") as f:
    print(f.read())


with open("File_Handling/lesson36/write.txt","w+",encoding="utf-8") as f:
    f.write("Deleted all but now we can read\n")
    f.seek(0) #for read set the last point begin
    print(f.read())

with open("File_Handling/lesson36/write.txt","a+",encoding="utf-8") as f:
    f.write("\nAdded new content and we can read\n")
    f.seek(0) 
    print(f.read())

with open("File_Handling/lesson36/write.txt","r+",encoding="utf-8") as f:
    f.write("Overwriting\n")
    f.seek(0) 
    print(f.read())
    #Because just overwrite not deleting all so text is:
    #Overwriting
    #ut now we can read

    #Added new content and we can read