import numpy as np
from hodgkin_huxley_model.config import (
    g_L, g_K_bar, g_Na_bar, C_m, E_L, E_K, E_Na,
    m_gate_params, h_gate_params, n_gate_params
)
from .functions import (
    m_inf, h_inf, n_inf, tau_m, tau_h, tau_n,
    calculate_gate_variables,
    calculate_time_constants
)
from .config import initial_conditions, simulation_settings

def hodgkin_huxley(t, y, I):
    V, n, m, h = y
    V = np.clip(V, -100, 100)

    A_m, B_m, A_h, B_h, A_n, B_n = calculate_gate_variables(V)
    
    m_inf_val = m_inf(V)
    h_inf_val = h_inf(V)
    n_inf_val = n_inf(V)

    tau_m_val = calculate_time_constants(A_m, B_m)
    tau_h_val = calculate_time_constants(A_h, B_h)
    tau_n_val = calculate_time_constants(A_n, B_n)

    dm = (m_inf_val - m) / tau_m_val
    dh = (h_inf_val - h) / tau_h_val
    dn = (n_inf_val - n) / tau_n_val

    dV = (I - (g_Na_bar * (m ** 3) * h * (V - E_Na) +
                g_K_bar * (n ** 4) * (V - E_K) +
                g_L * (V - E_L))) / C_m

    return [dV, dn, dm, dh]

def common_calculations(V, V0):
        V = np.clip(V, -100, 100)
        m = m_inf(V0)
        h = h_inf(V0)
        n = n_inf(V0)
        return V, m, h, n

def calculate_dV(V, m, h, n, I):
        return (I - (g_Na_bar * (m ** 3) * h * (V - E_Na) +
                g_K_bar * (n ** 4) * (V - E_K) +
                g_L * (V - E_L))) / C_m

def V_m_hodgkin_huxley(t, y, I, V0):
        V, m = y
        V, _, h, n = common_calculations(V, V0)
        A_m, B_m, _, _, _, _ = calculate_gate_variables(V)
        m_inf_val = m_inf(V)
        tau_m_val = calculate_time_constants(A_m, B_m)
        dm_simple = (m_inf_val - m) / tau_m_val
        dV_simple = calculate_dV(V, m, h, n, I)
        return [dV_simple, dm_simple]

def V_n_hodgkin_huxley(t, y, I, V0):
        V, n = y
        V, m, h, _ = common_calculations(V, V0)
        _, _, _, _, A_n, B_n = calculate_gate_variables(V)
        n_inf_val = n_inf(V)
        tau_n_val = calculate_time_constants(A_n, B_n)
        dn_simple = (n_inf_val - n) / tau_n_val
        dV_simple = calculate_dV(V, m, h, n, I)
        return [dV_simple, dn_simple]

def V_h_hodgkin_huxley(t, y, I, V0):
        V, h = y
        V, m, _, n = common_calculations(V, V0)
        _, _, A_h, B_h, _, _ = calculate_gate_variables(V)
        h_inf_val = h_inf(V)
        tau_h_val = calculate_time_constants(A_h, B_h)
        dh_simple = (h_inf_val - h) / tau_h_val
        dV_simple = calculate_dV(V, m, h, n, I)
        return [dV_simple, dh_simple]

def V_m_calculate_derivatives(V, m, I_ext):

    V0 = initial_conditions['V0']

    m_inf_val = m_inf(V)
    tau_m_val = tau_m(V)

    h = h_inf(V0)
    n = n_inf(V0)

    dm_simple = (m_inf_val - m) / tau_m_val
    dV_simple = (I_ext - (g_Na_bar * (m ** 3) * h * (V - E_Na) +
                g_K_bar * (n ** 4) * (V - E_K) +
                g_L * (V - E_L))) / C_m

    return dV_simple, dm_simple

def V_h_calculate_derivatives(V, h, I_ext):

    V0 = initial_conditions['V0']

    h_inf_val = h_inf(V)
    tau_h_val = tau_h(V)

    m = m_inf(V0)
    n = n_inf(V0)

    dh_simple = (h_inf_val - h) / tau_h_val
    dV_simple = (I_ext - (g_Na_bar * (m ** 3) * h * (V - E_Na) +
                g_K_bar * (n ** 4) * (V - E_K) +
                g_L * (V - E_L))) / C_m

    return dV_simple, dh_simple

def V_n_calculate_derivatives(V, n, I_ext):

    V0 = initial_conditions['V0']

    n_inf_val = n_inf(V)
    tau_n_val = tau_n(V)

    m = m_inf(V0)
    h = h_inf(V0)

    dn_simple = (n_inf_val - h) / tau_n_val
    dV_simple = (I_ext - (g_Na_bar * (m ** 3) * h * (V - E_Na) +
                g_K_bar * (n ** 4) * (V - E_K) +
                g_L * (V - E_L))) / C_m

    return dV_simple, dn_simple
    