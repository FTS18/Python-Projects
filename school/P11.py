#Write a program and create a function that receives a decimal number and prints the equivalent number in other bases i.e., in binary, octal and hexadecimal equivalents
inp=int(input("Enter any number: "))
print("Decimal    :", "00"+str(inp))
print("Binary     :", bin(inp))
print("Octal      :", oct(inp))
print("Hexadecimal:", hex(inp))