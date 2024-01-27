import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import diag
from numpy import pi, exp, sin, cos, cosh, tanh, real, imag
from numpy.linalg import inv, eig, pinv
from scipy.linalg import svd

def DMD(X, Y, r=10):

    # Step 1, perform SVD for X
    U2,Sig2,Vh2 = svd(X, False)

    # Rank r truncation
    U = U2[:,:r]
    Sig = diag(Sig2)[:r,:r]
    V = Vh2.conj().T[:,:r]

    # Step 2, build A tilde
    Atil = U.conj().T @ Y @ V @ inv(Sig)
    
    # Step 3 build DMD modes
    mu,W = eig(Atil)
    Phi = Y @ V @ inv(Sig) @ W

    # Step 4, compute A
    Phi_inv = pinv(Phi)
    A = Phi @ diag(mu) @ Phi_inv

    return A