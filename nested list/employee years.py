employees=[
    [100,"tom","developer",25000,1998,2017],
    [101,"savio","jobless",0,1997,2014],
    [103,"deepak","developer",100000,1998,2045],
    [104,"dilu","ma",1223,2017,2026]
]
# high=[]
# for exp in employees:
#     high.append(exp[5]-exp[4])
# print("HIGHEST EXPERIENCE = ", max(high) )
high=0
i=0
for emp in employees:
    if high<(emp[5]-emp[4]):
        high=emp[5]-emp[4]
        i=emp
print("HIGHEST EXPERIENCE = ",high,"& DETAILS OF THE EMPLOYEE ARE" ,i)