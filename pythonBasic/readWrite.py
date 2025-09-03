file = open("textfile1.txt")
#Read all the context of the read file
#print(file.read(6))

#Read one single line using readline methon
#print(file.readline())
#print(file.readline())

#file.close() #good practice to close a file when it is opened.

#Print all the content using readline

#line = file.readline()
#while line != "" :
#    print(line)
#    line = file.readline()

#Same funtion can be performed with the readlines as well. Here it will be stored in list.
for line in file.readlines():
    print(line)

file.close()