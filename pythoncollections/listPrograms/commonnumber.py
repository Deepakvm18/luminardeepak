lst1=[1,2,3,4,5]
lst2=[2,3,4,56,7]
olist=[]
for i in lst1:
    for j in lst2:
        if i==j:
         olist.append(i)

print(olist)
