import random
from utils.table import Table
import pandas as pd


class OpenSpace:

    def __init__(self, number_of_tables: int = 6, seat_capacity: int = 4) -> None:
        self.tables: list[Table] = []
        self.number_of_tables: int = number_of_tables
        for i in range(self.number_of_tables):
            self.tables.append(Table(seat_capacity))

    def __str__(self) -> str:
        return f"{self.tables}, {self.number_of_tables}"

    def organize(self, names: str) -> None:
        random.shuffle(names)
        for table in self.tables:
            while table.has_free_spot():
                if len(names) > 0:
                    table.assign_seat(names.pop())
    
    def store(self, filename) -> None:
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

    