# Imports required to read the code
import numpy as np
from scipy import optimize
import sympy as sm
from sympy import *
import random

# Step 1: Initialize the baseline parameters 
s_K = 0.15
s_H = 0.10
g = 0.02
n = 0.01
alpha = 1/3
phi = 1/3
delta = 0.075


def solow_equations(vars , s_K, s_H, n , g, delta, alpha, phi):

    k_tilde , h_tilde = vars

    solow_k = (s_K * k_tilde**alpha * h_tilde**phi - (delta + n + g + n*g)*k_tilde)/((1+n)*(1+g))
    solow_h = (s_H * k_tilde**alpha * h_tilde**phi - (delta + n + g + n*g)*h_tilde)/((1+n)*(1+g))

    return solow_k , solow_h


def ss_solve(num_guess = 500, bounds=[-1000, 1000], fun=solow_equations, args = None , method='hybr'):

        smallest_res = np.inf

        random_samples = list(np.random.uniform(low=bounds[0],high=bounds[1], size=num_guess))

        for i in range(num_guess):
            initial_guess=random.sample(random_samples, 2)

            solution = optimize.root(fun = fun, x0=initial_guess, args=args, method=method)

            residual_norm = np.linalg.norm(solution.fun)

            if residual_norm<smallest_res:
                smallest_res=residual_norm
                ss_k , ss_h = solution.x
        
        return ss_k, ss_h, smallest_res
