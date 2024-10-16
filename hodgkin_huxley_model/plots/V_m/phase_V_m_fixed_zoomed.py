import matplotlib.pyplot as plt
import numpy as np
from ...model import V_m_calculate_derivatives
from ...functions import find_intersections, step_current
from scipy.interpolate import interp1d

def plot_phase_fixed_zoomed_V_M(sol):
    t = sol.t

    # Form a 2D grid of V and m values
    V_values = np.linspace(-100, 60, 100)
    m_values = np.linspace(0, 1.2, 100)
    V_grid, m_grid = np.meshgrid(V_values, m_values)

    I = step_current(t[0])

    # Calculate the derivatives at each point in the grid
    dV_grid = np.zeros_like(V_grid)
    dm_grid = np.zeros_like(m_grid)

    for i in range(V_grid.shape[0]):
        for j in range(V_grid.shape[1]):
            V = V_grid[i, j]
            m = m_grid[i, j]
            dV, dm = V_m_calculate_derivatives(V, m, I)
            dV_grid[i, j] = dV
            dm_grid[i, j] = dm

    # Normalize the vectors
    magnitude = np.sqrt(dV_grid**2 + dm_grid**2)
    magnitude[magnitude == 0] = 1e-10

    dV_grid_norm = dV_grid / magnitude
    dm_grid_norm = dm_grid / magnitude

    # Plot the slope field using quiver
    plt.figure(figsize=(8, 6))
    q = plt.quiver(V_grid, m_grid, dV_grid_norm, dm_grid_norm,
                   magnitude, cmap='plasma', pivot='mid', scale=50)
    
    # Get values for the trajectory
    V_values = sol.y[0]
    m_values = sol.y[1]

    # Plot the system trajectory
    plt.plot(V_values, m_values, color='red', label='Trajectory')

    # Plot the zero-crossing lines without labels
    dV_contour = plt.contour(V_grid, m_grid, dV_grid, levels=[0], colors='green', linestyles='dashed', linewidths=1)
    dm_contour = plt.contour(V_grid, m_grid, dm_grid, levels=[0], colors='green', linestyles='dashed', linewidths=2)

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
    plt.plot([], [], color='green', linestyle='dashed', label='dm = 0')
  
    plt.xlim(-70, -50)  # Set x-axis limits
    plt.ylim(0.0, 0.15)   # Set y-axis limits
    
    plt.xlabel('Membrane Potential V (mV)')
    plt.ylabel('Gating Variable m')
    plt.title(f'Phase Diagram with Slope Field for V and m (V_M)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Import necessary functions to run a simulation
    from ...simulation import run_simulation
    
    # Run a simulation to get the solution
    _, V_M_hh_sol, _, _ = run_simulation()
    

