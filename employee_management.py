from numpy import*
def employees_number():
    number_of_employee=int(input("How many employee? "))
    while number_of_employee<=0:
        number_of_employee=int(input("How many employee? "))
    return number_of_employee
def employees_informations(number_of_employee):
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
    return e
def display_employees_informations(number_of_employee,e):
    for i in range(number_of_employee):
        print(f"====EMPLOYEE INFORMATIONS====\n employe{i+1}: Name:{e[i]['name']} \n ID: {e[i]['id']} \n Age: {e[i]['age']} \n Salary: {e[i]['salary']}TND \n")
def search_employee(e,number_of_employee):
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
def avg_salary_employee(e,number_of_employee):
    s=0
    for i in range(number_of_employee):
        s+=e[i]["salary"]
    avg=s/number_of_employee
    print(f"number of employee : {number_of_employee} \n average salary : {avg:.2f}")
def delete_employee(e):
    del_employee=int(input("Give me the ID of the employee that i should delete"))
    i=0
    x=0
    while(i<len(e)):
        if e[i]["id"]==del_employee:
            del(e[i])
            x=1
            break
        i+=1
    if x==0:
        print("employee does not exist")
def update_salary(e):
    employee_id=int(input("Give me your ID :"))
    i=0
    x=0
    while i<len(e) and x==0:
        if employee_id==e[i]["id"]:
            new_salary=float(input("Enter new salary :"))
            e[i]["salary"]=new_salary
            x=1
            print("Salary updated succesfully")
        i+=1
    if x==0:
        print("employee does niot exist")
    return e


