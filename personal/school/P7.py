#Write a Python program to implement a stack using list
stack=[]
stack.extend(["a","b","c"])
inp=str(input("Enter a stack: ").split(","))
x=["[","(","]",")","{","}"]
for i in inp:
    if i in x:
        inp=inp.replace(i,'')
print("Original Stack: ", stack)
stack.extend(eval(inp))
print("New Stack: ", stack)
for i in range(0,len(stack)):
    print("Stack after removing "+stack.pop()+" is: "+ str(stack))
print("Stack: ", list(stack))