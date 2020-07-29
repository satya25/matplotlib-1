from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5,8,10, 11, 12]
y = [12,16,6, 7, 8]

x2 = [6,9,11, 9, 11]
y2 = [6,15,7, 10, 12]

plt.scatter(x, y)#, align='center')

plt.scatter(x2, y2, color='g')#, align='center')
 
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()