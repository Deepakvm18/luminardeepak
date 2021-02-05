lst=[2,3,4,5]
num=int(input("ENTER THE NUMBER"))
sum=0
for i in lst:
    for j in lst:
        if (i+j==num)&(i!=j):
             print(i,j)
        break



