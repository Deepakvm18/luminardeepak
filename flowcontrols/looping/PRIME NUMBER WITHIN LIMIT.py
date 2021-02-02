l1=int(input("ENTER THE UPPER LIMIT"))
l2=int(input("ENTER THE LOWER LIMIT "))
flag = 0
for i in range( l1,l2+1):
    for j in range(2,i):
     if(i%j==0):
        flag=1
    if flag==0:
         print(i)

