import matplotlib.pyplot as plt
#esto deja que puedas poner los maximos  minimos valors del axis de valores
xmin=eval(input("valor minim de x?"))
xmax=eval(input("valor maxim de x?"))
ymin=eval(input("valor minim de y?"))
ymax=eval(input("valor maxim de y?"))
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([0,1,2,3,4], [0,2,4,8,10], "-ro")
plt.ylabel('Grafic de funcions')
plt.savefig('graph.jpg')
