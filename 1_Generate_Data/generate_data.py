import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter
import numba
from numba import jit
import scienceplots
from scipy.linalg import eigh_tridiagonal
plt.style.use(['science', 'notebook', 'grid'])


Nx = 401
Nt = 1000000
dx = 1/(Nx-1)
dt=1e-8
x = np.linspace(0, 1, Nx)

def generate_data(psi0,exp5=False):

    
    mu, sigma = 1/2, 1/20
    V = -1e4*np.exp(-(x-mu)**2/(2*sigma**2))
    if exp5:
        V = 2e5*(x-0.5)**2

    psi = np.zeros([Nt,Nx]).astype(complex)
    psi[0] = psi0

    @numba.jit("c16[:,:](c16[:,:])", nopython=True, nogil=True)
    def compute_psi(psi):
        for t in range(0, Nt-1):
            for i in range(1, Nx-1):
                psi[t+1][i] = psi[t][i] + 1j/2 * dt/dx**2 * (psi[t][i+1] - 2*psi[t][i] + psi[t][i-1]) - 1j*dt*V[i]*psi[t][i]
            
            normal = np.sum(np.absolute(psi[t+1])**2)*dx
            for i in range(1, Nx-1):
                psi[t+1][i] = psi[t+1][i]/normal
            
        return psi
    
    computed_psi = compute_psi(psi.astype(complex))

    return np.array([computed_psi[i] for i in range(len(computed_psi)) if i%100 == 0] )

def create_animation(psi,filename='pen.gif'):

    def animate(i):
        ln1.set_data(x, np.absolute(psi[10*i])**2)
        time_text.set_text('$(10^4 mL^2)^{-1}t=$'+'{:.1f}'.format(1000*i*dt*1e4))
        
    fig, ax = plt.subplots(1,1, figsize=(8,4))
    #ax.grid()
    ln1, = plt.plot([], [], 'r-', lw=1.5, markersize=8, label='Method 1')
    time_text = ax.text(0.68, 17, '', fontsize=15,
            bbox=dict(facecolor='white', edgecolor='black'))
    ax.set_ylim(-1, 20)
    if filename == 'animation3.gif':
        ax.set_ylim(-0.5, 5)
        time_text = ax.text(0.68, 5*17/20, '', fontsize=15,
            bbox=dict(facecolor='white', edgecolor='black'))
    ax.set_xlim(0,1)
    ax.set_ylabel('$|\psi(x)|^2$', fontsize=20)
    ax.set_xlabel('$x/L$', fontsize=20)
    #ax.legend(loc='upper left')
    ax.set_title('Simulation ' + str(filename.split('.')[0][-1]))
    plt.tight_layout()
    ani = animation.FuncAnimation(fig, animate, frames=1000, interval=50)
    ani.save(filename,writer='pillow',fps=50,dpi=100)