import math as m


def func(x_, y_):
    return -(m.log(y_-x_, m.e))

x0 = 0
y0 = m.e

a = x0
b = 1
n = 10
h = (b-a)/n

x = x0
y = y0

for i in range(1,n+1):
    y = y + h*func(x,y)
    x = x + h
    print('x = ' + str(x) + '\ny = ' + str(y) + '\n')