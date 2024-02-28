import matplotlib.pyplot as plt
import numpy as np

y = np.array([34, 56, 43, 89, 13])
mylables = ["Dbms", "python", "java", "c", "Daa"]
plt.pie(y, labels=mylables, startangle=90)
plt.show()