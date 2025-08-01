# With matplotlib, you can create a bunch of different plots in Python. The most basic plot is the line plot. A general recipe is given here.

# import matplotlib.pyplot as plt
# plt.plot(x,y)
# plt.show()

# Print the last item from year and pop
print(year[-1])
print(pop[-1])


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()