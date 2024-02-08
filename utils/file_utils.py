import pandas as pd

def load_colleagues(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    colleagues = []
    for line in lines:
        colleagues.append(line.strip().split(','))
    return colleagues