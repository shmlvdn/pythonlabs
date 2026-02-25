#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
print('Лампы -', lamps_cost, 'руб')

stol1 = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
stol2 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
st = stol1 + stol2
print('Столы -', st, 'руб')

sofa1 = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
sofa2 = store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
sf = sofa1 + sofa2
print('Диваны -', sf, 'руб')

stul1 = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
stul2 = store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']
stul3 = store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
sl = stul1 + stul2 + stul3
print('Стулья -', sl, 'руб')


# Вывести стоимость каждого вида товара на складе:

a = store[goods['Лампа']][0]['price']
print('Лампа -', a, 'руб')

b = store[goods['Стол']][0]['price']
b1 = store[goods['Стол']][1]['price']
print('Стол 1 -', b, 'руб')
print('Стол 2 -', b1, 'руб')


c = store[goods['Диван']][0]['price']
c1 = store[goods['Диван']][1]['price']
print('Диван 1 -', c, 'руб')
print('Диван 2 -', c1, 'руб')

d = store[goods['Стул']][0]['price']
d1 = store[goods['Стул']][1]['price']
d2 = store[goods['Стул']][2]['price']
print('Стул 1 -', d, 'руб')
print('Стул 2 -', d1, 'руб')
print('Стул 3 -', d2, 'руб')


# один раз распечать сколько всего столов и их общая стоимость

stoly1 = store[goods['Стол']][0]['quantity']
stoly2 = store[goods['Стол']][1]['quantity']
stoly3 = stoly1 + stoly2
st1 = store[goods['Стол']][0]['price'] * store[goods['Стол']][0]['quantity']
st2 = store[goods['Стол']][1]['price'] * store[goods['Стол']][1]['quantity']
st3 = st1 + st2
print('Стол:', stoly3, 'шт,', st3, 'руб')

# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе

stulia1 = store[goods['Стул']][0]['quantity']
stulia2 = store[goods['Стул']][1]['quantity']
stulia3 = store[goods['Стул']][2]['quantity']
stulia4 = stulia1 + stulia2 + stulia3
sl1 = store[goods['Стул']][0]['price'] * store[goods['Стул']][0]['quantity']
sl2 = store[goods['Стул']][1]['price'] * store[goods['Стул']][1]['quantity']
sl3 = store[goods['Стул']][2]['price'] * store[goods['Стул']][2]['quantity']
sl4= sl1 + sl2 + sl3
print('Стул:', stulia4, 'шт,', sl4, 'руб')

dv = store[goods['Диван']][0]['quantity']
dv1 = store[goods['Диван']][1]['quantity']
dv2 = dv + dv1
dv3 = store[goods['Диван']][0]['price'] * store[goods['Диван']][0]['quantity']
dv4 = store[goods['Диван']][1]['price'] * store[goods['Диван']][1]['quantity']
dv5 = dv3 + dv4
print('Диван:', dv2, 'шт,', dv5, 'руб')

lamp = store[goods['Лампа']][0]['quantity']
lamp1 = store[goods['Лампа']][0]['price'] * store[goods['Лампа']][0]['quantity']
print('Лампа:', lamp, 'шт,', lamp1, 'руб')

# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
