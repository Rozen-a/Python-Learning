MIN_BALANCE = 100.0  # 最低余额


# BankAccount 类
class BankAccount:
    __balance = 0.0  # 余额

    # 构造方法
    def __init__(self, new_balance):
        self.__balance = new_balance

    # 存款
    def deposit(self, amount):
        self.__balance += amount

    # 取款
    def withdraw(self, amount):
        self.__balance -= amount

    # 获取账户余额
    def get_balance(self):
        return self.__balance


# 存款
def deposit(account):
    print('当前余额：', account.get_balance())
    amount = float(input('请输入存款金额：'))
    account.deposit(amount)
    print('存款成功！\n当前余额：', account.get_balance())


# 取款
def withdraw(account):
    print('当前余额：', account.get_balance())
    amount = float(input('请输入取款金额：'))
    if account.get_balance() < amount + MIN_BALANCE:
        print('余额不足！取款后余额应不少于', MIN_BALANCE)
        return
    account.withdraw(amount)
    print('取款成功！\n当前余额：', account.get_balance())


# 测试
user = BankAccount(500)
while True:
    print()
    print('--银行账户管理--')
    print('  1 存款')
    print('  2 取款')
    print('  0 退出')
    choice = input('请选择业务：')
    print()

    match choice:
        case '1':
            deposit(user)
        case '2':
            withdraw(user)
        case '0':
            exit()
