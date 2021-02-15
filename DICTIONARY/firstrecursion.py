pattern="ABABAC"
dict={}
for ch in pattern:
    if ch not in dict:
       dict[ch]=1
    else:
        print("FIRST RECURSIVE", ch)
        break
