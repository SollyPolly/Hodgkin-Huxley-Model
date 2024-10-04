from .config import config

# Temperature parameters
temperature_params = config['temperature_params']
base_temperature = temperature_params['base_temperature']
Q10 = temperature_params['Q10']
simulation_temperature = temperature_params['simulation_temperature']

def calculate_temperature_scale():
    # Calculate the temperature scaling factor
    return Q10 ** ((simulation_temperature - base_temperature) / 10)

def apply_temperature_scaling(rate_constant):
    # Apply temperature scaling to a rate constant.
    return rate_constant * calculate_temperature_scale()

# Example usage:
# scaled_alpha_m = apply_temperature_scaling(original_alpha_m)
# scaled_beta_m = apply_temperature_scaling(original_beta_m)
