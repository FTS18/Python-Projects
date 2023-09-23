d={
    "Jan":31,
    "Feb":29,
    "Mar":31,
    "Apr":30,
    "May":31,
    "Jun":30,
    "Aug":31,
    "Sep":30,
    "Oct":31,
    "Nov":30,
    "Dec":31,
}
keys=list(d.keys())
values=list(d.values())

print("Months with 31 days are: ", end="")
for month, days in d.items():
    if days == 31:
        print(month, end=" ")
print()

for key in sorted(d.keys()):
    value = d[key]
    print(f"{key}: {value}")
    
inp=input("Enter the month: ")
for i in keys:
    if i==inp:
        print("Number of days in",inp,"is:", d[i])
print(sorted(keys))