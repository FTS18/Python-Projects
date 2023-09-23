def fetchEven(L):
    l=[]
    for i in L:
        if i%2==0:
            l.append(i)
    print(l)
fetchEven([1,2,3,4])