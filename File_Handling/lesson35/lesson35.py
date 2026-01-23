#if we dont write anything it is for read (r)
#automaticly close
#with open() as name:
with open("File_Handling/lesson35/oto.txt",encoding="utf-8") as f:
    print(f.read(10))
    print(f.tell()) #where is the last point

    f.readable() #True if this file readable
    f.seekable() #True if seek() method can use

    f.truncate(50) #delete all text after 50 byte
    f.seek(5)
    f.truncate() #delete all after last point (5)