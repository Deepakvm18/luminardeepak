isl={"MUMBAI CITY":32,"CHENNAIN FC":18,"KERALA BLASTERS":29,"ATK MOHAN BAGUN":12}
lst=[]
for k in isl:
    lst.append(isl[k])
lst.sort()
i=(len(lst))-1
while i>=0:
    for k in isl:
        if isl[k]==lst[i]:
            print(k,isl[k])
    i-=1