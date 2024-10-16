import matplotlib.pyplot as plt
import numpy as np
from ...config import simulation_settings
from ...functions import step_current, compute_derivatives

def plot_phase_diagram(sol, gating_var_name):
    t = sol.t

    V_values = np.linspace(-100, 50, 20)
    gating_var_values = np.linspace(0, 1, 20)
    V_grid, gating_var_grid = np.meshgrid(V_values, gating_var_values)

    I = step_current(t)
    dV_grid = np.zeros_like(V_grid)
    dgating_var_grid = np.zeros_like(gating_var_grid)

    for i in range(V_grid.shape[0]):
        for j in range(V_grid.shape[1]):
            V = V_grid[i, j]
            gating_var = gating_var_grid[i, j]
            dV, dgating_var = compute_derivatives(V, gating_var, gating_var_name, I)
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

    # Plot the zero-crossing lines without labels
    dV_contour = plt.contour(V_grid, gating_var_grid, dV_grid, levels=[0], colors='green', linestyles='dashed', linewidths=1)
    dm_contour = plt.contour(V_grid, gating_var_grid, dgating_var_grid, levels=[0], colors='green', linestyles='dashed', linewidths=2)


    # Plot the system trajectory
    plt.plot(V_values, gating_var_values, color='blue', label='Trajectory')

    # Add labels to the legend manually
    plt.plot([], [], color='green', linestyle='dashed', label='dV = 0')
    plt.plot([], [], color='green', linestyle='dashed', label='dm = 0')

    plt.xlabel('Membrane Potential V (mV)')
    plt.ylabel(f'Gating Variable {gating_var_name}')
    plt.title(f'Phase Diagram with Slope Field for V and {gating_var_name}')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Import necessary functions to run a simulation
    from ...simulation import run_simulation
    
    # Run a simulation to get the solution
    hh_sol, _, _, _ = run_simulation()
    