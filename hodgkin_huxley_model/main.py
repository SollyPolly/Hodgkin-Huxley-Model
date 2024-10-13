# To run this bad boy "python -m hodgkin_huxley_model.main" Make sure u are in \Project

from hodgkin_huxley_model.simulation import run_simulation
from hodgkin_huxley_model.plots import (
    plot_hodgkin_huxley_results,
    plot_simple_hodgkin_huxley_results,
    plot_steady_state_and_time_constants_dual_axis,
    plot_g_na_vs_time,
    plot_membrane_currents,
    plot_time_constant_comparison,
    plot_phase_fixed_diagram,
    plot_phase_diagram,
    plot_phase_fixed_zoomed,
    

)
from hodgkin_huxley_model.config import initial_conditions
import matplotlib.pyplot as plt


def main():
    hh_sol, simple_hh_sol = run_simulation()
    
    plot_hodgkin_huxley_results(hh_sol)
    #plot_simple_hodgkin_huxley_results(simple_hh_sol)
    #plot_steady_state_and_time_constants_dual_axis()
    #plot_g_na_vs_time(hh_sol)
    #plot_membrane_currents(hh_sol)
    #plot_time_constant_comparison(hh_sol)
    #plot_phase_fixed_diagram(simple_hh_sol)
    #plot_phase_fixed_zoomed(simple_hh_sol)



    for gating_var in ['n', 'm', 'h']:
        plot_phase_diagram(hh_sol, gating_var)

    
if __name__ == "__main__":
    main()

