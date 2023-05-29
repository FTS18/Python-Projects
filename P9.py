#Write a program that rotates the elements of a list so that the element at the first index moves to the second, second moves to the third, etc., and last elements moves to the first position.
inp=eval(input("Enter a list: "))
print("Original List: ", inp)
inp=inp[-1:]+inp[:-1]
print("New List: ", inp)