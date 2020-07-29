### Importing pyplot

from matplotlib import pyplot as plt

##  Plotting starts

plt.title('Chart Title')
plt.ylabel('This is Y-Axis Title')
plt.xlabel('This is X-Axis Title')

plt.plot([1, 2, 3, 4, 5, 1, 2, 3, 4, 5 ], [4, 6, 8, 10, 12, 16, 11, 14, 9, 4])

### Let's display what we plotted.

plt.show()