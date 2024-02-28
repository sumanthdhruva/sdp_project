#Example 5
import matplotlib.pyplot as plt
import numpy as np
regnum = ['101', '102', '103']
categories = ["DBMS", "Python", "OS", "MP"]
values = np.array([
    [35, 25, 25, 15],  # Values for category "DBMS"
    [20, 30, 15, 35],  # Values for category "Python"
    [10, 40, 20, 30],  # Values for category "OS"
])
colors = ['blue', 'green', 'orange', 'red']
# Plot area for each registration number and category
for i, reg in enumerate(regnum):
    plt.fill_between(categories, 0, values[i], label=f'Registration {reg}', color=colors[i], alpha=0.7)
# Add labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Area Plot with Different Colors")
plt.legend()
plt.show()