# Пользователь вводит целое положительное число
# Найти самую большую цифру в числе (исп. while + арифм.операции)

n = int(input('Введите целое положительное число: '))
max_n = n % 10  # (Для определения максимальной цифры логично использовать остаток от деления на 10)
while n >= 1:
    n = n // 10
    if n % 10 > max_n:
        max_n = n % 10
    if n > 9:
        continue
else:
    print('Максимальная цифра в Вашем числе ', max_n)



