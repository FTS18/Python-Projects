#Write a function, vowelCount() in Python that counts and displays the number of vowels in the text file named Poem.txt
file = (open('poem.txt').read()).lower()
def vowelCount():
    v=s=c=0
    vowels=['a','e','i','o','u']
    x=file.split(' ')
    for i in file:
        if i in vowels:
            v+=1
        if i.isspace()==True:
            s+=1
        c+=1
    print("Vowels: ", v)
    print("Words: ", len(x))
    print("Characters: ", c-s)
vowelCount()