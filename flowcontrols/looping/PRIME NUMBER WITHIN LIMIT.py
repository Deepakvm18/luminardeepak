l1=int(input("ENTER THE LOWER LIMIT"))
l2=int(input("ENTER THE UPPER LIMIT "))

for i in range( l1,l2+1):
    flag=0
    for j in range(2,i):
     if(i%j==0):
        flag=1
        break
    if (flag==0):
        print(i)
