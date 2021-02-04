power=int(input("ENTER THE POWER"))
n1=int(input("ENTER THE LOWER LIMIT"))
n2=int(input("ENTER THE UPPER LIMIT"))
for i in range(1,n2+1):
    if(i**power>=n1)&(i**power<=n2):
        print(i**power)