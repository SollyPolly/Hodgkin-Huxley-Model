# To run this bad boy "python -m hodgkin_huxley_model.main" Make sure u are in \Project

import matplotlib.pyplot as plt
from hodgkin_huxley_model.simulation import run_simulation
from hodgkin_huxley_model.config import initial_conditions

from hodgkin_huxley_model.plots.Full_Model import (
    plot_hodgkin_huxley_results,
    plot_steady_state_and_time_constants_dual_axis,
    plot_g_na_vs_time,
    plot_membrane_currents,
    plot_time_constant_comparison,
    plot_phase_diagram,
)

def main():
    hh_sol, V_M_hh_sol, V_H_hh_sol, V_N_hh_sol = run_simulation()
    
    # Entire System
    plot_hodgkin_huxley_results(hh_sol)
    plot_steady_state_and_time_constants_dual_axis()
    plot_g_na_vs_time(hh_sol)
    plot_membrane_currents(hh_sol)
    plot_time_constant_comparison(hh_sol)
    for gating_var in ['n', 'm', 'h']:
        plot_phase_diagram(hh_sol, gating_var)

    # V and M
    from hodgkin_huxley_model.plots.V_m import (
    plot_V_M_hodgkin_huxley_results,
    plot_phase_fixed_V_M,
    plot_phase_fixed_zoomed_V_M
    )

    #plot_V_M_hodgkin_huxley_results(V_M_hh_sol)
    plot_phase_fixed_V_M(V_M_hh_sol)
    plot_phase_fixed_zoomed_V_M(V_M_hh_sol)

    # V and h
    from hodgkin_huxley_model.plots.V_h import (
    plot_V_H_hodgkin_huxley_results,
    plot_phase_fixed_V_H,
    plot_phase_fixed_zoomed_V_H
    )

    #plot_V_H_hodgkin_huxley_results(V_H_hh_sol)
    plot_phase_fixed_V_H(V_H_hh_sol)
    plot_phase_fixed_zoomed_V_H(V_H_hh_sol)

    # V and n
    from hodgkin_huxley_model.plots.V_n import (
    plot_V_N_hodgkin_huxley_results,
    plot_phase_fixed_V_N,
    plot_phase_fixed_zoomed_V_N
    )

    #plot_V_N_hodgkin_huxley_results(V_N_hh_sol)
    plot_phase_fixed_V_N(V_N_hh_sol)
    plot_phase_fixed_zoomed_V_N(V_N_hh_sol)
    


if __name__ == "__main__":
    main()


