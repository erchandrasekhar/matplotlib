import matplotlib.pyplot as plt
import numpy as np
print("############# First Graph Using matplotlib.pyplot  ##################")
x = [1,2,3]
y = [1,2,6]

x1 = [1,2,3]
y1 = [6,5,4]

plt.plot(x,y)
plt.plot(x1,y1)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('First Graph using mat plot\ncheck out below\nDesigned by Chandrasekhar yadav')
plt.show()
