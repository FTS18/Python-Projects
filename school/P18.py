import pickle 
f= open("empty.dat","wb")
d={"name":"xyz","age":"22","address":"69 Street, Secx Avenue","number":"6969696969"}
pickle.dump(d,f)
f.close()
f2= open("empty.dat","rb")
print(pickle.load(f2))