import matplotlib.pyplot as plt
import csv

x = []
y = []

"""x1 = ['January','February','March','April','May','June','July','August','September','October','November','December']
y1 = [20,5,28,29,5,10,56,5,45,23,99,110]
"""
with open('monthly_leave_data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        y.append(str(row[1]))

plt.plot(x,y, label='All Employee Leave Taken History!')
plt.xlabel('X-axis: Month')
plt.ylabel('Y-axis: Number Of Leave Taken')
plt.title('Amtron Employee Monthly Leave Report Data\nDesigned By Chandrasekhar Yadav')
plt.legend()
plt.grid()
plt.show()