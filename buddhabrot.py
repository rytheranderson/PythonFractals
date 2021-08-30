import numpy as np
from numpy.random import random
import time
from numba import jit
from complex_dynamics import mandelbrot
from image_creation import nebula_image, save_image_array

@jit
def compute_cvals(Ncvals, xbound, ybound, update_func, args=2, width=5, height=5, dpi=100, importance_weight=0.75):

<<<<<<< HEAD
    """
        calculates the values to use for the Buddhabrot image, uses an "energy grid approach" where most of the sampled
        points (the fraction is determined by importance_weight) are on the boundary of the Mandelbrot set.
    """

    xmin,xmax = [float(xbound[0]),float(xbound[1])]
    ymin,ymax = [float(ybound[0]),float(ybound[1])]

    nx = width*dpi
    ny = height*dpi

    xvals  = np.array([xmin + i*(xmax-xmin)/(nx) for i in range(nx)], dtype=np.float32)
    yvals  = np.array([ymin + i*(ymax-ymin)/(ny) for i in range(ny)], dtype=np.float32)
    xboxs = [(xvals[i],xvals[i+1]) for i in range(len(xvals)-1)]
    yboxs = [(yvals[i],yvals[i+1]) for i in range(len(yvals)-1)]
    xboxs = xboxs + [(xboxs[-1][1], xmax)]
    yboxs = yboxs + [(yboxs[-1][1], ymax)]

    NR = int(round(Ncvals * (1-importance_weight)))
    cvals = []

    for k in range(NR):

        c = xmin+(random()*(xmax-xmin)) + 1j*(ymin+(random()*(ymax-ymin)))
        cvals.append(c)

    if importance_weight > 0.0:

        NI = int(round(Ncvals * importance_weight))
        energy_grid = mandelbrot(xbound, ybound, update_func, args=args, width=width, height=height, dpi=dpi, maxiter=1000, horizon=2.5, log_smooth=False)[0]
        energy_grid = (energy_grid/energy_grid.sum()) * NI

        for i in range(nx):
            for j in range(ny):
    
                N = int(round(energy_grid[i,j]))
        
                xlo,xhi = xboxs[i]
                ylo,yhi = yboxs[j]
                cs = xlo+(random(N)*(xhi-xlo)) + 1j*(ylo+(random(N)*(yhi-ylo)))
        
                cvals.extend(list(cs))

=======
    xmin,xmax = [float(xbound[0]),float(xbound[1])]
    ymin,ymax = [float(ybound[0]),float(ybound[1])]

    nx = width*dpi
    ny = height*dpi

    xvals  = np.array([xmin + i*(xmax-xmin)/(nx) for i in range(nx)], dtype=np.float32)
    yvals  = np.array([ymin + i*(ymax-ymin)/(ny) for i in range(ny)], dtype=np.float32)
    xboxs = [(xvals[i],xvals[i+1]) for i in range(len(xvals)-1)]
    yboxs = [(yvals[i],yvals[i+1]) for i in range(len(yvals)-1)]
    xboxs = xboxs + [(xboxs[-1][1], xmax)]
    yboxs = yboxs + [(yboxs[-1][1], ymax)]

    NR = int(round(Ncvals * (1-importance_weight)))
    cvals = []

    for k in range(NR):

        c = xmin+(random()*(xmax-xmin)) + 1j*(ymin+(random()*(ymax-ymin)))
        cvals.append(c)

    if importance_weight > 0.0:

        NI = int(round(Ncvals * importance_weight))
        energy_grid = mandelbrot(xbound, ybound, update_func, args=args, width=width, height=height, dpi=dpi, maxiter=1000, horizon=2.5, log_smooth=False)[0]
        energy_grid = (energy_grid/energy_grid.sum()) * NI

        for i in range(nx):
            for j in range(ny):
    
                N = int(round(energy_grid[i,j]))
        
                xlo,xhi = xboxs[i]
                ylo,yhi = yboxs[j]
                cs = xlo+(random(N)*(xhi-xlo)) + 1j*(ylo+(random(N)*(yhi-ylo)))
        
                cvals.extend(list(cs))

>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816
    return np.array(cvals)

@jit
def buddhabrot(xbound, ybound, cvals, update_func, args=2, width=5, height=5, dpi=100, maxiter=100, horizon=1.0E6):

<<<<<<< HEAD
    """
        computes the orbits of the cvals (output by compute_cvals) to form the Buddhabrot image
    """

=======
>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816
    xmin,xmax = [float(xbound[0]),float(xbound[1])]
    ymin,ymax = [float(ybound[0]),float(ybound[1])]

    nx = width*dpi
    ny = height*dpi

    xvals  = np.array([xmin + i*(xmax-xmin)/(nx) for i in range(nx)], dtype=np.float32)
    yvals  = np.array([ymin + i*(ymax-ymin)/(ny) for i in range(ny)], dtype=np.float32)
    xboxs = [(xvals[i],xvals[i+1]) for i in range(len(xvals)-1)]
    yboxs = [(yvals[i],yvals[i+1]) for i in range(len(yvals)-1)]
    xboxs = xboxs + [(xboxs[-1][1], xmax)]
    yboxs = yboxs + [(yboxs[-1][1], ymax)]

    lattice = np.zeros((int(width*dpi), int(height*dpi)), dtype=np.float32)

    for c in cvals:

        z = c
        trial_sequence = []
        sequence = []

        for N in range(maxiter):
    
            az = np.abs(z)
            trial_sequence.append(z)

            if az > horizon:
                sequence.extend(trial_sequence)
                break

            z = update_func(z, c, args)

        for c in sequence:

            indx = 0
            indy = 0
    
            for bx in range(nx):
                if xboxs[bx][0] < c.real < xboxs[bx][1]:
                    indx += bx
                    break
    
            for by in range(ny):
                if yboxs[by][0] < c.imag < yboxs[by][1]:
                    indy += by
                    break
    
            if indx != 0 and indy != 0:
                lattice[indx,indy] += 1

    return (lattice, width, height, dpi)

def run_nebula(xB, yB, Ncvals, update_func, gamma=0.5, args=2, importance_weight=0.5, width=5, height=5, dpi=100, maxiters=(100,1000,10000)):

<<<<<<< HEAD
    """
        calculates 3 Buddhabrot image with different maxiters, lowest maxiter = red channgel, middle = green, highest = blue
        (looks like a nebula)
    """

=======
>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816
    start_time = time.time()
    mi0, mi1, mi2 = maxiters
    
    cvals = compute_cvals(Ncvals, xB, yB, update_func, args=args, width=width, height=height, dpi=dpi, importance_weight=importance_weight)

    bud0 = buddhabrot(xB, yB, cvals, update_func, args=args, horizon=1.0E6, maxiter=mi0, width=width, height=height, dpi=dpi)
    save_image_array(bud0, name='save0')
    
    bud1 = buddhabrot(xB, yB, cvals, update_func, args=args, horizon=1.0E6, maxiter=mi1, width=width, height=height, dpi=dpi)
    save_image_array(bud1, name='save1')
    
    bud2 = buddhabrot(xB, yB, cvals, update_func, args=args, horizon=1.0E6, maxiter=mi2, width=width, height=height, dpi=dpi)
    save_image_array(bud2, name='save2')
    
    nebula_image(bud0, bud1, bud2, gamma=gamma)
    
    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))

if __name__ == '__main__':

    pass

