import pandas as pd

def read_csv(file_path):
    # Leser inn CSV-filen og returnerer en liste av tuples
    df = pd.read_csv(file_path)
    return [(row['name'], row['lat'], row['lng']) for index, row in df.iterrows()]
