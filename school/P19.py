indexList=[]
def INDEX_LIST(L):
    for i in range(len(L)):
        if l[i]!=0:
            indexList.append(i)
    return indexList
l=list(eval(input("Enter a list: ")))
print(INDEX_LIST(l))