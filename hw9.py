class Rectangle:
    class Point:
        def __init__(self, x=0, y=0):
            self.__x = x
            self.__y = y

        def show(self):
            print(f'({self.__x}, {self.__y})')

        def set(self, x, y):
            self.__x = x
            self.__y = y

        def get(self):
            return (self.__x, self.__y)

    def __init__(self, x1, y1, x2, y2):
        self.lt = self.Point(x1, y1)
        self.rb = self.Point(x2, y2)




    def show(self):
        print(f'좌측상단 꼭지점이 {self.lt.get()}이고 우측 하단 꼭지점이 {self.rb.get()}인 사각형입니다.')

    def getWidth(self):
        return self.rb.get()[0] - self.lt.get()[0]

    def getHeight(self):
        return self.rb.get()[1] - self.lt.get()[1]

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return self.getWidth() *2 +self.getHeight() *2


r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')