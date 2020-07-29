from matplotlib import pyplot as plt
from matplotlib import style
 

x = [10, 15, 5, 8, 10]
y = [16, 8, 12, 16, 6]

x1 = [20, 30, 16, 19, 31]
y1 = [30, 20, 6, 25, 17]
 
x2 = [10, 21, 6, 9, 11]
y2 = [11, 14, 6, 15, 7]

x3 = [8, 10, 21, 6, 9, 11]
y3 = [11, 25, 16, 6, 15, 7]

x4 = [10, 15, 20, 25, 30, 35]
y4 = [10, 15, 20, 25, 30, 35]

## Additional input
x5 = [101, 65, 60, 45, 40, 45]
y5 = [110, 65, 80, 55, 40, 25]



# can plot specifically, after just showing the defaults:
plt.plot(x, y, linewidth=5)
plt.plot(x1, y1, linewidth=7)
plt.plot(x2, y2, linewidth=9)
plt.plot(x3, y3, linewidth=6)
plt.plot(x4, y4, linewidth=3)

## Additional graph
plt.plot(x5, y5, linewidth=1)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show() 