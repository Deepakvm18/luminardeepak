lst=[1,2,3,4,5]
num=int(input("ENTER THE NUMBER  "))
# sum=0
# for i in lst:
#     for j in lst:
#         if (i+j==num)&(i!=j):
#              print(i,j)5

#         break

low=0
upp=len(lst)-1
while(low<upp):
    total=lst[low]+lst[upp]
    if num==total:
        print(lst[low],lst[upp])
        low+=1
        upp-=1
    elif total>num:
        upp-=1

    elif total<num:
        low+=1

    else:
        print(" THERES NO VALID PAIR")


