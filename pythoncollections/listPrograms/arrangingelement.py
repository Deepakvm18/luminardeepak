lst=[10,11,10,12,13,10,9]
ele=int(input("enter the element you want to isolate"))
# olist=[]
# for i in lst:
#     if(ele==i):
#         olist.append(i)
#         lst.remove(i)
# for i in olist:
#     lst.append(i)
# print(lst)
for j in lst:
    for i in range(0,len(lst)-1):
         if(lst[i]==ele):
            t=lst[i]
            lst[i]=lst[i+1]
            lst[i+1]=t
print(lst)
