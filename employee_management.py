import json
def employees_number():
    number_of_employee=int(input("How many employee? "))
    while number_of_employee<=0:
        number_of_employee=int(input("How many employee? "))
    return number_of_employee
def verif(e,employee_id):
    i=0
    test=True
    while test and i<len(e):
        if e[i]["id"]==employee_id:
            print("ID already exist \n")
            test=False
        i+=1
    return test
def verif_salary(employee_salary):
    test=True
    if employee_salary<0:
        print("Sarlary Error")
        test=False
    return test
        
def verif_id(employee_id):
    test=True
    if len(str(employee_id))!=8:
        test=False
    return test
def verif_age(employee_age):
    test=True
    if not(18<=employee_age<=64):
            print("Your age is unrealstic")
            test=False
    return test
def employees_informations(number_of_employee):
    e=[]
    for i in range(number_of_employee):
        employee_name=input("Give me your name : ")
        employee_id=int(input("\nGive me your ID :"))
        while not(verif_id(employee_id)):
            employee_id=int(input("\nError give me other your ID :"))
        employee_age=int(input("\nYour age : "))
        while not(verif_age(employee_age)):
            employee_age=int(input("\nYour age : "))
        employee_salary=float(input("\n Your salary :"))
        while not(verif_salary(employee_salary)):
            employee_salary=float(input("\n Your salary :"))
        while not verif(e,employee_id):
            employee_id=int(input("\nGive me your ID :"))
            employee_name=input("Give me your name : ")
            employee_age=int(input("\nYour age : "))
            employee_salary=float(input("\n Your salary :"))
        e.append(dict())
        e[i]["name"]=employee_name
        e[i]["id"]=employee_id
        e[i]["age"]=employee_age
        e[i]["salary"]=employee_salary
    return e
def display_employees_informations(number_of_employee,e):
    print("====EMPLOYEE INFORMATIONS====\n")
    for i in range(number_of_employee):
        print(f" employe{i+1}: Name:{e[i]['name']} \n ID: {e[i]['id']} \n Age: {e[i]['age']} \n Salary: {e[i]['salary']}TND \n")
def search_employee_by_id(e,number_of_employee):
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
    print(f"number of employee : {number_of_employee} \n total payroll :{s:.2f} average salary : {avg:.2f}")
def delete_employee(e):
    del_employee=int(input("Give me the ID of the employee that i should delete"))
    i=0
    x=0
    while(i<len(e)):
        if e[i]["id"]==del_employee:
            del(e[i])
            x=1
            save_employee(e)
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
        print("employee does not exist")
    save_employee(e)
    return e
def rank_employees_based_on_salary(e):
    for i in range(len(e)-1):
        for j in range(i+1,len(e)):
            if e[i]["salary"]<e[j]["salary"]:
                x=e[i]
                e[i]=e[j]
                e[j]=x
    print("====Rank employees based on salary====\n")
    for i in range(len(e)):
        print(f" employe{i+1}: Name:{e[i]['name']} \n ID: {e[i]['id']} \n Salary: {e[i]['salary']}TND \n")
def search_employee_by_name(e):
    name_to_search=(input("Enter employee id to search it"))
    found=0
    i=0
    while(found==0 and i<len(e)):
        if e[i]["name"]==name_to_search:
            found=1
            print(f"====EMPLOYEE INFORMATIONS====\n employee found: Name:{e[i]['name']} \n ID: {e[i]['id']} \n Age: {e[i]['age']} \n Salary: {e[i]['salary']}TND \n")
        else:
            i+=1
    if(found==0 ):
        print("employee does't exist")
def add_employee(e):
    employee_name=input("Give me your name : ")
    employee_id=int(input("\nGive me your ID :"))
    while not(verif_id(employee_id)):
        employee_id=int(input("\nError give me other your ID :"))
    employee_age=int(input("\nYour age : "))
    while not(verif_age(employee_age)):
        employee_age=int(input("\nYour age : "))
    employee_salary=float(input("\n Your salary :"))
    while not(verif_salary(employee_salary)):
        employee_salary=float(input("\n Your salary :"))
    while not verif(e,employee_id):
        while not(verif_id(employee_id)):
            employee_id=int(input("\nGive me your ID :"))
        employee_name=input("Give me your name : ")
        while not(verif_age(employee_age)):
            employee_age=int(input("\nYour age : "))
        while not(verif_salary(employee_salary)):
            employee_salary=float(input("\n Your salary :"))
    e.append(dict())
    e[len(e)-1]["name"]=employee_name
    e[len(e)-1]["id"]=employee_id
    e[len(e)-1]["age"]=employee_age
    e[len(e)-1]["salary"]=employee_salary
    save_employee(e)
    return e
def verif2(e,employee_age,employee_salary):
    test=True
    i=0
    if employee_salary<0:
        print("Sarlary Error")
        test=False
    if not(18<=employee_age<=64):
        print("Your age is unrealstic")
        test=False
    return test
def edit_employee(e):
    id=int(input("Enter the employee's ID :"))
    i=0
    x=0
    while i<len(e):
        if id==e[i]["id"]:
            x=1
            employee_name=input("Give me your name : ")
            employee_age=int(input("\nYour age : "))
            employee_salary=float(input("\n Your salary :"))
            while not verif2(e,employee_age,employee_salary):
                employee_name=input("Give me your name : ")
                employee_age=int(input("\nYour age : "))
                employee_salary=float(input("\n Your salary :"))
            e[i]["name"]=employee_name
            e[i]["age"]=employee_age
            e[i]["salary"]=employee_salary
            save_employee(e)
                
        i+=1
    if x==0:
        print("Employee does not exist")
    return e
def save_employee(e):
    with open("employee.json","w") as file:
        json.dump(e,file,indent=4)
def load_employee():
    try:
        with open("employee.json","r") as file:
            x=json.load(file)
    except:
        x=[]
    return x








x=load_employee()
if len(x)==0:
    number_of_employee=employees_number()
    e=employees_informations(number_of_employee)
    save_employee(e)
    x=load_employee()
    s=1
    while s!=0:
        s=int(input("\n\n1. Display_employees_informations \n2. Search_employee_by_id\n3. Search_employee_by_name\n4. Avg_salary_employee\n5. Update_salary \n6. Delete_employee\n7. Rank_employees_based_on_salary\n8. Add_employee \n9. Edit_employee\n0. Exit\n "))
        if(s==1):
            display_employees_informations(len(x),x)
        elif s==2:
            search_employee_by_id(x,len(x))
        elif s==3:
            search_employee_by_name(x)
        elif s==4:
            avg_salary_employee(x,len(x))
        elif s==5:
            update_salary(x)
        elif s==6:
            delete_employee(x)
        elif s==7:
            rank_employees_based_on_salary(x)
        elif s==8:
            add_employee(x)
        elif s==9:
            edit_employee(x)
        elif s==0:
            print("Thank youu")
        else:
            print("You should enter a number between 0 and 9")
else:
    display_employees_informations(len(x),x)
    s=1
    while s!=0:
        s=int(input("\n\n1. Display_employees_informations \n2. Search_employee_by_id\n3. Search_employee_by_name\n4. Avg_salary_employee\n5. Update_salary \n6. Delete_employee\n7. Rank_employees_based_on_salary\n8. Add_employee \n9. Edit_employee\n0. Exit\n "))
        if(s==1):
            display_employees_informations(len(x),x)
        elif s==2:
            search_employee_by_id(x,len(x))
        elif s==3:
            search_employee_by_name(x)
        elif s==4:
            avg_salary_employee(x,len(x))
        elif s==5:
            update_salary(x)
        elif s==6:
            delete_employee(x)
        elif s==7:
            rank_employees_based_on_salary(x)
        elif s==8:
            add_employee(x)
        elif s==9:
            edit_employee(x)
        elif s==0:
            print("Thank youu")
        else:
            print("You should enter a number between 0 and 9")
