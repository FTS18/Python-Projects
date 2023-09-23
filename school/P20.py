import pickle
f=open("file1.pkl",'wb+')
l={"Ananay": 1,"Nirupaksh":2}
pickle.dump(l,f)
f.close()
f1=open("file1.pkl","rb")
print(pickle.load(f1))
f1.close()