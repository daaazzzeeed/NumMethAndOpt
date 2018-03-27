import math as m

x0 = -1
y0 = 1

a = x0
b = 1
n = 10
h = (b-a)/n

y = list()

print('n = ' + str(n)+'\nh = ' + str(h))

x = x0
y = y0

def func(x_,y_):
    return m.sqrt(y_-m.pow(x_,2))


for i in range(1, n+1):
    y = y + h*func(x, y)
    x = x + h
    print('x = ' + str(round(x, 4)) + '\ny = ' + str(round(y, 4)) + '\n')
