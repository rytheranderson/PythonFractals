import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from skimage.restoration import denoise_nl_means, estimate_sigma
from matplotlib import colors
from numpy.ma import masked_where
import matplotlib.colors as mcolors
import matplotlib.animation as animation
import pickle

def save_image_array(A, name='save'):

    with open(name + '.pkl','wb') as f:
        pickle.dump(A, f)

def open_image_array(file):

    with open(file,'rb') as f:
        A = pickle.load(f)
        return A

def stack_cmaps(cmap, Nstacks):
    
    colors = np.array(cmap(np.linspace(0, 1, 200))) 
    
    for n in range(Nstacks - 1):
        colors = np.vstack((colors, cmap(np.linspace(0, 1, 200))))

    mymap = mcolors.LinearSegmentedColormap.from_list('my_colormap', colors)

    return mymap

def image(lattice, cmap=plt.cm.hot, filename='f', image_type='png', ticks='off', gamma=0.3, vert_exag=0, ls=[315,10]):

    A, width, height, dpi = lattice
    A = A.T

    w,h = plt.figaspect(A)
    fig, ax0 = plt.subplots(figsize=(w,h), dpi=dpi)
    fig.subplots_adjust(0,0,1,1)
    plt.axis(ticks)

    norm = colors.PowerNorm(gamma)
    light = colors.LightSource(azdeg=ls[0], altdeg=ls[1])
    
    if vert_exag != 0.0:
        M = light.shade(A, cmap=cmap, norm=norm, vert_exag=vert_exag, blend_mode='hsv')
        ax0.imshow(M, origin='lower')
    else: 
        M = A
        ax0.imshow(M, origin='lower', cmap=cmap, norm=norm)

    F = plt.gcf()
    F.set_size_inches(width, height)

    fig.savefig(filename + '.' + image_type, dpi=dpi)

def nebula_image(AB, AG, AR, filename='f', image_type='png', ticks='off', gamma=1.0, denoise=False):

    A_blue, width, height, dpi = AB
    A_green = AG[0]
    A_red = AR[0]

    A_blue = A_blue.T
    A_green = A_green.T
    A_red = A_red.T

    A_blue /= np.amax(A_blue)
    A_green /= np.amax(A_green)
    A_red /= np.amax(A_red)

    w,h = plt.figaspect(A_blue)
    fig, ax0 = plt.subplots(figsize=(w,h), dpi=dpi)
    fig.subplots_adjust(0,0,1,1)
    plt.axis(ticks)

    M = np.dstack((A_red, A_green, A_blue))

    if denoise:
        sigma_est = np.mean(estimate_sigma(M, multichannel=True))
        patch_kw = dict(patch_size=9, patch_distance=15, multichannel=True)
        M = denoise_nl_means(M, h=0.9*sigma_est, fast_mode=True, **patch_kw)

    ax0.imshow(M**gamma, origin='lower')
    F = plt.gcf()
    F.set_size_inches(width, height)

    fig.savefig(filename + '.' + image_type, dpi=dpi)

def animate(series, fps=15, bitrate=1800, cmap=plt.cm.hot, filename='f', ticks='off', gamma=0.3, vert_exag=0, ls=[315,10]):

<<<<<<< HEAD
    writer = animation.PillowWriter(fps=fps, metadata=dict(artist='Me'), bitrate=bitrate)
=======
    Writer = animation.writers['Pillow']
    writer = Writer(fps=fps, metadata=dict(artist='Me'), bitrate=bitrate)
>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816

    norm = colors.PowerNorm(gamma)
    light = colors.LightSource(azdeg=ls[0], altdeg=ls[1])

    foo, width, height, dpi = series[0]
    FIG = plt.figure()
    F = plt.gcf()
    F.set_size_inches(width, height)
    plt.axis(ticks)
    ims = []

    for s in series:

        A, width, height, dpi = s
        A = A.T
        M = light.shade(A, cmap=cmap, norm=norm, vert_exag=vert_exag, blend_mode='hsv')
        im = plt.imshow(M, origin='lower', norm=norm)
        ims.append([im])

    ani = animation.ArtistAnimation(FIG, ims, interval=50, blit=True, repeat_delay=1000)
<<<<<<< HEAD
    ani.save(filename + '.gif', dpi=dpi, writer=writer)
=======
    ani.save(filename + '.mp4', dpi=dpi)
>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816

def markus_lyapunov_image(M, gammas=(1.0, 1.0, 1.0), ticks='off', filename='f', image_type='png', ls=[315,10], vert_exag=0.0):

    A, width, height, dpi = M
    rg, gg, bg = gammas 
    
    red = np.zeros(A.shape) ** rg

    green = np.zeros(A.shape) + A
    green[green > 0.0] = 0.0
    green[green < 0.0] -= np.amin(green)
    green /= np.amax(green)
    green = green ** gg

    blue = np.zeros(A.shape) + A
    blue[blue < 0.0] = 0.0
    blue[blue > 0.0] -= np.amin(blue)
    blue /= np.amax(blue)
    blue = blue ** bg

    w,h = plt.figaspect(blue)
    fig, ax0 = plt.subplots(figsize=(width,height), dpi=dpi)
    fig.subplots_adjust(0,0,1,1)
    plt.axis(ticks)

    M = np.dstack((red, green, blue))
<<<<<<< HEAD
    elev = A

    if vert_exag != 0.0:
        light = colors.LightSource(azdeg=ls[0], altdeg=ls[1])
        M = light.shade_rgb(M, elev, vert_exag=vert_exag, blend_mode='hsv')
        ax0.imshow(M, origin='lower')
    else: 
        ax0.imshow(M, origin='lower', vmin=0.0, vmax=1.0)

    F = plt.gcf()
    F.set_size_inches(width, height)

=======
    ax0.imshow(M, origin='lower', vmin=0.0, vmax=1.0)
    F = plt.gcf()
    F.set_size_inches(width, height)

>>>>>>> f087012c1bf19f0a595a8a98d4526c198fd3a816
    fig.savefig(filename + '.' + image_type, dpi=dpi)

def random_walk_3D_image(lattice, cmap=plt.cm.hot, single_color=False, filename='f', image_type='png', ticks='off', gamma=0.3, vert_exag=0, ls=[315,10], alpha_scale=1.0):

    A, width, height, dpi = lattice

    if single_color:
        A[np.nonzero(A)] = 1.0

    w,h = plt.figaspect(A[:,:,0])
    fig, ax0 = plt.subplots(figsize=(w,h), dpi=dpi)
    fig.subplots_adjust(0,0,1,1)
    plt.axis(ticks)

    max_ind = float(A.shape[-1] + 1)

    for i in range(A.shape[-1]):
        
        IM = A[..., i]
        IM = masked_where(IM == 0, IM)

        alpha = 1 - (i + 1)/max_ind
        alpha *= alpha_scale

        norm = colors.PowerNorm(gamma)
        light = colors.LightSource(azdeg=ls[0], altdeg=ls[1])

        if vert_exag != 0.0:
            M = light.shade(IM, cmap=cmap, vert_exag=vert_exag, blend_mode='overlay')
            ax0.imshow(M, origin='lower', alpha=alpha, interpolation=None)
        else: 
            M = IM
            ax0.imshow(M, origin='lower', alpha=alpha, cmap=cmap, norm=norm, interpolation=None)
        
    F = plt.gcf()
    F.set_size_inches(width, height)
        
    fig.savefig(filename + '.' + image_type, dpi=dpi)

