#Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file
file = open('file.txt').read()
def chk(n):
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    v=c=a=u=l=s=0
    for i in n:
        if i in vowels:
            v+=1
        if i.isspace()==True:
            s+=1
        if i.isalpha()==True:
            a+=1
        if i.islower()==True:
            l+=1
        if i.isupper()==True:
            u+=1
    c=a-v
    print("Length    :", len(n))
    print("Vowels    :", v)
    print("Consonants:", c)
    print("Spaces    :", s)
    print("Lowercase :", l)
    print("Uppercase :", u)
chk(file)