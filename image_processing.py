import numpy as np
import time
import sys
import pickle

import matplotlib
matplotlib.use('Agg')

from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib.colors import Normalize
import matplotlib.animation as animation
from scipy.ndimage import gaussian_filter
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage.util import random_noise

def layered_color_map_image(AB, AG, AR, cmap0, cmap1, cmap2, filename='f', image_type='png', ticks='off', gammas=(1.0, 1.0, 1.0), vmin=0.0, vmax0=1.0, vmax1=1.0, vmax2=1.0):

    A_blue, width, height, dpi = AB
    A_green = AG[0]
    A_red = AR[0]

    #A_blue = A_blue.T
    #A_green = A_green.T
    #A_red = A_red.T

    A_blue /= np.amax(A_blue)
    A_green /= np.amax(A_green)
    A_red /= np.amax(A_red)

    s0 = np.mean(estimate_sigma(A_blue))
    s1 = np.mean(estimate_sigma(A_green))
    s2 = np.mean(estimate_sigma(A_red))
    
    #patch_kw = dict(patch_size=9, patch_distance=15)
    #A_blue = denoise_nl_means(A_blue, h=0.95*s0, fast_mode=True, **patch_kw)
    #A_green = denoise_nl_means(A_green, h=0.95*s1, fast_mode=True, **patch_kw)
    #A_red = denoise_nl_means(A_red, h=0.95*s2, fast_mode=True, **patch_kw)

    w,h = plt.figaspect(A_blue)
    fig, ax0 = plt.subplots(figsize=(w,h), dpi=dpi)
    fig.subplots_adjust(0,0,1,1)
    plt.axis(ticks)

    norm0 = colors.PowerNorm(gammas[0], vmin=vmin, vmax=vmax0)
    norm1 = colors.PowerNorm(gammas[1], vmin=vmin, vmax=vmax1)
    norm2 = colors.PowerNorm(gammas[2], vmin=vmin, vmax=vmax2)

    ax0.imshow(A_blue, origin='lower', cmap=cmap0, norm=norm0, alpha=0.50)
    ax0.imshow(A_green, origin='lower', cmap=cmap1, norm=norm1, alpha=0.50)
    ax0.imshow(A_red, origin='lower', cmap=cmap2, norm=norm2, alpha=0.50)

    F = plt.gcf()
    F.set_size_inches(width, height)

    fig.savefig(filename + '.' + image_type, dpi=dpi)

def nebula_image(AB, AG, AR, filename='f', image_type='png', ticks='off', gammas=(1.0,1.0,1.0), vmin=0.0, vmax=1.0):

    A_blue, width, height, dpi = AB
    A_green = AG[0]
    A_red = AR[0]

    A_blue /= np.amax(A_blue)
    A_green /= np.amax(A_green)
    A_red /= np.amax(A_red)

    A_blue = A_blue**gammas[0]
    A_green = A_green**gammas[1]
    A_red = A_red**gammas[2]

    w,h = plt.figaspect(A_blue)
    fig, ax0 = plt.subplots(figsize=(w,h), dpi=dpi)
    fig.subplots_adjust(0,0,1,1)
    plt.axis(ticks)

    M = np.dstack((A_red, A_green, A_blue))

    sigma_est = np.mean(estimate_sigma(M, multichannel=True))
    patch_kw = dict(patch_size=9, patch_distance=15, multichannel=True)
    M = denoise_nl_means(M, h=1.0*sigma_est, fast_mode=True, **patch_kw)

    ax0.imshow(M, origin='lower', vmin=vmin, vmax=vmax)

    F = plt.gcf()
    F.set_size_inches(width, height)

    fig.savefig(filename + '.' + image_type, dpi=dpi)

def save_image_array(A, name='save'):

    with open(name + '.pkl','wb') as f:
        pickle.dump(A, f)

def open_image_array(file):

    with open(file,'rb') as f:
        A = pickle.load(f)
        return A

M = open_image_array('save.pkl')
blue = M[:,:,1]
green = M[:,:,2] + 0.1 
red = M[:,:,0]

red = (red, 24, 36, 100)
green = (green, 24, 36, 100)
blue = (blue, 24, 36, 100)
#layered_color_map_image(blue, green red, plt.cm.tab20b, plt.cm.tab20b, plt.cm.tab20b, filename='cm', gammas=(1.0, 1.0, 1.0))
nebula_image(green, blue, red, gammas=(1.0,1.0,1.0), filename='neb', image_type='tiff')


