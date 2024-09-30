import pandas as pd


def read_names_from_csv(filepath):
    """Creates a list that contains all the colleagues names"""
    # Open new_colleagues.csv file, reading contents and appending each row to names list.
    df = pd.read_csv(filepath, header=None)  # Creating DataFrame
    print(f'This is the dataframe from pandas: {df}')
    # Iterating over the rows. i is row index, j is the data in the row (all columns)
    # Getting the information (name) from the 1st [0] column with the name
    names_list = [j[0] for i, j in df.iterrows()]
    print(f"This is the original names list from pandas: {names_list}")
    return names_list
