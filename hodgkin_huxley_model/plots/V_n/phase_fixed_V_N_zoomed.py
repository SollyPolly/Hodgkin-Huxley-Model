import matplotlib.pyplot as plt
import numpy as np
from ...model import V_n_calculate_derivatives
from ...functions import find_intersections, step_current
from scipy.interpolate import interp1d

def plot_phase_fixed_zoomed_V_N(sol):
    t = sol.t

    # Form a 2D grid of V and m values
    V_values = np.linspace(-100, 60, 100)
    n_values = np.linspace(0, 1.2, 100)
    V_grid, n_grid = np.meshgrid(V_values, n_values)

    I = step_current(t[0])

    # Calculate the derivatives at each point in the grid
    dV_grid = np.zeros_like(V_grid)
    dn_grid = np.zeros_like(n_grid)

    for i in range(V_grid.shape[0]):
        for j in range(V_grid.shape[1]):
            V = V_grid[i, j]
            n = n_grid[i, j]
            dV, dn = V_n_calculate_derivatives(V, n, I)
            dV_grid[i, j] = dV
            dn_grid[i, j] = dn

    # Normalize the vectors
    magnitude = np.sqrt(dV_grid**2 + dn_grid**2)
    magnitude[magnitude == 0] = 1e-10

    dV_grid_norm = dV_grid / magnitude
    dn_grid_norm = dn_grid / magnitude

    # Plot the slope field using quiver
    plt.figure(figsize=(8, 6))
    q = plt.quiver(V_grid, n_grid, dV_grid_norm, dn_grid_norm,
                   magnitude, cmap='plasma', pivot='mid', scale=50)
    
    # Get values for the trajectory
    V_values = sol.y[0]
    n_values = sol.y[1]

    # Plot the system trajectory
    plt.plot(V_values, n_values, color='red', label='Trajectory')

    # Plot the zero-crossing lines without labels
    dV_contour = plt.contour(V_grid, n_grid, dV_grid, levels=[0], colors='green', linestyles='dashed', linewidths=1)
    dm_contour = plt.contour(V_grid, n_grid, dn_grid, levels=[0], colors='green', linestyles='dashed', linewidths=2)

    # Find intersection points of the contours
    xi = np.array([])
    yi = np.array([])
    for path1 in dV_contour.collections[0].get_paths():
        for path2 in dm_contour.collections[0].get_paths():
            xinter, yinter = find_intersections(path1.vertices, path2.vertices)
            xi = np.append(xi, xinter)
            yi = np.append(yi, yinter)

    # Plot the intersection points
    plt.scatter(xi, yi, color='purple', s=50, zorder=5, label='Intersection Points')
    
    # Add labels to the legend manually
    plt.plot([], [], color='green', linestyle='dashed', label='dV = 0')
    plt.plot([], [], color='green', linestyle='dashed', label='dn = 0')
  
    plt.xlim(-70, -50)  # Set x-axis limits
    plt.ylim(0.0, 0.15)   # Set y-axis limits
    
    plt.xlabel('Membrane Potential V (mV)')
    plt.ylabel('Gating Variable n')
    plt.title(f'Phase Diagram with Slope Field for V and n (V_n)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Import necessary functions to run a simulation
    from ...simulation import run_simulation
    
    # Run a simulation to get the solution
    _, _, _, V_N_hh_sol = run_simulation()
    

