# -*- coding: utf-8 -*-
"""hw6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jX-ICcrwtylIgL5CP-TibkPFrXIAPmN0
"""

def gugudan(x,n):
  print(f'{x} x {n} = {x*n:2d}\t',end='')

def printgugu1():
  for b in range(1,10):
    for a in range(2,6):
      gugudan(a,b)
    print()

def printgugu2():
  for b in range(1,10):
    for a in range(6,10):
      gugudan(a,b)
    print()

printgugu1()
print()
printgugu2()