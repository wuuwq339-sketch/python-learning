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
        super().introduce()
        print( f"管理人数:{self.team_size}" )


employee = Employee(1, "张三", 25, 10000);
manager = Manager(2, "李四", 30, 15000,8);

list = [employee,manager]
for em in list:
    em.introduce()
