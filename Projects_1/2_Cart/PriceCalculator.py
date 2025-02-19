# 计算总价函数
def calculator(prices, quantities):
    price_sum = 0.0
    i = 0
    while i < len(prices):
        price_sum += prices[i] * quantities[i]
        i += 1

    if price_sum >= 500:
        print('原价：', price_sum)
        print('折扣：-10%')
        price_sum *= 0.9

    print('总价：', round(price_sum, 2))


def print_cart(prices, quantities):
    print('----购物车----')
    print('序号\t单价\t数量')

    i = 0
    while i < len(prices):
        print(i+1, '\t', prices[i], '\t', quantities[i])
        i += 1


# 测试1（总价不超过500）
prices_1 = [2.0, 5.0, 2.4, 8.1, 3.4]
quantities_1 = [5, 6, 10, 4, 3]
print_cart(prices_1, quantities_1)
calculator(prices_1, quantities_1)

print()

# 测试2（总价超过500，打九折）
prices_2 = [20.3, 53.0, 24.8, 66.1, 95.6, 77.3]
quantities_2 = [5, 3, 4, 2, 1, 3]
print_cart(prices_2, quantities_2)
calculator(prices_2, quantities_2)
