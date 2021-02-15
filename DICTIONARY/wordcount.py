text="hello hi hello hi hello"
words=text.split(" ")
dict={}
for word in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
# high=0
# i=0
# for num in dict:
#     if high<dict[num]:
#         high=dict[num]
#         i=num
# print(" MOST OCCURED ELEMENT IS ", i)
print(max(dict,key=dict.get))

# to sort a dictionary
sorted(dict,key=dict.get,reverse=True)

print(dict)
