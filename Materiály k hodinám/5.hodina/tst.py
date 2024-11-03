import matplotlib.pyplot as plt
from random import randint

# make data:
x = [1,2,3,4,5]
y = [4.8, 5.5, 3.5, 4.6, 6.5]


# plot
fig, ax = plt.subplots()

ax.bar(x2, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 5), xticks=[1,2,3,4,5],
       ylim=(0, 5), yticks=[1,2,3,4,5])

plt.show()