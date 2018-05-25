#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from os.path import join
mpl.rcParams['agg.path.chunksize'] = 100000

# Exercise 4
X_0 = 36.  # [g/cm^2]
E_c = 89.  # [MeV]
A= 26.
E_0 = np.linspace(1.0e11, 1.0e14, 10000)  # [MeV]
lambda_i = 90.-9.*np.log(E_0/1.e18)
N_pi = (E_0/1.e15)**(1./5.)
X_max_EM = X_0*np.log(E_0/E_c)  # [g/cm^2]
X_max_p = lambda_i*np.log(2.)+X_0*np.log(E_0/(6*N_pi*E_c))  # [g/cm^2]
X_max_A = -2.-36.*np.log(A)+12.*np.log(E_0**2.*1.e18/E_c**3.)  # [g/cm^2]
#X_max_A2 = X_max_p-36.*np.log(A)  # [g/cm^2]

def plot_X_max():
    plt.rc('text', usetex='True')
    plt.rc('font', family='serif')
    plt.ylabel(r'X$_{\rm max}$ [g/cm$^{-2}$]')
    plt.xlabel(r'E$_0$ [eV]')
    plt.semilogx(E_0*1.0e6, X_max_EM, ls='-', color='k', label='EM')
    plt.semilogx(E_0*1.0e6, X_max_p, ls='-', color='b', label='p')
    plt.semilogx(E_0*1.0e6, X_max_A, ls='-', color='r', label='Fe')
    #plt.semilogx(E_0*1.0e6, X_max_A2, ls='-', color='g', label='Fe 2')
    plt.legend()
    plt.savefig('plot_ex_1e.pdf')
    plt.show()
plot_X_max()




