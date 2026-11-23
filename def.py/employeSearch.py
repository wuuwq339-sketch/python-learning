# 功能要求：
# 1. 接收员工列表。
# 2. 接收需要查询的员工 ID。
# 3. 使用 for 遍历员工列表。
# 4. 使用 if 判断 ID 是否匹配。
# 5. 找到后返回对应的员工字典。
# 6. 没找到返回 None。

employees = [
    {"id": 1, "name": "张三", "age": 25},
    {"id": 2, "name": "李四", "age": 30},
    {"id": 3, "name": "王五", "age": 28}
]

def find_employee(employees, employee_id):
    for em in employees :
        if em["id"] == employee_id :
            return em
    return None

result = find_employee(employees , 99)

print(result)