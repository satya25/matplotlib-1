from matplotlib import pyplot as plt
from matplotlib import style

# x   =   [11, 22, 33, 44, 55, 66, 77]
# y   =   [10, 20, 30, 40, 50, 60, 70]

# #x1  =   [31, 21, 41, 34, 45, 67, 45]
# x1   =   [11, 22, 33, 44, 55, 66, 77]
# y1  =   [22, 33, 44, 21, 34, 55, 25]

x   =   [5,8,10, 11, 7]
y   =   [12,16,6, 10, 9]

x2  =   [5,8,10, 11, 7]
y2  =   [6,15,7, 11, 9]

plt.bar(x, y, align='center')

plt.bar(x2, y2, color='g', align='center')
 
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()