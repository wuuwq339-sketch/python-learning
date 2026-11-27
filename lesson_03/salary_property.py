class Employee:
    def __init__(self,salary):
        self._salary = salary
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if value < 0:
            raise ValueError("工资不能小于0")
        self._salary = value

employee = Employee(10000)

print(employee.salary)

try:
    employee.salary = -15000
except ValueError as e:
    print("发生异常：", e)

print(employee.salary)
