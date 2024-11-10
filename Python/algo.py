#list_x = []
#list_y = []
#
#def pega_val(quant):
#    for i in range(0, quant):
#        nx = float(input(f"Valor X{i}: "))
#        ny = float(input(f"Valor Y{i}: "))
#        list_x.insert(i, nx)
#        list_y.insert(i, ny)    
#
#def mostra_list():
#    for i in range(0, len(list_x)):
#            print(f"P{i}({list_x[i], list_y[i]})")
#
#def prox(val_x):
#        l1 = ( (val_x - list_x[1])/(list_x[0] - list_x[1]) * (val_x - list_x[2])/(list_x[0] - list_x[2]) )
#        l2 = ( (val_x - list_x[0])/(list_x[1] - list_x[0]) * (val_x - list_x[2])/(list_x[1] - list_x[2]) )
#        l3 = ( (val_x - list_x[0])/(list_x[2] - list_x[0]) * (val_x - list_x[1])/(list_x[2] - list_x[1]) )
#        px = ( (list_y[0] * l1) + (list_y[1] * l2) + (list_y[2] * l3) )
#        print(f"Para x = {val_x}, temos y = {px}")
#        
#pega_val(3)
#prox(2)

import numpy as np
import matplotlib.pyplot as plt

def interpLagrange(xp,x,y,grau):
  yp = 0
  for k in range(0,n+1):
    p = 1
    for j in range(0,n+1):
      if k != j:
        p = p*(xp - x[j])/(x[k] - x[j])

    yp = yp + p * y[k]

  return yp

x = [-1, 0, 2]
y = [4, 1, -1]

n  = 2
xp = 1.5
yp = interpLagrange(xp,x,y,n)
t  = np.arange(-1.0,2.0,0.1)
yt = []
for i in t:
  yt.append(interpLagrange(i,x,y,n))

plt.plot(t,yt,'b-')
plt.plot(x,y,'ro')
plt.plot(xp,yp,'g*')
plt.show()

