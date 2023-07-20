def countNow(n):
    value=list(n.values())
    L=[]
    for i in value:
        c=len(i)
        if c>5:
            print(i.upper())

PLACES={1:"Delhi",2:"London",3:"Paris",4:"New York",5:"Doha"} 
countNow(PLACES)