expense={"jan":28000,"feb":30000,"march":40000,"april":38000,"may":35000}
print(expense["feb"])

expense["april"]-=2000
print(expense)

expense["june"]=45000
print(expense)

if "march" in expense:
    print("entry exist")
else:
    print("not exist")

# check for july entry if not add july=52000

if "july" in expense:
    print("entry exist")
else:
    expense["july"]=52000
print(expense)