class Employee :
    def __init__(self,employee_id,name,age,salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary
    def introduce(self):
        print(f"员工id:{self.employee_id},姓名:{self.name},年龄:{self.age},工资:{self.salary}")

    def __str__(self):
        return f"员工id:{self.employee_id},姓名:{self.name},年龄:{self.age},工资:{self.salary}"

class EmployeeManager :

    def __init__(self):
        self.employees = []
    def add_employee(self,employee):
        self.employees.append(employee)

    def find_employee(self,id):
        for em in self.employees:
            if em.employee_id == id :
                return em
    def update_age(self,id,age):
        for em in self.employees:
                    if em.employee_id  == id :
                        em.age = age
                        return True
        return False            
    def show_all(self):
          for em in self.employees:
               print(em)
                      
        

manager = EmployeeManager()

employee1 = Employee(1, "张三", 25, 10000)
employee2 = Employee(2, "李四", 30, 15000)

manager.add_employee(employee1)
manager.add_employee(employee2)

manager.show_all()

result = manager.find_employee(2)

print(result)

manager.update_age(2, 31)

manager.show_all()