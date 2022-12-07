import os, sys

def imports_from_relative():
    sys.path.append(sys.path[0])

def imports_from_above_one():
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

def imports_from_above_two():
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."))

def use_file(file: str = ""):
    return open(os.path.join(os.path.dirname(__file__), "..", file))

def resolve_path(path: str = ""):
    return str(os.path.join(os.path.dirname(os.path.abspath(__file__)), path))

def asset(path: str = ""):
    return str(os.path.join(os.getcwd(), "ground_station/graphical_interface/assets", path))
    
def use_path(path: str = ""):
    return str(os.path.join(os.getcwd(), path))
