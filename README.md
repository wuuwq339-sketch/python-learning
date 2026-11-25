# Python Learning

我的 Python 学习项目。

## 学习目标

从 Java / PHP 开发转向 AI 应用工程师。

## 学习记录

- Lesson 01：Python 基础语法，已通过（88 分）。
- Lesson 02：Python 函数，已通过（92 分）。
- Lesson 03：Python 面向对象，待验收。仓库已有 `Employee` 和 `EmployeeManager` 练习代码，以及继承和方法类型的练习。

## 项目练习

员工管理练习从列表和字典开始，再用函数封装查询，最后用类区分员工数据和员工管理操作。

| 阶段 | 练习文件 | 内容 |
| --- | --- | --- |
| 基础语法 | [employeeManageSystem.py](employeeManageSystem.py) | 遍历员工列表，按 ID 修改员工年龄 |
| 函数 | [basicDef.py](def.py/basicDef.py)、[employeSearch.py](def.py/employeSearch.py) | 计算工资，按 ID 查询员工并处理未找到的情况 |
| 面向对象 | [employeeManagerSysToObj.py](thirdLesson/employeeManagerSysToObj.py) | 用 `Employee` 表示员工，用 `EmployeeManager` 添加、查询、修改年龄和展示员工 |
| 面向对象 | [extendAndThreeMethod.py](thirdLesson/extendAndThreeMethod.py) | 练习继承、方法重写，以及实例方法、类方法和静态方法 |

## 运行示例

在仓库根目录用 Python 3 运行下面的命令，即可查看员工列表练习、员工查询和面向对象版本的输出。

```powershell
python .\employeeManageSystem.py
python .\def.py\employeSearch.py
python .\thirdLesson\employeeManagerSysToObj.py
```
