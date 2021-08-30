import numpy as np
from numba import jit, prange
from image_creation import *
from matplotlib import pyplot as plt
import matplotlib.colors as mcolors

@jit
def lyapunov(string, xbound, ybound, maxiter=100, width=3, height=3, dpi=100, transpose=False):

    """
        returns a Lyupanov fractal according to the proved string (e.g. 'ABAA')
    """

    L = len(string)

    xmin,xmax = [float(xbound[0]),float(xbound[1])]
    ymin,ymax = [float(ybound[0]),float(ybound[1])]
    nx = width*dpi
    ny = height*dpi

    xvals  = np.array([xmin + i*(xmax - xmin)/(nx) for i in range(nx)], dtype=np.float64)
    yvals  = np.array([ymin + i*(ymax - ymin)/(ny) for i in range(ny)], dtype=np.float64)

    lattice = np.zeros((int(nx), int(ny)), dtype=np.float64)

    for i in prange(len(xvals)):
        for j in prange(len(yvals)):

            count = 0
            x = 0.5
            lamd = 0.0

            xv = xvals[j]
            yv = xvals[i]

            for n in range(maxiter):

                S = string[count%L]
                if S == 'A':
                    rn = xv
                else:
                    rn = yv
                count += 1

                x = (rn*x)*(1-x)
                lamd += np.log(np.abs(rn*(1-(2*x))))
                
            lattice[i,j] += lamd
            lamd /= maxiter

    if transpose:
        lattice = lattice.T

    return (lattice, width, height, dpi)

if __name__ == '__main__':

    colors0 = np.array(plt.cm.YlGnBu_r(np.linspace(0, 1, 1000)))
    colors1 = np.array(plt.cm.YlGnBu_r(np.linspace(0, 1, 1000)))    
    colors = np.vstack((colors1, colors0))
    mymap = mcolors.LinearSegmentedColormap.from_list('my_colormap', colors)

    string =  'AAABA'
    xB = (2.60, 4.0)
    yB = (2.45, 4.0)

    im = lyapunov(string, xB, yB, maxiter=100, dpi=300, width=4, height=3)
    image(im, gamma=3.0, vert_exag=10000.0, cmap=mymap)    
    
