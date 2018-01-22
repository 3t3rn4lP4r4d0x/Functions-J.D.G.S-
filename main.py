import matplotlib.pyplot as plt
#esto deja que puedas poner los maximos  minimos valors del axis de valores

xmin=int(input("valor minim de x?"))
xmax=int(input("valor maxim de x?"))
func = input("funcio")
xarray = []
yarray = []
x = xmin
while x <= xmax:
  xarray.append(x)
  y = eval(func)
#  y = x**2 - 3*x
  print ("x = {0:5.2f}  y = {1:5.2f}".format(x,y))
  yarray.append(y)
  x = x + 0.1
plt.plot(xarray, yarray, "-ro")
plt.ylabel('Grafic de funcions')
plt.savefig('graph.jpg')
def cutx ():
  if xmin > y  or y > xmax:
    print ('Aquesta funció talla per eix x.')
  else:
    print ('Aquesta funció no talla per eix x.')
     
    
    
    
cutx ()
