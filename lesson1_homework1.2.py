# Пользователь вводит время в секундах.
# Перевести время в часы, минуты и секунды и вывести в формате чч:мм:сс .
# Использовать форматирование строк.

time = int(input('Введите время в секундах: '))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
seconds = time % 60

print(f'{hours:02}:{minutes:02}:{seconds:02}')