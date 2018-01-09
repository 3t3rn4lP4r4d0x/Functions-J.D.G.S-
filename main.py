import matplotlib.pyplot as plt
plt.axis([0,10,0,10])
plt.plot([0,1,2,3,4], [0,2,4,8,10], "-ro")
plt.ylabel('Grafic de funcions')
plt.savefig('graph.jpg')
