# !---   Don't Touch   ---!
import numpy as np
import matplotlib.pyplot as plt
import math as m

def calcGain(y):
	abs_y = np.absolute(y)
	answer = 20 * np.log10(abs_y)
	return answer
# !---   Don't Touch End   ---!

#You can decide the range of valuable "s"
#np.arange(start, end, step)
original_s = np.arange(10, 10000, 10, dtype=complex)
original_s = original_s / 1000

# !---   Don't Touch   ---!
s = original_s * complex(0, 1)
# !---   Don't Touch End   ---!

#You can define Transfer Function: tf
#For example, if you wanna make First-order System,
#tf = 1 / ( T * s + 1 )
# !--- Transfer Function Definition Zone   ---!

# !--- Transfer Function Definition Zone End   ---!

# !---   Don't Touch   ---!
gain = calcGain(tf)

plt.xscale("log")
plt.plot(original_s, gain)
plt.show()
# !---   Don't Touch End   ---!


