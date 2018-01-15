import matplotlib.pyplot as plt
#esto deja que puedas poner los maximos  minimos valors del axis de valores
xmin=int(input("valor minim de x?"))
xmax=int(input("valor maxim de x?"))
#plt.axis([xmin,xmax,ymin,ymax]) no hace falta plt.axis ya que te lo hace solo con lo de plot.
plt.plot([0,1,2,3,4], [0,2,4,8,10], "-ro")
plt.ylabel('Grafic de funcions')
plt.savefig('graph.jpg')
