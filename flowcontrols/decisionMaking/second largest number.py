n1=int(input("ENTER FIRST NUMBER: "))
n2=int(input("ENTER SECOND NUMBER: "))
n3=int(input("ENTER THIRD NUMBER: "))
if (n1>n2)&(n1>n3):
    if(n2>n3):
        print("n2 NUMBER IS second LARGEST")
    else:
        print("n3 is second largest")

elif (n2>n1)&(n2>n3):
        if(n1>n3):
            print("n1 is second largest");
        else:
            print("n3 is second largest")

elif (n3>n1)&(n3>n2):
        if(n2>n1):
            print("n2 is second largest")
        else:
            print("n1 is secomd largest")

