class Point:
    def __init__(self, x0,y0):
        self.x0 = x0
        self.y0 = y0

    def show(self):
        print(self.x0, self.y0)

    def move(self, moveX, moveY):
        self.x1 = self.x0 + moveX
        self.y1 = self.y0 + moveY
        print(self.x1, self.y1)

    def dist(self):
        d = ((self.x1-self.x0)**2 + (self.y1-self.y0)**2)**0.5
        print(d)

x0 = int(input())
y0 = int(input())
moveX = int(input())
moveY = int(input())

myPoint = Point(x0, y0)
myPoint.show()
myPoint.move(moveX,moveY)
myPoint.dist()
