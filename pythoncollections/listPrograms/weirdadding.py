lst=[2,6,5]
sum=0
olist=[]
for num in lst:
    sum=sum+num
for num in lst:
    num=sum-num
    olist.append(num)

print(olist)
