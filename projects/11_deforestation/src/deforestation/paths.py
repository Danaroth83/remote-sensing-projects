from pathlib import Path

def project():
    return Path(__file__).resolve().parents[2]
    
def data():
    return project() / "data"

def raw():
    return data() / "raw"

def outputs():
    return data() / "outputs"

def weights():
    return data() / "weights"

def source():
    return Path(__file__).resolve().parents[1]

def package():
    return Path(__file__).resolve().parent