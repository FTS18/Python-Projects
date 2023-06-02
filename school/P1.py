#Read a text file line by line and display each word separated by a #
file = open('file.txt').read()
y=file.replace(" ","#")
print(y)