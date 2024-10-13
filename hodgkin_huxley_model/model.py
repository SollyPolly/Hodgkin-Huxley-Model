import numpy as np
from hodgkin_huxley_model.config import (
    g_L, g_K_bar, g_Na_bar, C_m, E_L, E_K, E_Na,
    m_gate_params, h_gate_params, n_gate_params
)
from .functions import apply_temperature_scaling
from .config import initial_conditions, simulation_settings

def calculate_gate_variables(V):
    A_m = apply_temperature_scaling(m_gate_params['alpha_m'] * (V - m_gate_params['V_am']) / (1 - np.exp(-(V - m_gate_params['V_am']) / m_gate_params['K_am'])))
    B_m = apply_temperature_scaling(m_gate_params['beta_m'] * np.exp(-(V - m_gate_params['V_bm']) / m_gate_params['K_bm']))
    A_h = apply_temperature_scaling(h_gate_params['alpha_h'] * np.exp(-(V - h_gate_params['V_ah']) / h_gate_params['K_ah']))
    B_h = apply_temperature_scaling(h_gate_params['beta_h'] / (1 + np.exp(-(V - h_gate_params['V_bh']) / h_gate_params['K_bh'])))
    A_n = apply_temperature_scaling(n_gate_params['alpha_n'] * (V - n_gate_params['V_an']) / (1 - np.exp(-(V - n_gate_params['V_an']) / n_gate_params['K_an'])))
    B_n = apply_temperature_scaling(n_gate_params['beta_n'] * np.exp(-(V - n_gate_params['V_bn']) / n_gate_params['K_bn']))
    return A_m, B_m, A_h, B_h, A_n, B_n

def calculate_steady_states(A, B):
    return A / (A + B)

def calculate_time_constants(A, B):
    return 1 / (A + B)

def m_inf(V):
    A_m, B_m, _, _, _, _ = calculate_gate_variables(V)
    return calculate_steady_states(A_m, B_m)

def h_inf(V):
    _, _, A_h, B_h, _, _ = calculate_gate_variables(V)
    return calculate_steady_states(A_h, B_h)

def n_inf(V):
    _, _, _, _, A_n, B_n = calculate_gate_variables(V)
    return calculate_steady_states(A_n, B_n)

def tau_m(V):
    A_m, B_m, _, _, _, _ = calculate_gate_variables(V)
    return calculate_time_constants(A_m, B_m)

def tau_h(V):
    _, _, A_h, B_h, _, _ = calculate_gate_variables(V)
    return calculate_time_constants(A_h, B_h)

def tau_n(V):
    _, _, _, _, A_n, B_n = calculate_gate_variables(V)
    return calculate_time_constants(A_n, B_n)

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

def simple_hodgkin_huxley(t, y, I, V0):
    V, m, = y
    V = np.clip(V, -100, 100)

    A_m, B_m, _, _, _, _ = calculate_gate_variables(V)
    
    m_inf_val = m_inf(V)
    h = h_inf(V0)
    n = n_inf(V0)

    tau_m_val = calculate_time_constants(A_m, B_m)

    dm_simple = (m_inf_val - m) / tau_m_val

    dV_simple = (I - (g_Na_bar * (m ** 3) * h * (V - E_Na) +
                g_K_bar * (n ** 4) * (V - E_K) +
                g_L * (V - E_L))) / C_m

    return [dV_simple, dm_simple]

def compute_derivatives(V, gating_var, gating_var_name, I_ext, n=None, h=None):
    V = np.clip(V, -100, 100)

    m_inf_val = m_inf(V)
    h_inf_val = h_inf(V)
    n_inf_val = n_inf(V)

    tau_m_val = tau_m(V)
    tau_h_val = tau_h(V)
    tau_n_val = tau_n(V)

    if n is None:
        n = n_inf_val
    if h is None:
        h = h_inf_val

    if gating_var_name == 'n':
        n = gating_var
        dn = (n_inf_val - n) / tau_n_val
        m = m_inf_val
        h = h_inf_val
    elif gating_var_name == 'm':
        m = gating_var
        dm = (m_inf_val - m) / tau_m_val
        n = n_inf_val
        h = h_inf_val
    elif gating_var_name == 'h':
        h = gating_var
        dh = (h_inf_val - h) / tau_h_val
        n = n_inf_val
        m = m_inf_val

    dV = (I_ext - (g_Na_bar * (m ** 3) * h * (V - E_Na) +
                   g_K_bar * (n ** 4) * (V - E_K) +
                   g_L * (V - E_L))) / C_m

    if gating_var_name == 'n':
        return dV, dn
    elif gating_var_name == 'm':
        return dV, dm
    elif gating_var_name == 'h':
        return dV, dh

def simple_calculate_derivatives(V, m, I_ext):
    _, _, _, _, _, _ = calculate_gate_variables(V)
    
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

def step_current(t):
    
    start = simulation_settings['start_time']
    amplitude = simulation_settings['pulse_amplitude']
    pulse_duration = simulation_settings['pulse_duration']
    
    if pulse_duration is None:
        return np.where(t >= start, amplitude, 0)
    else:
        return np.where((t >= start) & (t < start + pulse_duration), amplitude, 0)
    