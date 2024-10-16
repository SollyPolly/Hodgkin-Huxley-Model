import matplotlib.pyplot as plt
from ...model import m_inf

def plot_time_constant_comparison(sol):
    time_values = sol.t
    V_values = sol.y[0]  # Membrane potential
    m_values = sol.y[2]

    # Compute steady-state values for each V
    m_inf_values = [m_inf(V) for V in V_values]

    # Filter for time values from 20 to 30 ms
    min_time, max_time = 20, 30
    mask = (time_values >= min_time) & (time_values <= max_time)
    time_values_filtered = time_values[mask]
    m_values_filtered = m_values[mask]
    m_inf_values_filtered = [m_inf_values[i] for i in range(len(m_inf_values)) if mask[i]]


    plt.figure(figsize=(8, 6))

    plt.plot(time_values_filtered, m_values_filtered, label=r'$m(t)$ (Gating Variable)', color='green')
    plt.plot(time_values_filtered, m_inf_values_filtered, label=r'$m_\infty(V(t))$ (Steady State)', color='blue', linestyle='--')

    plt.xlabel('Time (ms)')
    plt.ylabel('Gating Variables and Steady States')
    plt.title('Comparison of Gating Variables and their Steady States')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
