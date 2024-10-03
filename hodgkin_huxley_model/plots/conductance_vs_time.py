import matplotlib.pyplot as plt
from ..config import g_Na_bar, g_K_bar

def plot_g_na_vs_time(sol):
    time_values = sol.t
    m_values = sol.y[2]
    h_values = sol.y[3]
    n_values = sol.y[1]

    g_Na_values = g_Na_bar * (m_values ** 3) * h_values
    g_K_values = g_K_bar * (n_values ** 4)

    min_time, max_time = 20, 30
    mask = (time_values >= min_time) & (time_values <= max_time)
    time_values_filtered = time_values[mask]
    g_Na_values_filtered = g_Na_values[mask]
    g_K_values_filtered = g_K_values[mask]

    plt.figure(figsize=(10, 6))
    plt.plot(time_values_filtered, g_Na_values_filtered, label=r'$g_{Na}(t) = g_{Na} \cdot m^3 \cdot h$', color='green')
    plt.plot(time_values_filtered, g_K_values_filtered, label=r'$g_{K}(t) = g_{K} \cdot n^4$', color='purple')
    plt.axhline(0, color='grey', lw=0.5, ls='--')
    plt.xlabel('Time (ms)')
    plt.ylabel('Conductance (mS/cm²)')
    plt.title(r'Plot of $g_{Na}(t)$ and $g_{K}(t)$ vs. Time')
    plt.xlim(min_time, max_time)
    plt.ylim(0, 40)
    plt.grid(True)
    plt.legend()
    plt.show()
