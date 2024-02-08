import pandas as pd

def load_colleagues(filepath):
    df = pd.read_excel(filepath)
    colleagues = []
    for _, row in df.iterrows():
        name = row['Name']
        whitelist = row['Whitelist'].split(',') if not pd.isna(row['Whitelist']) else []
        blacklist = row['Blacklist'].split(',') if not pd.isna(row['Blacklist']) else []
        colleagues.append((name, whitelist, blacklist))
    return colleagues