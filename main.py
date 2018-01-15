import matplotlib.pyplot as plt
#esto deja que puedas poner los maximos  minimos valors del axis de valores
xmin=int(input("valor minim de x?"))
xmax=int(input("valor maxim de x?"))
plt.axis([xmin,xmax])
plt.plot([0,1,2,3,4], [0,2,4,8,10], "-ro")
plt.ylabel('Grafic de funcions')
plt.savefig('graph.jpg')
