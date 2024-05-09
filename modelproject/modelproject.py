from types import SimpleNamespace
import numpy as np
from scipy import optimize

class SolowClass():

    def __init__(self,do_print=True):
        """ create the model """

        if do_print: print('initializing the model:')

        self.par = SimpleNamespace()
        self.ss = SimpleNamespace()
        self.path = SimpleNamespace()

        if do_print: print('calling .setup()')
        self.setup()

    
    def setup(self):
        """ baseline parameters """

        par = self.par

        par.s_K = 2.0 # Saving rate physical capital
        par.s_H = 0.1 # Saving rate human capital
        par.g = 0.02 # Growth rate in technology
        par.n = 0.01 # Growth rate in population
        par.alpha = 1/3 # capital weight  
        par.phi = 1/3 #     
        par.delta = 0.05 # depreciation rate
        par.production_function = 'cobb-douglas'

        # c. initial
        par.K_lag_ini = 1.0
        par.L_lag_ini = 1.0
        par.A_lag_ini = 1.0
        par.Y_lag_ini = 1.0

        # d. misc
        par.solver = 'broyden' # solver for the equation system, 'broyden' or 'scipy'
        par.Tpath = 500 # length of transition path, "truncation horizon"
        
    def solow_equations(vars , s_K, s_H, n , g, delta, alpha, phi):

        k_tilde , h_tilde = vars

        solow_k = (s_K * k_tilde**alpha * h_tilde**phi - (delta + n + g + n*g)*k_tilde)/((1+n)*(1+g))
        solow_h = (s_H * k_tilde**alpha * h_tilde**phi - (delta + n + g + n*g)*h_tilde)/((1+n)*(1+g))

        return solow_k , solow_h



def solve_ss(alpha, c):
    """ Example function. Solve for steady state k. 

    Args:
        c (float): costs
        alpha (float): parameter

    Returns:
        result (RootResults): the solution represented as a RootResults object.

    """ 
    
    # a. Objective function, depends on k (endogenous) and c (exogenous).
    f = lambda k: k**alpha - c
    obj = lambda kss: kss - f(kss)

    #. b. call root finder to find kss.
    result = optimize.root_scalar(obj,bracket=[0.1,100],method='bisect')
    
    return result


def solow_equations(vars , s_K, s_H, n , g, delta, alpha, phi):
    k_tilde , h_tilde = vars
    solow_k = (s_K * k_tilde**alpha * h_tilde**phi - (delta + n + g + n*g)*k_tilde)/((1+n)*(1+g))
    solow_h = (s_H * k_tilde**alpha * h_tilde**phi - (delta + n + g + n*g)*h_tilde)/((1+n)*(1+g))
    return solow_k , solow_h

