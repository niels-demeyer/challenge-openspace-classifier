import pandas as pd
import json

def load_colleagues(filepath):
    """
    This function reads a text file where each line represents a colleague.
    Each line is split on commas and added to a list.
    The function returns a list of lists, where each inner list represents a colleague.

    Args:
        filepath (str): The path to the text file.

    Returns:
        list: A list of lists, where each inner list represents a colleague.
    """
    with open(filepath, 'r') as file:
        lines = file.readlines()
    colleagues = []
    for line in lines:
        colleagues.append(line.strip().split(','))
    return colleagues

def load_json(filepath):
    """
    This function reads a JSON file and returns a dictionary.

    Args:
        filepath (str): The path to the JSON file.

    Returns:
        dict: A dictionary with the data from the JSON file.
    """
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data