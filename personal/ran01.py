x=input("Enter two integers: ")
y=x.split()
g,f=bin(int(y[0]))[2:],bin(int(y[1]))[2:]
p,q=len(g),len(f)
if p<q:
    g='0'*(q-p)+g
else:
    f='0'*(p-q)+f
count=0
for i in range(len(g)):
    if g[i]!=f[i]:
        count+=1
print(g,f)
print(count)