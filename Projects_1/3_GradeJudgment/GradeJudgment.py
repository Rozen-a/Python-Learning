def check_pass(grade):
    if grade >= 60:
        print('恭喜，你通过了考试！')
    else:
        print('很遗憾，未通过考试。')


grade = float(input('请输入成绩:'))
check_pass(grade)
