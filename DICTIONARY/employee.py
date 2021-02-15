emp={"ID":"BOND007","Name":"Deepak","Designation":"SOFTWARE DEVELOPER","SALARY":23000}
print("Name=", emp["Name"],"\n" ,"Designation=" , emp["Designation"])
if "gender" in emp:
    print("entry exist")
else:
    emp["gender"] = "MALE"
print(emp)
for k,v in emp.items():
    print(k,v)