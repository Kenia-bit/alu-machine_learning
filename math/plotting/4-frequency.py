#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Generating data for the plots
y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Plotting all graphs in one figure
plt.figure(figsize=(10, 7))

# Plot 1: Line graph
plt.subplot(3, 2, 1)
plt.plot(y0, color='red')
plt.xlabel('X-axis', fontsize='x-small')
plt.ylabel('Y-axis', fontsize='x-small')
plt.title('Plot 1', fontsize='x-small')

# Plot 2: Scatter plot
plt.subplot(3, 2, 2)
plt.scatter(x1, y1, color='magenta')
plt.xlabel('Height (in)', fontsize='x-small')
plt.ylabel('Weight (lbs)', fontsize='x-small')
plt.title("Plot 2", fontsize='x-small')

# Plot 3: Line graph
plt.subplot(3, 2, 3)
plt.plot(x2, y2, color='blue')
plt.xlabel('Time (years)', fontsize='x-small')
plt.ylabel('Fraction Remaining', fontsize='x-small')
plt.title("Plot 3", fontsize='x-small')

# Plot 4: Line graphs (two plots in one)
plt.subplot(3, 2, (4, 5))
plt.plot(x3, y31, linestyle='--', color='red', label='C-14')
plt.plot(x3, y32, linestyle='-', color='green', label='Ra-226')
plt.xlabel('Time (years)', fontsize='x-small')
plt.ylabel('Fraction Remaining', fontsize='x-small')
plt.title("Plot 4", fontsize='x-small')
plt.legend(fontsize='x-small')

# Plot 5: Histogram
plt.subplot(3, 2, 6)
plt.hist(student_grades, bins=10, color='orange')
plt.xlabel('Grades', fontsize='x-small')
plt.ylabel('Frequency', fontsize='x-small')
plt.title("Plot 5", fontsize='x-small')

# Adjust layout and display the figure
plt.tight_layout()
plt.suptitle('All in One', fontsize='large')
plt.show()

