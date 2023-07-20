#Write a function INDEX_LIST(L), where L is the list of elements passed as argument to the function. The function returns another list named ‘indexList’ that stores the indices of all Non-Zero Elements of L. For example: If L contains [12,4,0,11,0,56] The indexList will have - [0,1,3,5]
indexList=[]
def index_List(n):
    for i in n:
        if i!=0:
            x=n.index(i)
            indexList.append(x)
    return indexList
L=eval(input("Enter list: "))
print(index_List(L))