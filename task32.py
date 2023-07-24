'''Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)'''

import random

data = [random.randint(-100, 100) for i in range(10)]
# Раскоментируйте строку ниже, что бы отображать созданый список
print(data)
while True:
    minimum = int(input('Введите минимальную границу диапозона: '))
    maximum = int(input('Введите максимальную границу диапозона: '))
    if minimum > maximum:
        print('Минимальная граница больше максимальной. Хотите поменять границы местами? (да/нет)')
        quesion = input(
            'да - поменять границы местами, нет - задать новые границы: ').lower()
        if quesion == 'да':
            minimum, maximum = maximum, minimum
            break
    else:
        break
res = list(filter(lambda i: i <= maximum and i >= minimum, data))
res1 = []
for i in range(len(data)):
    if data[i] in res:
        res1.append(i)
print(res1)
