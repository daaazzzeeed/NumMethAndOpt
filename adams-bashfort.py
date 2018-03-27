import math as m

x0 = 0
y0 = m.e

a = x0
b = 1
n = 10
h = (b-a)/n
x = x0
y = y0
x1 = b

y = list(m.e for i in range(3))
y[2] = [ y[2] ]


def f(x_, y_):
    return -m.log(y_ - x_, m.e)


def k1(x_, y_):
    return f(x_, y_)


def k2( x_, y_, h):
    return f(x_ + 0.5 * h, y_ + 0.5 * h * k1(x_, y_))


def k3(x_, y_, h):
    return f(x_ + 0.5 * h, y_ + h * 0.5 * k2(x_, y_, h))


def k4(x_, y_, h):
    return f(x_ + h, y_ + h * k3(x_, y_, h))


def M(x_, y_, h):
    return (1 / 6) * h * (k1(x_, y_) + 2 * k2(x_, y_, h) + 2 * k3(x_, y_, h) + k4(x_, y_, h))


for i in range(0, int((b-x)/h)):
    K1 = k1(x, y[1])
    K2 = k2(x, y[1])
    K3 = k3(x, y[1])
    K4 = k4(x, y[1])

    y[1] = y[1] + M(x,y[1],h)

    if i < 3:
        y[2].append(y[1])
        print("{i}\t{xi:.1f}\t{yi[0]:.4f}\t\t{yi[1]:.4f}\t\t{Adams:.4f}".format(xi=x+h,yi = y,Adams = y[2][-1],i=i+1))

