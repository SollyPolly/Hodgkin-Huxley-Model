# To run this bad boy "python -m hodgkin_huxley_model.main" Make sure u are in \Project

from hodgkin_huxley_model.simulation import run_simulation
from hodgkin_huxley_model.plots import (
    plot_hodgkin_huxley_results,
    plot_steady_state_and_time_constants_dual_axis,
    plot_g_na_vs_time,
    plot_membrane_currents,
    plot_time_constant_comparison,
    plot_phase_diagram,
    plot_phase_diagram_fixed_gating
)
from hodgkin_huxley_model.config import initial_conditions


def main():
    sol = run_simulation()
    
    plot_hodgkin_huxley_results(sol)
    plot_steady_state_and_time_constants_dual_axis()
    plot_g_na_vs_time(sol)
    plot_membrane_currents(sol)
    plot_time_constant_comparison(sol)
    
    for gating_var_name in ['n', 'm', 'h']:
        plot_phase_diagram(sol, gating_var_name)
    
    plot_phase_diagram_fixed_gating(sol, gating_var_name='m', n0=initial_conditions['n0'], h0=initial_conditions['h0'])

if __name__ == "__main__":
    main()

