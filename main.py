# from utils.table import Seat
# from utils.openspace import Openspace

import csv

with open("new_colleagues.csv", newline="") as csv_file:
    contents = csv.reader(csv_file, delimiter=" ", quotechar="|")
    print(contents)
    names = []
    for row in contents:
        names.append(row)
    print(names)


class Seat:

    def __init__(self):
        self.free = True
        self.occupant = ""
    
    def set_occupant(self, name):
        self.free == False
        self.occupant = name

    def remove_occupant(self):
        self.free = True
        self.occupant = ""

class Table:

    def __init__(self):
        self.capacity = 4
        self.seats = []
        for i in range(self.capacity):
            seat = Seat()
            self.seats.append(seat)

    def has_free_spot(self):
        """
        Checks if there are any free seats at the table.
        """
        for i in self.seats:
            if i.free == True:
                return True
                break
    
    def assign_seat(self, name):
        for i in self.seats:
            i.set_occupant(name)
    
    def left_capacity(self):
        left_capacity = 0
        for i in self.seats:
            if i.free == True:
                left_capacity += 1


seat = Seat()
table = Table()
# openspace = Openspace()

print(table.capacity)

table.assign_seat("Erin")
print(table.seats[0].occupant)
print(table.left_capacity())


# names = list(range(0,25))
# list_seats = []
# for name in names:
#     seat = Seat()
#     seat.seat_occupant("Kelli")
#     list_seats.append(seat)
