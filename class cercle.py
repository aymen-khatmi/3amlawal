import math

class cercle:
    def __init__(self,r,a,b):
        self.r=r
        self.a=a
        self.b=b
    def surface(self):
        return math.pi*self.r**2
    def premetre(self):
        return 2*math.pi*self.r
    def equation(self,x,y):
        return (x-self.a)**2+(y-self.b)**2-self.r**2
    def test_app(self,x,y):
        if self.equation(x,y) == 0:
            print("le point est appartenance")
        else:
            print("le point n est pas appartenance")
