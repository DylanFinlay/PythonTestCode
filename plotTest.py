# Practice file for learning matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 2, 4, 8])
y = np.array([0, 5, 1, 10])

xTwo = np.array([1, 8, 12])
yTwo = np.array([3, 5, 10])

#plt.plot(x, y, 'o--r')

plt.grid()

#Plot one
plt.subplot(1, 2, 1)
plt.title("Dataset practice")
plt.xlabel("Independent")
plt.ylabel("Dependent")
plt.plot(x,y)

#Plot two
plt.subplot(1,2,2)
plt.title("Dataset practice")
plt.xlabel("Independent")
plt.plot(xTwo,yTwo)

# Scatter plot
# plt.scatter(x,y)

# Bar graph
# xThree = ["APPLES", "BANANAS"]
# yThree = [400, 350]
# plt.bar(xThree, yThree)

# Pie chart
# y_val = np.array([35, 25, 25, 15])
# myLabels = ["Apples", "Bananas", "Cherries", "Dates"]
# plt.pie(y_val, labels = myLabels)
# plt.legend(title = "Four Fruits:")

plt.suptitle("Practice")

plt.show()
