n1=int(input("ENTER FIRST NUMBER: "))
n2=int(input("ENTER SECOND NUMBER: "))
n3=int(input("ENTER THIRD NUMBER: "))
if (n1>n2)&(n1>n3):
    print("FIRST NUMBER IS LARGEST")
elif (n2>n1)&(n2>n3):
    print("second number is largest")
elif (n3>n1)&(n3>n2):
    print("third number is largest")
else:
    print("numbers repeated or invalid")