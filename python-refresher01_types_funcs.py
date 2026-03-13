###01_types_funcs.py


###一、定义基础数据（字符串变量、列表、字典、集合、元组）


class_name =  "python_programming"
student_name = ["one","two","three","four","five"]
student_grade = {"one":45,
                 "two":96,
                 "three":73,
                 "four":82,
                 "five":65 }
homework_finished = ("one","three","five")
class_stage = ("basic","advanced","project")

print(class_name)#打印字符串变量

for i in student_name:#打印列表
    print(i)

for name, grade in student_grade.items():
    print(f"student {name} 's grade is {grade}")#打印字典

for i in homework_finished:
    print(i)#打印集合

for i in class_stage:
    print(i)#打印元组


###二、字符串处理（大写、小写、输出长度）


print(class_name.upper())

print(class_name.lower())

print(len(class_name))

sub_str = "python"
if sub_str in class_name:
    print("YES")
else:
    print("NO")


###三、遍历数据


for name in student_name:
    if name in homework_finished:
        print(f"{name} submitted homework")
    else:
        print(f"{name}  dosn't submitted homework")


###四、条件判断

 
for name,score in student_grade.items():
    if score >= 90:
        print(f"{name} is level A")  
    elif score >= 80 and score <= 89:
        print(f"{name} is level B")
    elif score >= 70 and score <= 79:
        print(f"{name} is level C")
    elif score >= 60 and score <= 69:
        print(f"{name} is level D")
    else:
        print(f"{name} is level E")


###五、列表推导式


list_good = []
list_good = [name for name in student_name if student_grade[name] >= 85]
print(list_good) #score>85 student_name

list_all = []
list_all = [score for score in student_grade.values()]
print(list_all)


###六、函数


def average(num_list):#计算平均值函数
    return sum(num_list) / len(num_list)
ave = average(list(student_grade.values()))
print(ave)

def hello(studentname = None):#问候函数
    if studentname is None:
        print("hello student")
    else:
        print("hello " + (studentname))
hello()

def plus(grade_sum):
    return sum(grade_sum)
grade_plus = plus(list(student_grade.values()))
print(grade_plus)


###七、条件统计


upstudent = 0
downstudent = 0
for score in student_grade.values():
    if score >= 60:
        upstudent += 1
    else:
        downstudent += 1
print("The number of passing students:" , upstudent)
print("The number of unpassing students:" , downstudent)


###八、While循环


i = 0
while i < 5:
    i += 1
    print(i)


###九、模块使用


import statistics
print(statistics.mean(student_grade.values()))

import random
num = random.randint(1,10)
print(num)
