import json

def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

config = load_config()

# Model parameters
model_params = config['model_params']
g_L = model_params['g_L']
g_K_bar = model_params['g_K_bar']
g_Na_bar = model_params['g_Na_bar']
C_m = model_params['C_m']
E_L = model_params['E_L']
E_K = model_params['E_K']
E_Na = model_params['E_Na']

# Gate parameters
m_gate_params = config['m_gate_params']
h_gate_params = config['h_gate_params']
n_gate_params = config['n_gate_params']

# Simulation settings
simulation_settings = config['simulation_settings']
t_span = tuple(simulation_settings['t_span'])
num_points = simulation_settings['num_points']

# Initial conditions
initial_conditions = config['initial_conditions']


