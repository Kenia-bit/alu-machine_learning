#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# Plotting x ↦ y1 with dashed red line
plt.plot(x, y1, linestyle='--', color='red', label='C-14')
# Plotting x ↦ y2 with solid green line
plt.plot(x, y2, linestyle='-', color='green', label='Ra-226')
plt.xlabel('Time (years)')  # Labeling the x-axis
plt.ylabel('Fraction Remaining')  # Labeling the y-axis
plt.title("Exponential Decay of Radioactive Elements")  # Adding a title
plt.xlim(0, 20000)  # Setting the x-axis range
plt.ylim(0, 1)  # Setting the y-axis range
plt.legend(loc='upper right')  # Adding a legend in the upper right corner
plt.show()

