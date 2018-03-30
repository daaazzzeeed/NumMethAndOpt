import math as m


class RK:
    def func(self, x_, y_):
        return -m.log(y_ - x_, m.e)

    def k1(self, x_, y_):
        return self.func(x_, y_)

    def k2(self, x_, y_, h):
        return self.func(x_ + 0.5 * h, y_ + 0.5 * h * self.k1(x_, y_))

    def k3(self, x_, y_, h):
        return self.func(x_ + 0.5 * h, y_ + h * 0.5 * self.k2(x_, y_, h))

    def k4(self, x_, y_, h):
        return self.func(x_ + h, y_ + h * self.k3(x_, y_, h))

    def M(self, x_, y_, h):
        return y_ + (1 / 6) * h * (
                    self.k1(x_, y_) + 2 * self.k2(x_, y_, h) + 2 * self.k3(x_, y_, h) + self.k4(x_, y_, h))

    x0 = 0
    y0 = m.e

    a = x0
    b = 1
    n = 10
    h = (b - a) / n

    x = x0
    y = y0
    x1 = b
    L = 0


rk = RK()
i = 0
values = list()
x_val = list()
y_val = list()
y_final = list()
y_to_print = list()
y_val.append(rk.y0)
x_val.append(rk.x0)

for i in range(0, 10):
    if i < 3:
            rk.y = rk.M(rk.x, rk.y, rk.h)
            rk.x = rk.x + rk.h
            x_val.append(rk.x)
            y_val.append(rk.y)
            y_final = y_val
            y_to_print = y_final
           # print(y_final)

    else:
        x_val.append(rk.x)
        df = rk.func(x_val[3], y_final[3])-rk.func(x_val[2], y_final[2])
        d2f = rk.func(x_val[3], y_final[3])-2*rk.func(x_val[2], y_final[2])+rk.func(x_val[1], y_final[1])
        d3f = rk.func(x_val[3], y_final[3])-3*rk.func(x_val[2], y_final[2]) - 3*rk.func(x_val[1], y_final[1])-rk.func(x_val[0],y_val[0])
        yip1 = y_final[3] + rk.h*rk.func(x_val[3],y_final[3])+rk.h*rk.h*0.5*df+5*(rk.h*rk.h*rk.h/12)*d2f+3*(rk.h*rk.h*rk.h*rk.h/8)*d3f
        y_final.append(yip1)
        y_to_print.append(yip1)
        y_final = y_final[1:]
        x_val = x_val[1:]
       # print(y_to_print)
    rk.x = rk.x + rk.h

print(y_to_print) # len() == 12 ????????

for i in range(0,len(y_to_print)):
    print('i = ' + str(i) + '\ty = '+str(y_to_print[i]))   # wrong output values
