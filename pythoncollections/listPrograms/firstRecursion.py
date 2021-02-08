lst=['b','a','b','c']
xlst=[]
# lst.sort()
for i in lst:
    count=lst.count(i)
        if(count>1):
            xlst.append(i)
            print(xlst)
# if (lst[0]==olst[0])&(lst[0]==olst[1]):
#     print(lst[0])
# else:
#     print("No repetition")