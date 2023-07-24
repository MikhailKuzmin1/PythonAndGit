'''Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры.
Каждое число вводится с новой строки.
'''

first_element = int(input('Введите первый элемент прогрессии: '))
step = int(input('Введите разность прогрессии: '))
count_element = int(input('Введите количество элементов в прогрессии: '))
res = [first_element]
counter = 1
while counter < count_element:
    res.append(res[-1] + step)
    counter += 1
print(*res)
