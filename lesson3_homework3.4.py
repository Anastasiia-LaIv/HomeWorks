# Программа принимает действительное положительное число x
# и целое отрицательное число y. Необходимо выполнить возведение
# числа x в степень y. Задание необходимо реализовать в виде функции
# my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.

#1
def my_func(x,y):
    try:
        ans = x ** y
    except TypeError:
        return 'Enter float'
    return ans

print(my_func(2, -2))

#2
def my_func(x,y):
    try:
        x,y = float(x), int(y)
        res = x
        for i in range(abs(y) - 1):
            res *= x
        return 1 / res
    except ValueError:
        return 'Check value'

