import numpy as np
from scipy.integrate import solve_ivp
from .model import hodgkin_huxley, simple_hodgkin_huxley, step_current
from .config import t_span, num_points, initial_conditions

def run_hh_simulation():
    t_eval = np.linspace(t_span[0], t_span[1], num_points)
    y0 = [
        initial_conditions['V0'],
        initial_conditions['n0'],
        initial_conditions['m0'],
        initial_conditions['h0']
    ]

    def ode_wrapper(t, y):
        return hodgkin_huxley(t, y, step_current(t))

    sol = solve_ivp(ode_wrapper, t_span, y0, t_eval=t_eval)
    return sol

def run_simple_hh_simulation():
    t_eval = np.linspace(t_span[0], t_span[1], num_points)
    y0 = [
        initial_conditions['V0'],
        initial_conditions['m0']
    ]

    def ode_wrapper(t, y):
        return simple_hodgkin_huxley(t, y, step_current(t), initial_conditions['V0'])

    sol = solve_ivp(ode_wrapper, t_span, y0, t_eval=t_eval)
    return sol

def run_both_simulations():
    hh_sol = run_hh_simulation()
    simple_hh_sol = run_simple_hh_simulation()
    return hh_sol, simple_hh_sol

def run_simulation():
    return run_both_simulations()