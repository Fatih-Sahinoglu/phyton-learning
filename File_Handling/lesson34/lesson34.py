f=open("File_Handling/lesson34/demo.txt","r",encoding="utf-8")
 #open (first) file with (second) mod (third) for Turkish words

print(f.read(5)) #Read 5 characters 
print(f.read()) #Read all text after start point (for now after Hello)

f.seek(0) #Change start point to file begin (or anywhere)

print(f.readline()) #Read all line after start point
#There is \n end of all line and print makes \n after printing so
#print(f.readline(),end="") makes just one \n

line=f.readlines() #All lines turn a list
print(line[0]) #so we can get like this


f.closed #False because still file is open
f.close()#closing file
f.closed #True because file is closed