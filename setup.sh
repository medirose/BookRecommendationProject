#!/bin/bash

# Navigate to the project directory
cd /Users/medirose/Documents/GitHub/BookRecommendationProject

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install necessary packages
pip install streamlit pandas scikit-learn surprise matplotlib seaborn