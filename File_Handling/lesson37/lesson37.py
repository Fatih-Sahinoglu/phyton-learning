# 2.C#
# 4.Ruby

with open("File_Handling/lesson37/write.txt","r+",encoding="utf-8") as f:

    #Adding text at first line---------------------------------
    my_text=f.read() # read all and get in string
    my_text="1.C++\n"+my_text #add first line
    f.seek(0) #start from begin
    f.write(my_text) #overwrite all new text
    # 1.C++
    # 2.C#
    # 4.Ruby
    #we can add last or a+ also work---------------------------
    f.seek(0)
    #Add text midddle of file--------------------------------
    file_list=f.readlines()
    file_list.insert(2,"3.Python\n")
    f.seek(0)
    f.writelines(file_list)
    # 1.C++
    # 2.C#
    # 3.Python
    # 4.Ruby
    # -------------------------------------------------
    f.seek(0)
    print(f.read())

