

def getsale(prompt):
  res = int(input(prompt))
  return res



tsale = getsale('할인율은?')



def get_fixed_price(sprice):
  oprice = int(sprice/(1-(tsale/100)))
  return oprice




sprice1 = int(input('A 상품의 할인된 가격은?'))

sprice2 = int(input('B 상품의 할인된 가격은?'))


op1 =get_fixed_price(sprice1)
op2 =get_fixed_price(sprice2)


print('A 상품의 정가는',op1,'원')
print('B 상품의 정가는',op2,'원')
