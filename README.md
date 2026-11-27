# Python Learning

我的 Python 学习项目。

## 学习目标

从 Java / PHP 开发转向 AI 应用工程师。

## 学习进度

| 课程 | 进度 | 练习 |
| --- | --- | --- |
| [Lesson 01 · Python 基础语法](lesson_01/) | 已通过（88 分） | 用列表和字典保存员工信息，遍历并按 ID 修改年龄 |
| [Lesson 02 · Python 函数](lesson_02/) | 已通过（92 分） | 用函数计算工资、按 ID 查询员工 |
| [Lesson 03 · Python 面向对象](lesson_03/) | 已有练习代码，待验收 | 员工管理、继承、方法类型、多态、`@property` |
| [Lesson 04 · 模块与文件操作](lesson_04/) | 已有练习代码，待验收 | 模块导入、查看 `sys.path`、读写文本文件 |

第四课的文件读写示例使用 `open()` 和 `close()`。复习时可以对比 `with open(...) as file`，解释代码块退出时为什么会关闭文件，以及抛出异常时会发生什么。

## 项目练习

员工管理练习从列表和字典开始，再用函数封装查询，最后用类区分员工数据和员工管理操作。

- **基础语法** — [遍历员工列表并修改年龄](lesson_01/employee_list_demo.py)。
- **函数** — [计算工资](lesson_02/calculate_salary.py)、[查询员工](lesson_02/find_employee.py)。查询不到时返回 `None`。
- **面向对象** — [员工管理](lesson_03/employee_manager.py)演示添加、查询、修改年龄和展示员工。另有[继承与方法类型](lesson_03/inheritance_and_methods.py)、[多态](lesson_03/polymorphism.py)和[工资属性校验](lesson_03/salary_property.py)。
- **模块与文件操作** — [导入工资模块](lesson_04/module_import_demo.py)、[查看 Python 的模块搜索路径](lesson_04/sys_path_demo.py)、[写入员工列表](lesson_04/write_employees_demo.py)、[读取员工列表](lesson_04/read_employees_demo.py)和[写入单条员工记录](lesson_04/write_employee_demo.py)。

## 运行示例

在仓库根目录用 Windows PowerShell 运行。以下示例只用到 Python 3 和标准库。

```powershell
python .\lesson_01\employee_list_demo.py
python .\lesson_02\find_employee.py
python .\lesson_03\employee_manager.py
python .\lesson_04\module_import_demo.py
python .\lesson_04\sys_path_demo.py
```

第四课的文件练习在当前目录读写相对路径。从仓库根目录进入 `lesson_04` 后，先写入 `employees.txt`，再运行读取脚本。写入示例会覆盖同名文件。

```powershell
Set-Location .\lesson_04
python .\write_employees_demo.py
python .\read_employees_demo.py
```
