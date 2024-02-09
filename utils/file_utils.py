import pandas as pd
import json


def load_colleagues(filepath: str) -> list:
    """
    Function that reads a text file where each line represents a colleague.
    Each line is split on commas and added to a list.
    The function returns a list of lists, where each inner list represents a colleague.

    :param filepath: A string that represents the path to the text file.
    :return: A list of lists, where each inner list represents a colleague.
    """
    with open(filepath, "r") as file:
        lines = file.readlines()
    colleagues = []
    for line in lines:
        colleagues.append(line.strip().split(","))
    return colleagues


def load_json(filepath: str) -> dict:
    """
    Function that reads a JSON file and returns a dictionary.

    :param filepath: A string that represents the path to the JSON file.
    :return: A dictionary with the data from the JSON file.
    """
    with open(filepath, "r") as file:
        data = json.load(file)
    return data


def save_to_json(data: dict, filepath: str):
    """
    Function that writes a dictionary to a JSON file.

    :param data: A dictionary with the data to be written to the JSON file.
    :param filepath: A string that represents the path to the JSON file.
    """
    with open(filepath, "w") as file:
        json.dump(data, file)
