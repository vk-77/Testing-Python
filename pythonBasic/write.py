#Another way of opening a file.
#with open('textfile1.txt','r') as file : #Here 'r' is flag which means file is in read mode.
#    print(file)

#Read the files and store data in the list.
# Reverse the list
# Write back the list in the file.
with open('textfile1.txt','r') as reader:
    content = reader.readlines()
    reversed(content)

    with open('textfile1.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)