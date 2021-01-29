n1=int(input("ENTER FIRST NUMBER: "))
n2=int(input("ENTER SECOND NUMBER: "))
n3=int(input("ENTER THIRD NUMBER: "))
if (n1>n2)&(n2>n3):
    if(n2>n3):
        print(n3,n2,n1)
    else:
        print(n2,n3,n1)

elif (n2>n1)&(n2>n3):
        if(n1>n3):
            print(n3,n1,n2);
        else:
            print(n1,n3,n2)

elif (n3>n1)&(n3>n2):
        if(n2>n1):
            print(n1,n2,n3)
        else:
            print(n2,n1,n3)

