pi=22/7
def x0():
    x=input('''Hi there!
Press <option number> to continue
Note: Enter units in metres
Pick one option:
1) 2D
2) 3D
''')
    if x=="1":
        x1()
    elif x=="2":
        x2()
    else:
        check_inp(x0)

def x1():
    a=input('''
Pick one:
1) Rectrangle
2) Circle
3) Triangle
''')
    if a=="1":
        l=int(input("Enter length: "))
        b=int(input("Enter breadth: "))
        print("Area: ", str(l*b)+"m^2")
        print("Perimeter: ", str(2*(l+b))+"m")
    elif a=="2":
        r=int(input("Enter radius: "))
        print("Area: ", round(pi*(r**2),4),"m^2")
        print("Circumference: ", round(2*pi*r,4),"m")
    elif a=="3":
        b=int(input("Enter base: "))
        h=int(input("Enter height: "))
        print("Area: ", round((1/2)*b*h,4),"m^2")
        print("Perimeter: ", round(h+b+((h**2+b**2)**(1/2)),4),"m")
    else:
        check_inp(x1)
        
def x2():
    a=input('''
Pick one:
1) Cuboid
2) Sphere
3) Cone
''')
    if a=="1":
        l=int(input("Enter length: "))
        b=int(input("Enter breadth: "))
        h=int(input("Enter height: "))
        print("Volume: ", str(l*b*h)+"m^3")
        print("Surface Area: ", str(2*(l*b+b*h+h*l))+"m^2")
    elif a=="2":
        r=int(input("Enter radius: "))
        print("Volume: ", round((4/3)*pi*(r**3),4),"m^3")
        print("Surface Area: ", round(4*pi*(r**2),4),"m^2")
    elif a=="3":
        r=int(input("Enter base radius: "))
        h=int(input("Enter height: "))
        l=(r**2+h**2)**(1/2)
        print("Volume: ", round((1/3)*pi*(r**2)*h,4),"m^3")
        print("Surface Area: ", round(r*pi*(r+l),4),"m^2")
    else:
        check_inp(x2)
        
def check_inp(xy):
    while True:
        y=input('''
Invalid Input, try again (y/n) ''').lower()
        if y=="yes" or y=="y":
            print("ok")
            xy()
        else:
            print("Bye!")

x0()

