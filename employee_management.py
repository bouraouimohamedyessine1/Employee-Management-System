from numpy import*
number_of_employee=int(input("How many employee? "))
e=[]
for i in range(number_of_employee):
    employee_name=input("Give me your name : ")
    employee_id=int(input("\nGive me your ID :"))
    employee_age=int(input("\nYour age : "))
    employee_salary=float(input("\n Your salary :"))
    e.append(dict())
    e[i]["name"]=employee_name
    e[i]["id"]=employee_id
    e[i]["age"]=employee_age
    e[i]["salary"]=employee_salary
for i in range(number_of_employee):
    print(f"====EMPLOYEE INFORMATIONS====\n employe{i+1}: Name:{e[i]['name']} \n ID: {e[i]['id']} \n Age: {e[i]['age']} \n Salary: {e[i]['salary']}TND \n")
id_to_search=int(input("Enter employee id to search it"))
found=0
i=0
while(found==0 and i<number_of_employee):
    if e[i]["id"]==id_to_search:
        found=1
        print(f"====EMPLOYEE INFORMATIONS====\n employee found: Name:{e[i]['name']} \n ID: {e[i]['id']} \n Age: {e[i]['age']} \n Salary: {e[i]['salary']}TND \n")
    else:
        i+=1
if(found==0 ):
    print("employee does't exist")
