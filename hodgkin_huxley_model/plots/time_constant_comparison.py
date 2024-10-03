import matplotlib.pyplot as plt
from ..model import m_inf, h_inf, n_inf

def plot_time_constant_comparison(sol):
    time_values = sol.t
    V_values = sol.y[0]  # Membrane potential
    m_values = sol.y[2]
    h_values = sol.y[3]
    n_values = sol.y[1]

    # Compute steady-state values for each V
    m_inf_values = [m_inf(V) for V in V_values]
    h_inf_values = [h_inf(V) for V in V_values]
    n_inf_values = [n_inf(V) for V in V_values]

    # Filter for time values from 20 to 30 ms
    min_time, max_time = 20, 30
    mask = (time_values >= min_time) & (time_values <= max_time)
    time_values_filtered = time_values[mask]
    m_values_filtered = m_values[mask]
    h_values_filtered = h_values[mask]
    n_values_filtered = n_values[mask]
    m_inf_values_filtered = [m_inf_values[i] for i in range(len(m_inf_values)) if mask[i]]
    h_inf_values_filtered = [h_inf_values[i] for i in range(len(h_inf_values)) if mask[i]]
    n_inf_values_filtered = [n_inf_values[i] for i in range(len(n_inf_values)) if mask[i]]

    plt.figure(figsize=(8, 6))

    plt.plot(time_values_filtered, m_values_filtered, label=r'$m(t)$ (Gating Variable)', color='green')
    plt.plot(time_values_filtered, m_inf_values_filtered, label=r'$m_\infty(V(t))$ (Steady State)', color='blue', linestyle='--')
    #plt.plot(time_values_filtered, h_values_filtered, label=r'$h(t)$ (Gating Variable)', color='red')
    #plt.plot(time_values_filtered, h_inf_values_filtered, label=r'$h_\infty(V(t))$ (Steady State)', color='purple', linestyle='--')
    #plt.plot(time_values_filtered, n_values_filtered, label=r'$n(t)$ (Gating Variable)', color='orange')
    #plt.plot(time_values_filtered, n_inf_values_filtered, label=r'$n_\infty(V(t))$ (Steady State)', color='brown', linestyle='--')
    
    plt.xlabel('Time (ms)')
    plt.ylabel('Gating Variables and Steady States')
    plt.title('Comparison of Gating Variables and their Steady States')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()
