"""Main file for Mars rover photos app."""
import os
import json
from app.input_data.input_data import InputData

def run():
    """Main execution for running the Mars rover photos module/app"""
    project_name = 'app'
    config_file = 'config.json'
    cwd = os.getcwd()
    config_path = os.path.join(cwd, project_name, config_file)
    with open(config_path) as infile:
        config = json.load(infile)

if __name__ == '__main__':
    """Entry point for Mars rover photos app."""
    run()
