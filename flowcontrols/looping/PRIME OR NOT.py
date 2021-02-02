num=int(input("ENTER THE NUMBER "))

if num<=0:
    print("NEITHER PRIME NOR COMPOSITE")
else:
    flag = 0
    for i in range(2,num):
     if(num%i==0):
        flag=1
    if flag==0:
         print("IT IS  PRIME")

    else:
        print("IT IS not PRIME")