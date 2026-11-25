class Employee :
    company = "上海科技有限公司"
    def __init__(self,employee_id,name,age,salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary
    def introduce(self):
        print(f"员工id:{self.employee_id},姓名:{self.name},年龄:{self.age},工资:{self.salary}")

    def __str__(self):
        return f"员工id:{self.employee_id},姓名:{self.name},年龄:{self.age},工资:{self.salary}"

    @classmethod
    def change_company(cls,company):
        cls.company = company
    @staticmethod
    def is_valid_age(age):
        if age >= 18:
            return True
        else :
            return False
class Manager(Employee):
    def __init__(self, employee_id, name, age, salary,team_size):
        super().__init__(employee_id, name, age, salary)       
        self.team_size = team_size 
    def introduce(self):
        super().introduce
        print( f"管理人数:{self.team_size}" )


manager = Manager(3, "王经理", 35, 20000, 8)

manager.introduce()

Employee.change_company("北京科技有限公司")

print(Employee.company)

print(Employee.is_valid_age(16))
print(Employee.is_valid_age(25))        
