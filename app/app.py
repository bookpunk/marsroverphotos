"""Main file for Mars rover photos app."""
import os
import json
from app.input_data.input_data import InputData

def run():
    """Main execution for running the Mars rover photos module/app"""
    config_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = 'config.json'
    config_path = os.path.join(config_dir, config_file)
    with open(config_path) as infile:
        config = json.load(infile)

if __name__ == '__main__':
    """Entry point for Mars rover photos app."""
    run()
