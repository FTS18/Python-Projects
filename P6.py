#Write a random number generator that generates random numbers between 1 and 6 (simulates a dice)
from random import *
y=["yes","y","ye","yee","yed","yew","ya","yup"]
i=1
while i>0:
    num=randrange(1,7)
    print("Turn", str(i)+":", num)
    x=input("Reroll?: ")
    i+=1
    if x in y:
        continue
    else:
        break