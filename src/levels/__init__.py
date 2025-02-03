import importlib

def load_level(level_name):
    return importlib.import_module(f"levels.{level_name}")

