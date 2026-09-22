#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

plt.scatter(x, y, color='magenta')  # Plotting the data as magenta points
plt.xlabel('Height (in)')  # Labeling the x-axis
plt.ylabel('Weight (lbs)')  # Labeling the y-axis
plt.title("Men's Height vs Weight")  # Adding a title
plt.show()

