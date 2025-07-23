names  = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
memos  = [ 0 , 1 , 1 , 2 , 2 , 1 , 2 , 1 , 2 , 2 ]
salary = [1000,2000,3000,4500,2000,5000,1500,2300,1300,1100]

removed=[]
for i in range(len(names)):
    if salary [i] > 4000:
        removed.append(names[i])
        
remaining = [
    (i, names[i], memos[i], salary[i])
    for i in range(len(names))
    if i not in removed
] 

remaining.sort(key=lambda x: x[3], reverse=True)

for emp in remaining:
    if memos[emp[0]] >= 2:
        removed.append(emp[0])
    if len(removed) == 5:
        break
    
    
removed_names = [names[i] for i in removed]

print("Employees to be removed:", removed_names)     
