import math

def welcome():
    print('''>> Welcome to Calculator.py''')

def reciprocal(f):
    return 1.0 / f
    
def calculateApn():
	a=float(input(">> Enter First Term: "))
	d=float(input(">> Enter Common Difference: "))
	n=int(input(">> Which Term would you like to find?: "))
	Tn=(a+(n*d)-d)
	print (">> Nth Term for the given set of numbers is: ",Tn)
	for i in range(1,n+1):t_n = a + (i-1)*d;
	print(t_n)
def calculateGpn():
	a=float(input(">> Enter First Term: "))
	r=float(input(">> Enter Common Ratio: "))
	n=int(input(">> Which Term would you like to find?: "))
	Tn=(a*(r**(n-1)))
	print (">> Nth Term for the given set of numbers is: ",Tn)
#Baaki haii
def calculateHpn():
	a=float(input(">> Enter First Term: "))
	d=float(input(">> Enter Common Difference: "))
	n=int(input(">> Which Term would you like to find?: "))
	Tn1=int(a+(n*d)-d)
	Tn=reciprocal(Tn1)
	print (">> Nth Term for the given set of numbers is: ",Tn)

def add():
	a=int(input(">> Enter First Number: "))
	b=int(input(">> Enter Second Number: "))
	c=a+b
	print (c)
	
def subtract():
	a=int(input(">> Enter First Number: "))
	b=int(input(">> Enter Second Number: "))
	c=a-b
	print (c)
	
def sin():
	x=int(input(">> Enter angle: "))
	y=math.radians(x)
	z=math.sin(y)
	print(round(z, 5))

def cos():
	x=int(input(">> Enter angle: "))
	y=math.radians(x)
	z=math.cos(y)
	print(round(z, 5))

def csc():
	x=int(input(">> Enter angle: "))
	y=math.radians(x)
	z=reciprocal(math.sin(y))
	print(round(z, 5))

def sec():
	x=int(input(">> Enter angle: "))
	y=math.radians(x)
	z=reciprocal(math.cos(y))
	print(round(z, 5))

def tan():
	x=int(input(">> Enter angle: "))
	y=math.radians(x)
	z=math.tan(y)
	print(round(z, 5))

def cot():
	x=int(input(">> Enter angle: "))
	y=math.radians(x)
	z=reciprocal(math.tan(y))
	print(round(z, 5))


def trigonometricFx():
	fx=input('''>> Which Trigonometric Ratio?
sin for sin∅
cos for cos∅
tan for tan∅
csc for cosec∅
sec for sec∅
cot for cot∅
>> ''')
	if fx=="sin":
		sin()
	elif fx=="cos":
		cos()
	elif fx=="tan":
		tan()
	elif fx=="csc":
		csc()
	elif fx=="sec":
		sec()
	elif fx=="cot":
		cot()

def restartProgram():
	restart=input('''>> Sorry, I didn't got what you wrote.
Do you want to calculate again? [y/n]
>> ''')
	if restart=="y":
		main()
	elif restart=="n":
		print(">> Have a good day. Bye!")
		return 0
	else:
		print(">> Invalid Response. The program has closed.")
		return 0

def prime(x,y):
	prime_list =[]
	for i in range(x,y):
	    	if i == 0 or i == 1:
	    		continue
	    	else:
	    		for j in range(2, int(i/2)+1):
	    			if i % j == 0:
	    				break
	    			else:
	  			  	prime_list.append(i)
	return prime_list
welcome()
print('''
>> Which mathematical operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
! for factorial
c for complex operations
p for prime numbers
t for trigonometric operations

For nth terms of:-
apn for arithmatic progression
gpn for geometric progression
hpn for harmonic progression
''')

def main():
	userInput=input(">> ").lower()
	var_1=len(userInput)
	if userInput=="apn":
		calculateApn()
	elif userInput=="gpn":
		calculateGpn()
	elif userInput=="hpn":
		calculateHpn()
	elif userInput=="c":
		calc = input(">> Type calculation: ")
		print(">> Result: " + str(eval(calc)))
	elif userInput=="t":
		trigonometricFx()
	elif userInput=="+":
	 	add()
	elif userInput=="-":
		subtract()
	elif userInput=="p":
		lower = int(input(">> Enter Lower Limit: "))
		upper = int(input(">> Enter Upper Limit: "))
		lst = prime(lower,upper)
		res = [*set(lst)]
		if len(lst) == 0:
	  	  print(">> There are no prime numbers in this range")
		else:
			print(">> The prime numbers in this range are: ", res)
	elif var_1==0:
		print (">> \033[A                                                 \033[A")
		restartProgram() 
		
if __name__ == '__main__':
    main()
