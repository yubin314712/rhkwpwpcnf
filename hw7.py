# -*- coding: utf-8 -*-
"""hw7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZffTDLZte5IUBnhqQAUHIi2ufUuzbvyv
"""

shopping_bag = {}


print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':
        break
    itnum = int(input('수량은? '))
    shopping_bag[item] = itnum
    print (f'장바구니에 {item} {itnum}개가 담겼습니다. \n')
print(f'\n>>> 장바구니 보기: {shopping_bag}')

print('\n[검색]')
ask= input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{ask}은(는) {shopping_bag[ask]}개 담겨 있습니다.')