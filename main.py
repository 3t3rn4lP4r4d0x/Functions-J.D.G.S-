import matplotlib.pyplot as plt
#esto deja que puedas poner los maximos  minimos valors del axis de valores

xmin=int(input("valor minim de x?"))
xmax=int(input("valor maxim de x?"))
func = input("funcio")
ymenzero = False
ymaszero = False

xarray = []
yarray = []
x = xmin

while x <= xmax:
  xarray.append(x)
  y = eval(func)
  if y <= 0 :
    ymenzero = True
  if 0 <= y :
    ymaszero = True
#  y = x**2 - 3*x
  print ("x = {0:5.2f}  y = {1:5.2f}".format(x,y))
  yarray.append(y)
  x = x + 0.1

plt.axhline(0)
plt.axvline(0)
plt.plot(xarray, yarray, "-ro")
plt.ylabel('Grafic de funcions')
plt.savefig('graph.jpg')
def cutx ():
  if ymenzero and ymaszero:
    print ('Aquesta funció talla per eix x.')
  else:
    print ('Aquesta funció no talla per eix x.')
    
    
    
    
cutx ()
