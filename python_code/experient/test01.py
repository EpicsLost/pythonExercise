import math
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111)
    u = np.linspace(0,5,200)
    v = np.linspace(0, 4, 1000)
    x,y = np.meshgrid(u,v)
    z = np.log(np.exp(x)+np.exp(y))
    ax.contourf(x,y,z,50)
    plt.show()