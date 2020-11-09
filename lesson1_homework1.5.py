# Пользователь вводит значения выручки и издержек фирмы.
# Определить, с каким финансовым результатом работает фирма -
# прибыль - выручка больше издержек или
# убыток - издержки больше выручки.
# Вывести на экран соотв. сообщение.
# Если фирма отработала с прибылью, вычислить рентабельность выручки (соотношение прибыли к выручке).
# Запросить численность сотрудников фирмы.
# Определить прибыль фирмы в расчете на одного сотрудника.

profit = float(input('Введите выручку фирмы '))
costs = float(input('Введите издержки фирмы '))
if profit > costs:
    print(f'Фирма работает с прибылью. Рентабельность выручки составляет {profit / costs:.2f}')  # до 2х знаков
    workers = int(input('Введите численность сотрудников фирмы '))
    print(f'Прибыль в расчете на одного сотрудника составляет {profit / workers:.2f}')
elif profit == costs:
    print('Прибыль фирма равна убыткам')
else:
    print('Фирма работает в убыток')
