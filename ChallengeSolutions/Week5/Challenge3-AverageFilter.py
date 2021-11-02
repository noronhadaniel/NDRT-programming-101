import numpy as np

x = [1,2,4,8,16,32,64]
x = np.array(x)
window = 3
print(f"Unfiltered: {x}")
print(f"Average Filtered: {np.convolve(x,np.ones(window),'valid') / window}")
