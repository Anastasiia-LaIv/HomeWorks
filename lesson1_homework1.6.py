# Спортсмен занимается пробежками.
# В 1й день его рез-т a км.
# Каждый день рез-т увеличивается на 10 % относительно предыдущего.
# Определить номер дня, на к-рый общий рез-т спортсмена сост. не менее b км.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число - номер дня.

a = int(input('Введите результат пробежки первого дня, в км: '))
b = int(input('Введите желаемый результат, в км: '))
i = 1
while a < b:
    a *= 1.1
    i += 1
print('Вы достигнете желаемого результата на', i, 'день')