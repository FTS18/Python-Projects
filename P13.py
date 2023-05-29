#Write a function, lenWords(STRING), that takes a string as an argument and returns a tuple containing length of each word of a string. For example, if the string is "Come let us have some fun", the tuple will have (4, 3, 2, 4, 4, 3)
l=[]
def lenWords(n):
    x=n.split(' ')
    for i in x:
        a=list(i)
        c=len(a)
        l.append(c)
    print(tuple(l))
STRING=input("Enter the string: ")
lenWords(STRING)