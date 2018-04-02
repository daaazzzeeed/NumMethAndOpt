import math

x = -1; b = 0; h = (b-x)/10
y = list(0 for i in range(3))
y[2] = [ y[2] ]

f = lambda x, y: -math.sqrt(y) - 2*x
print('Step\txi\tEuler\tRunge_Kutta\tAdams')
print('{i}\t{xi:.1f}\t{yi[0]:.4f}\t\t{yi[1]:.4f}\t\t{yi[2][0]:.4f}'.format(xi=x, yi=y, i=0))

for i in range(0, int((b-x)/h)):
    #Euler
    y[0] = y[0] + h*f(x,y[0])
    #Runge-Kutta
    K1 = f(x,y[1])
    K2 = f(x+h/2,y[1]+h*K1/2)
    K3 = f(x+h/2, y[1]+h*K2/2)
    K4 = f(x+h,y[1]+h*K3)

    y[1] = y[1] + h*(K1 + 2*K2 + 2*K3 + K4)/6
    #Adams
    if i<3:
        y[2].append(y[1])
        print('{i}\t{xi:.1f}\t{yi[0]:.4f}\t\t{yi[1]:.4f}\t\t{Adams:.4f}'.format(xi=x+h,yi=y,Adams=y[2][-1],i=i+1))
    else:
        df = f(x,y[2][-1])-f(x,y[2][-2])
        d2f = f(x,y[2][-1])-2*f(x,y[2][-2])+f(x,y[2][-3])
        d3f = f(x,y[2][-1])-2*f(x,y[2][-2])-2*f(x,y[2][-3])-f(x,y[2][-4])
        y[2].append(y[2][-1] + h*f(x,y[2][-1]) + (1/2)*(h**2)*df + (5/12)*(h**3)*d2f + (3/8)*(h**4)*d3f)
        y[2].pop(0)
        print('{i}\t{xi:.1f}\t{yi[0]:.4f}\t\t{yi[1]:.4f}\t\t{yi[2][3]:.4f}'.format(xi=x+h,yi=y,i = i+1))
    x = x + h


