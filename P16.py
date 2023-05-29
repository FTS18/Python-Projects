sample={"Ananay":85, "Aditya":90, "Arunjay":89, "Arush":65, "Dishank":70, "Ishan":82}
value=list(sample.values())
key=list(sample.keys())
L=[]
for i in value:
    if i>75:
        c=value.index(i)
        x=key[c]
        L.append(x)
print("Students with marks>75: ", L)