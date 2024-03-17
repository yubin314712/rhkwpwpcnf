#조건 1
def get_fadius(prompt):
    r= int(input(prompt))
    return r


#조건 2

def get_cirle_area():
    r =int(input('넓이를 구하고자 하는 원의 반지름은?'))
    
    cul= 3.14*r*r
    print('원의 넓이는',cul)
    return cul

    
print('시작')
get_cirle_area()
print('종료')

