#!/bin/bash

echo " AVAST !!  [BADBUOY SETUP] Initializing environment..."

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Upgrade pip and install dependencies
echo "Installing packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. To activate later:"
echo "    source .venv/bin/activate"
