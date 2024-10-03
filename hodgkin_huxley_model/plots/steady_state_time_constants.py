import numpy as np
import matplotlib.pyplot as plt
from ..model import m_inf, h_inf, n_inf, tau_m, tau_h, tau_n

def plot_steady_state_and_time_constants_dual_axis():
    V_values = np.linspace(-80, 70, 500)

    m_inf_values = [m_inf(V) for V in V_values]
    h_inf_values = [h_inf(V) for V in V_values]
    n_inf_values = [n_inf(V) for V in V_values]

    tau_m_values = [tau_m(V) for V in V_values]
    tau_h_values = [tau_h(V) for V in V_values]
    tau_n_values = [tau_n(V) for V in V_values]

    plt.figure(figsize=(8, 8))

    # Plot for m_inf and tau_m with dual y-axis
    plt.subplot(3, 1, 1)
    ax1 = plt.gca()
    ax1.plot(V_values, m_inf_values, label=r'$m_\infty$ (Steady State)', color='green')
    ax1.set_ylabel(r'$m_\infty$ (Steady State) (ms)', color='green')
    ax1.set_ylim(0, 1.1)
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.plot(V_values, tau_m_values, label=r'$\tau_m$ (Time Constant)', color='blue', linestyle='--')
    ax2.set_ylabel(r'$\tau_m$ (Time Constant) (ms)', color='blue')
    ax2.set_ylim(0, 0.8)

    plt.title(r'Steady-State and Time Constant: $m_\infty$ and $\tau_m$')
    ax1.set_xlabel('Membrane Potential (mV)')

    # Plot for h_inf and tau_h with dual y-axis
    plt.subplot(3, 1, 2)
    ax1 = plt.gca()
    ax1.plot(V_values, h_inf_values, label=r'$h_\infty$ (Steady State)', color='red')
    ax1.set_ylabel(r'$h_\infty$ (Steady State)', color='red')
    ax1.set_ylim(0, 1.1)
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.plot(V_values, tau_h_values, label=r'$\tau_h$ (Time Constant)', color='blue', linestyle='--')
    ax2.set_ylabel(r'$\tau_h$ (Time Constant)', color='blue')
    ax2.set_ylim(0, 10)

    plt.title(r'Steady-State and Time Constant: $h_\infty$ and $\tau_h$')
    ax1.set_xlabel('Membrane Potential (mV)')

    # Plot for n_inf and tau_n with dual y-axis
    plt.subplot(3, 1, 3)
    ax1 = plt.gca()
    ax1.plot(V_values, n_inf_values, label=r'$n_\infty$ (Steady State)', color='orange')
    ax1.set_ylabel(r'$n_\infty$ (Steady State)', color='orange')
    ax1.set_ylim(0, 1.1)
    ax1.grid(True)

    ax2 = ax1.twinx()
    ax2.plot(V_values, tau_n_values, label=r'$\tau_n$ (Time Constant)', color='blue', linestyle='--')
    ax2.set_ylabel(r'$\tau_n$ (Time Constant)', color='blue')
    ax2.set_ylim(0, 6)

    plt.title(r'Steady-State and Time Constant: $n_\infty$ and $\tau_n$')
    ax1.set_xlabel('Membrane Potential (mV)')

    plt.tight_layout(pad=2)
    plt.show()
