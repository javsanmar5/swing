import os
import glob

def load_levels(directory="src/levels"):
    levels = {}
    for filepath in glob.glob(os.path.join(directory, "*.txt")):
        with open(filepath, "r") as file:
            level_layout = [line.rstrip("\n") for line in file if line.strip()]
        filename = os.path.splitext(os.path.basename(filepath))[0]
        level_name = filename.capitalize()   
        levels[level_name] = level_layout
    return dict(sorted(levels.items())) 

