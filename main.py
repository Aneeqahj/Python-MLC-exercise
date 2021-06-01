# Challenge 1

from numpy import *
import numpy as np
import matplotlib.pyplot as plt

numbers = np.arange(0, 20)
print(numbers)

mean = np.mean(numbers)
print(mean)

std = np.std(numbers)
print(std)

variance = np.var(numbers)
print(variance)

# Challenge 2

bins = [0, 1, 2, 3, 4]
nums = [0.5, 0.7, 1., 1.2, 1.3, 2.1]

print("nums: {}".format(nums))
print("bins: {}".format(bins))
print("Result: {}".format(histogram(nums, bins)))

plt.title("Histogram of nums against bins")
plt.xlabel("nums")
plt.ylabel("bins")
plt.hist(nums, bins)
plt.show()