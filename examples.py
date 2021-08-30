import numpy as np
import time
from matplotlib import pyplot as plt
from complex_dynamics import mandelbrot, julia, julia_series, power, cosine, magnetic_1, magnetic_2
from random_walks import random_walk_3D
from buddhabrot import compute_cvals, buddhabrot
from image_creation import image, save_image_array, nebula_image, stack_cmaps, animate

pi = np.pi 

# ----- Mandelbrot images ----- #


def mandelbrot_ex0(): # basic Mandelbrot set

    xB = (-1.70, 0.75)
    yB = (-1.25, 1.25)
<<<<<<< HEAD

    start_time = time.time()

    man = mandelbrot(xB, yB, power, args=2, width=5, height=5, maxiter=500, dpi=300)
    image(man, cmap=plt.cm.hot, filename='mandelbrot_ex0', gamma=0.20)

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))
=======

    start_time = time.time()

    man = mandelbrot(xB, yB, power, args=2, width=5, height=5, maxiter=500, dpi=300)
    image(man, cmap=plt.cm.hot, filename='mandelbrot_ex0', gamma=0.20)

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))

>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816

def mandelbrot_ex1(): # slighly zoomed Mandelbrot

    xB = (-0.748770, -0.748720)
    yB = ( 0.065053,  0.065103)

    start_time = time.time()

    man = mandelbrot(xB, yB, power, args=2, width=5, height=5, maxiter=5000, dpi=300)
    image(man, cmap=plt.cm.gist_yarg, filename='mandelbrot_ex1', gamma=0.3)
<<<<<<< HEAD

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))
=======

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))

>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816

def mandelbrot_ex2(): # lowered maxiter from ex0

    xB = (-1.70, 0.75)
    yB = (-1.25, 1.25)
<<<<<<< HEAD

    start_time = time.time()

    man = mandelbrot(xB, yB, power, args=2, width=5, height=5, maxiter=100, dpi=300)
    image(man, cmap=plt.cm.hot, filename='mandelbrot_ex2', gamma=0.3)

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))
=======

    start_time = time.time()

    man = mandelbrot(xB, yB, power, args=2, width=5, height=5, maxiter=100, dpi=300)
    image(man, cmap=plt.cm.hot, filename='mandelbrot_ex1', gamma=0.3)

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))

>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816

def mandelbrot_ex3(): # zoomed in on a mini-Mandel, stacked colormaps look good

<<<<<<< HEAD
    xB = ( 0.3602404434376143632361252444495 - 0.00000000000003,  0.3602404434376143632361252444495 + 0.00000000000025)
    yB = (-0.6413130610648031748603750151793 - 0.00000000000005, -0.6413130610648031748603750151793 + 0.00000000000013)

    start_time = time.time()
    mymap = stack_cmaps(plt.cm.gist_gray, 50)

    man = mandelbrot(xB, yB, power, args=2, width=6, height=4, maxiter=5000, dpi=300)
    image(man, cmap=mymap, filename='mandelbrot_ex3', gamma=0.8)

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))
=======
    xB = ( 0.3602404434376143632361252444495 - 0.00000000000007,  0.3602404434376143632361252444495 + 0.00000000000023)
    yB = (-0.6413130610648031748603750151793 - 0.00000000000008, -0.6413130610648031748603750151793 + 0.00000000000012)

    start_time = time.time()
    mymap = stack_cmaps(plt.cm.terrain, 5)

    man = mandelbrot(xB, yB, power, args=2, width=5, height=5, maxiter=5000, dpi=300)
    image(man, cmap=mymap, filename='mandelbrot_ex1', gamma=0.8)

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))

# ----- Julia images ----- #
>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816


def julia_ex0():

    c = 1j
    xB = (-1.5, 1.5)
    yB = (-1.5, 1.5)
<<<<<<< HEAD

    start_time = time.time()

    jul = julia(c, xB, yB, power, args=2, width=5, height=5, maxiter=500, dpi=300)
    image(jul, cmap=plt.cm.viridis, filename='julia_ex0', gamma=0.6)

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))

def julia_ex1():

    c = -0.391 - 0.587j 
    xB = (-1.5, 1.5)
    yB = (-1.5, 1.5)

    start_time = time.time()

    jul = julia(c, xB, yB, power, args=2, width=5, height=5, maxiter=1000, dpi=300)
    image(jul, cmap=plt.cm.gist_ncar, filename='julia_ex1', gamma=0.6)

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))

def cos_julia_ex():

    c = pi/2*(1.0 + 0.6j) 
=======

    start_time = time.time()

    jul = julia(c, xB, yB, power, args=2, width=5, height=5, maxiter=500, dpi=300)
    image(jul, cmap=plt.cm.viridis, filename='julia_ex0', gamma=0.6)

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))


def julia_ex1():

    c = -0.391 - 0.587j
    xB = (-1.5, 1.5)
    yB = (-1.5, 1.5)

    start_time = time.time()

    jul = julia(c, xB, yB, power, args=2, width=5, height=5, maxiter=1000, dpi=300)
    image(jul, cmap=plt.cm.gist_ncar, filename='julia_ex1', gamma=0.6)

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))


def cos_julia_ex():

    c = pi/2*(1.0 + 0.6j)
>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816
    xB = (-1.5, 1.5)
    yB = (-1.5, 1.5)

    start_time = time.time()

    jul = julia(c, xB, yB, cosine, args=0, width=5, height=5, maxiter=1000, dpi=300)
    image(jul, cmap=plt.cm.plasma, filename='cos_julia_ex', gamma=1.0)
<<<<<<< HEAD

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))
=======

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))

>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816

def mag_julia_ex0():

    c = 2.0j
    xB = (-2.5, 0.5)
    yB = (-2.5, 0.5)
<<<<<<< HEAD

    start_time = time.time()

    jul = julia(c, xB, yB, magnetic_1, args=0, width=5, height=5, maxiter=1000, dpi=300)
    image(jul, cmap=plt.cm.gist_ncar, filename='mag_julia_ex0', gamma=0.5)

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))
=======

    start_time = time.time()

    jul = julia(c, xB, yB, magnetic_1, args=0, width=5, height=5, maxiter=1000, dpi=300)
    image(jul, cmap=plt.cm.gist_ncar, filename='mag_julia_ex0', gamma=0.5)

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))

>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816

def mag_julia_ex1():

    c = 2.0 + 0.80j
    xB = (-1.0, 1.0)
    yB = (-1.0, 1.0)

    start_time = time.time()

    jul = julia(c, xB, yB, magnetic_2, args=0, width=5, height=5, maxiter=1000, dpi=300)
    image(jul, cmap=plt.cm.gist_ncar, filename='mag_julia_ex1', gamma=1.0)

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))
<<<<<<< HEAD
=======

# ----- Animation ----- #
>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816


def julia_animation_ex():

    start_time = time.time()

    c_vals = np.array([complex(i,0.75) for i in np.linspace(0.05, 3.0, 100)])
    s = julia_series(c_vals, [-1,1], [-0.75,1.25], magnetic_2, args=2, maxiter=100)
    animate(s, gamma=0.9, cmap=plt.cm.gist_ncar, filename='julia_animation_ex')

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))
<<<<<<< HEAD
=======

# ----- random walk -----#
# to add
>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816

# ----- buddhabrot -----#
# this will take awhile


def buddhabrot_ex():

    xB = (-1.75, 0.85)
    yB = (-1.10, 1.10)
<<<<<<< HEAD
    
    start_time = time.time()

    cvals = compute_cvals(1000000, xB, yB, power, args=2, width=5, height=4, dpi=300)

    bud0 = buddhabrot(xB, yB, cvals, power, args=2, horizon=1.0E6, maxiter=100, width=5, height=4, dpi=300)
    save_image_array(bud0, name='save0')

    bud1 = buddhabrot(xB, yB, cvals, power, args=2, horizon=1.0E6, maxiter=1000, width=5, height=4, dpi=300)
    save_image_array(bud1, name='save1')
    
    bud2 = buddhabrot(xB, yB, cvals, power, args=2, horizon=1.0E6, maxiter=10000, width=5, height=4, dpi=300)
    save_image_array(bud2, name='save2')
    
=======

    start_time = time.time()

    cvals = compute_cvals(1000000, xB, yB, power, args=2, width=5, height=4, dpi=300)

    bud0 = buddhabrot(xB, yB, cvals, power, args=2, horizon=1.0E6, maxiter=100, width=5, height=4, dpi=300)
    save_image_array(bud0, name='save0')

    bud1 = buddhabrot(xB, yB, cvals, power, args=2, horizon=1.0E6, maxiter=1000, width=5, height=4, dpi=300)
    save_image_array(bud1, name='save1')

    bud2 = buddhabrot(xB, yB, cvals, power, args=2, horizon=1.0E6, maxiter=10000, width=5, height=4, dpi=300)
    save_image_array(bud2, name='save2')

>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816
    nebula_image(bud0, bud1, bud2, gamma=0.4, filename='buddhabrot_ex', image_type='tiff')

    print('calculation took %s seconds ' % np.round((time.time() - start_time), 3))

if __name__ == '__main__':

<<<<<<< HEAD
    #mandelbrot_ex3()
    julia_animation_ex()

    pass
    
=======
    # add example function here

    pass
>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816
