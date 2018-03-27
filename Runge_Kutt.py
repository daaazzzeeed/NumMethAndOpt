import math as m

class RK:
    def func(self, x_,y_):
        return -m.log(y_-x_, m.e)

    def k1(self,x_,y_):
        return self.func(x_,y_)

    def k2(self, x_,y_,h):
        return self.func(x_+0.5*h,y_+0.5*h*self.k1(x_,y_))

    def k3(self, x_,y_,h):
        return self.func(x_+0.5*h, y_+h*0.5*self.k2(x_,y_,h))

    def k4(self, x_,y_,h):
        return self.func(x_+h, y_+h*self.k3(x_,y_,h))

    def M(self,x_,y_,h):
        return y_+(1/6)*h*(self.k1(x_,y_)+2*self.k2(x_,y_,h)+2*self.k3(x_,y_,h)+self.k4(x_,y_,h))

    x0 = 0
    y0 = m.e

    a = x0
    b = 1
    n = 10
    h = (b-a)/n

    x = x0
    y = y0
    x1 = b
    L = 0


rk = RK()

while rk.L == 0:
    if rk.x+rk.h > rk.x1:
        rk.h = rk.x1-rk.h
        rk.L = 1
    else:
        rk.y = rk.M(rk.x,rk.y, rk.h)
        rk.x = rk.x + rk.h
        print('x = ' + str(rk.x) + '\ny = ' + str(rk.y))
