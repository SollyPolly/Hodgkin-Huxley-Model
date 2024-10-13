import matplotlib.pyplot as plt
from ..model import step_current

def plot_simple_hodgkin_huxley_results(sol):
    plt.figure(figsize=(12, 6))

    # Plot the membrane potential
    plt.subplot(3, 1, 1)
    plt.plot(sol.t, sol.y[0], label='Membrane Potential (V)')
    plt.axhline(0, color='grey', lw=0.5, ls='--')
    plt.ylabel('Voltage (mV)')
    plt.title('Simple Hodgkin-Huxley Neuron Model')
    plt.legend()

    # Plot the gating variable
    plt.subplot(3, 1, 2)
    plt.plot(sol.t, sol.y[1], label='m', color='green')
    plt.ylabel('Gating Variable')
    plt.legend()

    # Plot the input current
    plt.subplot(3, 1, 3)
    input_current = [step_current(t) for t in sol.t]
    plt.plot(sol.t, input_current, label='Input Current', color='purple')
    plt.ylabel('Current (µA/cm²)')
    plt.xlabel('Time (ms)')
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    from ..simulation import run_simulation
    
    _, simple_hh_sol = run_simulation()
