arr=[10,1,2,13,14,16,5]
element=int(input("ENTER THE NUMBER "))
flag=0
for num in arr:
    if(element==num):
        flag=1
        break
if flag==0:
    print("element not found")
else:
    print("element found")