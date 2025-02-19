grades = [59, 56, 87, 82, 72, 77, 100, 54, 100, 96,
          93, 55, 55, 98, 61, 59, 53, 84, 74, 68,
          57, 66, 80, 94, 60, 99, 93, 77, 89, 72,
          85, 91, 71, 91, 70, 81, 93, 59, 62, 70,
          53, 80, 53, 71, 77, 94, 59, 64, 57, 58]

print(f'最高分：{max(grades)}')

print(f'最低分：{min(grades)}')

print('成绩降序排列：')
grades_sorted = sorted(grades, reverse=True)
print(grades_sorted)

grades_avg = round(sum(grades)/len(grades), 2)
print(f'平均分：{grades_avg}')
passed = [i for i in grades if i >= grades_avg]
print(f'大于等于平均成绩的学生数：{len(passed)}')
