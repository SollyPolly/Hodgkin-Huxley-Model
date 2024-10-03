import matplotlib.pyplot as plt
from ..config import pulse_params

def plot_hodgkin_huxley_results(sol):
    plt.figure(figsize=(12, 6))

    # Plot the membrane potential
    plt.subplot(3, 1, 1)
    plt.plot(sol.t, sol.y[0], label='Membrane Potential (V)')
    plt.axhline(0, color='grey', lw=0.5, ls='--')
    plt.ylabel('Voltage (mV)')
    plt.title('Hodgkin-Huxley Neuron Model')
    plt.legend()

    # Plot the gating variables
    plt.subplot(3, 1, 2)
    plt.plot(sol.t, sol.y[1], label='n', color='orange')
    plt.plot(sol.t, sol.y[2], label='m', color='green')
    plt.plot(sol.t, sol.y[3], label='h', color='red')
    plt.ylabel('Gating Variables')
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

def step_current(t, start=pulse_params['start_time'], amplitude=pulse_params['pulse_amplitude'], pulse_duration=pulse_params['pulse_duration']):
    if pulse_duration is None:
        return amplitude if t >= start else 0
    else:
        return amplitude if start <= t < start + pulse_duration else 0
