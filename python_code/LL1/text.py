import pysnooper
import numpy as np
@pysnooper.snoop()
def multi_matmul(times):
    x = np.random.rand(2,2)
    w = np.random.rand(2,2)
    for i in range(times):
        x = np.matmul(x,w)
    return x

multi_matmul(3)