# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10za8pDX4ijJDMPzFw76s3uN8LXzTM4X6
"""

def get_integer(prompt) :
  res = int(input(prompt))
  return res;

def get_integer1(prompt) :
  res = int(input(prompt))
  return res;


def exchange(amount):
  print('잔돈:', amount, '원')

  n500= amount // 500
  amount %= 500

  n100= amount // 100
  amount %= 100

  n50= amount // 50
  amount %= 50

  n10= amount // 10


  print('> 500원권', n500, '개')
  print('> 100원권', n100, '개')
  print('> 50원권', n50, '개')
  print('> 10원권', n10, '개')


total_cost = get_integer('구매한 물건의 총구매 금액은?')

payment = get_integer1('고객으로 부터 지불받은 금액은?')

amount = payment - total_cost

exchange(amount)



