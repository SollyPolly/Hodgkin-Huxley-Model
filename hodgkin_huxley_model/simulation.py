import numpy as np
from scipy.integrate import solve_ivp
from .model import hodgkin_huxley
from .config import t_span, num_points, initial_conditions, pulse_params

def step_current(t, start=pulse_params['start_time'], amplitude=pulse_params['pulse_amplitude'], pulse_duration=pulse_params['pulse_duration']):
    if pulse_duration is None:
        return np.where(t >= start, amplitude, 0)
    else:
        return np.where((t >= start) & (t < start + pulse_duration), amplitude, 0)

def run_simulation():
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
