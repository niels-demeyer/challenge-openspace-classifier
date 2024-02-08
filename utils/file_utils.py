def load_colleagues(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file]