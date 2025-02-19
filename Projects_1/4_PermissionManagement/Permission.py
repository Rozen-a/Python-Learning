# 用户类
class User:
    __is_admin = False
    __is_logged_in = False

    def __init__(self, is_admin, is_logged_in):
        self.__is_admin = is_admin
        self.__is_logged_in = is_logged_in

    def get_is_admin(self):
        return self.__is_admin

    def get_is_logged_in(self):
        return self.__is_logged_in

    def set_is_admin(self, is_admin):
        self.__is_admin = is_admin

    def set_is_logged_in(self, is_logged_in):
        self.__is_logged_in = is_logged_in


# 权限判断
def permission_check(user):
    if user.get_is_logged_in() and user.get_is_admin():
        print('欢迎进入管理员页面')
    else:
        print('权限不足，无法访问管理员页面')


# 测试1：(is_admin, is_logged_in):(0, 0)
print('测试1：(is_admin, is_logged_in):(0, 0)')
user1 = User(0, 0)
permission_check(user1)

print()

# 测试2：(is_admin, is_logged_in):(0, 1)
print('测试2：(is_admin, is_logged_in):(0, 1)')
user2 = User(0, 1)
permission_check(user2)

print()

# 测试3：(is_admin, is_logged_in):(1, 0)
print('测试3：(is_admin, is_logged_in):(1, 0)')
user3 = User(1, 0)
permission_check(user3)

print()

# 测试4：(is_admin, is_logged_in):(1, 1)
print('测试4：(is_admin, is_logged_in):(1, 1)')
user4 = User(1, 1)
permission_check(user4)
