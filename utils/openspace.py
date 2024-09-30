import random
from utils.table import Table
import pandas as pd


class OpenSpace:

    def __init__(self, number_of_tables: int = 6, seat_capacity: int = 4) -> None:
        self.tables: list[Table] = [] # Initialize an empty list for making tables
        self.number_of_tables: int = number_of_tables # Input from number of tables given as arguments in constructor
        for i in range(self.number_of_tables): # For the number of tables (6), will add the amount of seats (4) from the Table class
            self.tables.append(Table(seat_capacity))

    def __str__(self) -> str:
        return f"{self.tables}, {self.number_of_tables}"

    def organize(self, names: str) -> None:
        random.shuffle(names) # Takes names as argument in main.py which is the list of names from csv file.
        for table in self.tables: # Loops through the table list
            while table.has_free_spot(): # Checks if table has a free spot from the Table class and has_free_spot method
                if len(names) > 0: # If there are still names in the list to assign (>0)
                    table.assign_seat(names.pop()) # Removes the last name from the list .pop() and assigns the name to a seat
    
    def store(self, filename) -> None:
        """
       To make an exportable csv file, this can be done with pandas. pandas Dataframe takes in a dictionary, which is created
       by initializing a table counter to get the number for the table (up to 6), a seat counter to get which seat we're on,
       and name to set the occupant in that seat.
       A dataframe is created in the end from the dictionary. 
        """
        data : dict = {
            "Table": [],
            "Seat": [],
            "Name": []
        }
        table_counter : int = 0
        for table in self.tables:
            seat_counter : int = 0
            table_counter += 1
            for seat in table.seats:
                seat_counter += 1
                data['Table'].append(f"T{table_counter}")
                data['Seat'].append(f"S{seat_counter}")
                data['Name'].append(seat.occupant)
        df = pd.DataFrame(data=data)
        df.to_csv(filename, index=False)

    def display(self) -> None:
        table_counter : int = 0
        for table in self.tables:
            seat_counter : int = 0
            table_counter += 1
            print(f"Table {table_counter} :")
            for seat in table.seats:
                seat_counter += 1
                print(f"Seat {seat_counter} : {seat.occupant}")