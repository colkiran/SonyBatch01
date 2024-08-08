Fl=open("emp.csv",'r')

gender_count={}
departments=[]
designation=[]
salaries=0

for line in Fl.readlines():
    t=line.split(',')[2]
    if t in gender_count:
        gender_count[t]+=1
    else:
        gender_count[t]=1

    dept=line.split(',')[4]
    if dept not in departments:
        departments.append(dept)

    des = line.split(',')[3]
    if des not in designation:
        designation.append(des)

    sal=line.split(',')[5]
    salaries+=int(sal)


Fl.close()

print(f"Count of males and females:{gender_count}")
print(f"Unique list of depts:{departments}")
print(f"Unique list of designations:{designation}")
print(f"Sum of salaries:{salaries}")