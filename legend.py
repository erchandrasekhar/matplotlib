import matplotlib.pyplot as plt
x = [1,2,3]
y = [4,5,6]

x1 = [9,8,7]
y1 = [6,5,4]

plt.plot(x,y,label='First Line')
plt.plot(x1,y1,label='Second Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('In this tutorial legend demonstration has been completed')
plt.legend()
plt.show()