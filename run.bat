#!/bin/bash

# Ensure we're in the project root directory
cd "$(dirname "$0")"

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Run the simulation
python -m hodgkin_huxley_model.main

# Deactivate the virtual environment
deactivate
