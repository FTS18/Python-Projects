import time
t1=time.time()
inp=input(">>")
t2=time.time()
c=w=0
for i in list(inp.split()):
    w+=1
for i in inp:
    c+=1
t=(t2-t1)
print("Words typed : ",w)
print("Characters  : ",c)
print("Time elapsed: ",round(t,3))
print("Speed (wpm) : ",round(w/(t/60),3))
print("Speed (wps) : ",round(w/t,3))
print("Speed (cpm) : ",round(c/(t/60),3))
print("Speed (cps) : ",round(c/t,3))