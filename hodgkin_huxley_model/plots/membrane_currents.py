import matplotlib.pyplot as plt
from ..config import g_Na_bar, g_K_bar, g_L, E_Na, E_K, E_L

def plot_membrane_currents(sol):
    # Calculate the currents
    time_values = sol.t
    V_values = sol.y[0]  # Membrane potential
    m_values = sol.y[2]  # m gate variable
    h_values = sol.y[3]  # h gate variable
    n_values = sol.y[1]  # n gate variable

    # Calculate the currents
    I_Na_values = g_Na_bar * (m_values**3) * h_values * (V_values - E_Na)  # Sodium current
    I_K_values = g_K_bar * (n_values**4) * (V_values - E_K)  # Potassium current
    I_L_values = g_L * (V_values - E_L)  # Leak current

    # Filter for time values from 20 to 30 ms
    min_time = 20
    max_time = 30
    mask = (time_values >= min_time) & (time_values <= max_time)
    time_values_filtered = time_values[mask]
    I_Na_values_filtered = I_Na_values[mask]
    I_K_values_filtered = I_K_values[mask]
    I_L_values_filtered = I_L_values[mask]

    plt.figure(figsize=(8, 6))
    plt.plot(time_values_filtered, I_Na_values_filtered, label=r'$I_{Na}$', color='green')
    plt.plot(time_values_filtered, I_K_values_filtered, label=r'$I_{K}$', color='purple')
    plt.plot(time_values_filtered, I_L_values_filtered, label=r'$I_{L}$', color='red')
    plt.xlabel('Time (ms)')
    plt.ylabel('Current (mA/cm²)')
    plt.axhline(0, color='grey', lw=0.5, ls='--')
    plt.xlim(min_time, max_time)
    plt.ylim(-1000, 1000)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
