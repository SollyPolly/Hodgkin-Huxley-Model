import matplotlib.pyplot as plt
import numpy as np
from ..config import pulse_params
from ..model import compute_derivatives

def plot_phase_diagram_fixed_gating(sol, gating_var_name, n0, h0):
    t = sol.t

    V_values = np.linspace(-100, 50, 20)
    gating_var_values = np.linspace(0, 1, 20)
    V_grid, gating_var_grid = np.meshgrid(V_values, gating_var_values)

    I = step_current(t, start=pulse_params['start_time'], amplitude=pulse_params['pulse_amplitude'], pulse_duration=pulse_params['pulse_duration'])
    dV_grid = np.zeros_like(V_grid)
    dgating_var_grid = np.zeros_like(gating_var_grid)

    for i in range(V_grid.shape[0]):
        for j in range(V_grid.shape[1]):
            V = V_grid[i, j]
            gating_var = gating_var_grid[i, j]
            
            dV, dgating_var = compute_derivatives(V, gating_var, gating_var_name, I, n=n0, h=h0)
            dV_grid[i, j] = dV[0]
            dgating_var_grid[i, j] = dgating_var

    magnitude = np.sqrt(dV_grid**2 + dgating_var_grid**2)
    magnitude[magnitude == 0] = 1e-10

    dV_grid_norm = dV_grid / magnitude
    dgating_var_grid_norm = dgating_var_grid / magnitude

    plt.figure(figsize=(8, 6))
    q = plt.quiver(V_grid, gating_var_grid, dV_grid_norm, dgating_var_grid_norm,
                   magnitude, cmap='plasma', pivot='mid')
    plt.colorbar(q, label='Vector Magnitude')

    V_values = sol.y[0]
    gating_var_values = sol.y[['n', 'm', 'h'].index(gating_var_name) + 1]

    plt.plot(V_values, gating_var_values, color='blue', label='Trajectory')

    plt.xlabel('Membrane Potential V (mV)')
    plt.ylabel(f'Gating Variable {gating_var_name}')
    plt.title(f'Phase Diagram with Slope Field for V and {gating_var_name}\n (h={h0}, n={n0} constant)')
    plt.legend()
    plt.grid(True)
    plt.show()

def step_current(t, start, amplitude, pulse_duration):
    if pulse_duration is None:
        return np.where(t >= start, amplitude, 0)
    else:
        return np.where((t >= start) & (t < start + pulse_duration), amplitude, 0)
