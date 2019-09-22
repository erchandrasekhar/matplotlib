import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,100)
y = 2*x + 1
y1 = 2*x + 2
y2 = 2*x + 3
plt.title('Straight Lines Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.plot(x,y,label='y=2x+1')
plt.plot(x,y1,label='y=2x+2')
plt.plot(x,y2,label='y=2x+3')
plt.legend()
plt.grid()
plt.show()
