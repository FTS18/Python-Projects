#Remove all the lines that contain the character 'a' in a file and write it to another file.
file = open('file.txt').read()
newString=file.replace("a", "")
newString=file.replace("A", "")
newFile = open('newFile.txt', "w").write(newString)