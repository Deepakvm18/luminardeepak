employees=[
    [100,"tom","developer",25000],
    [101,"savio","jobless",0],
    [103,"deepak","developer",100000],
    [104,"dilu","ma",1223],
 ]
sallist=[]
# TO PRINT ALL EMPLOYEE NAMES
for employee in employees:
    print(employee[1])

# TO FIND ALL DEVELOPERS

for employee in employees:
    if employee[2]=="developer":
         print(employee)
sum=0
for employee in employees:
    sum=sum+employee[3]
print(sum)

# HIGHEST SALARY
for employee in employees:
    sallist.append(employee[3])
print("HIGHEST SALARY IS " ,max(sallist))
# highsal=max(map(lambda emp:emp[3],employees))      <----FOR PROS