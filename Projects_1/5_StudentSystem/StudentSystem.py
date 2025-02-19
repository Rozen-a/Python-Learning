# Student类
class Student:
    def __init__(self):
        self.__name = 'Unknown'
        self.__score = 0.0

    # 更新成绩
    def update_score(self, new_score):
        self.__score = new_score

    # 输出学生信息
    def get_info(self):
        print('姓名：', self.__name, '\t成绩：', self.__score)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score


# 10个学生信息数据
students_info = [
    ["Alice", 85],
    ["Bob", 90],
    ["Charlie", 78],
    ["David", 92],
    ["Eve", 88],
    ["Frank", 76],
    ["Grace", 95],
    ["Hank", 83],
    ["Ivy", 89],
    ["Jack", 91]
]

# 实例化学生对象
i = 0
students = []
while i < len(students_info):
    student = Student()
    student.name = students_info[i][0]
    student.score = students_info[i][1]
    students.append(student)
    i += 1

print('姓名\t\t成绩')
print('-'*20)
for student in students:
    print(f'{student.name:<16} {student.score}')