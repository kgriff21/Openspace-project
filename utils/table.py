class Seat:
    """
    Initialize the seat class
    """
    def __init__(self) -> None:
        self.free: bool = True  # Indicating the seat is available (free).
        self.occupant: str = ""  # Initially empty because no one is seated.

    def __str__(self) -> str:
        return f"{self.occupant}, {self.free}"

    def set_occupant(self, name: str) -> (None):
        """
        Intended to place an occupant in the seat, changing occupant with the given name input.
        """
        self.free: bool = False
        self.occupant: str = name

    def remove_occupant(self,) -> (None):
        """
        This method removes the occupant from the seat and marks the seat free.
        """
        self.free: bool = True
        self.occupant: str = ""


class Table:
    """Creating a Table with Seats, instancized from the Seat() class. Need to create seat objects
    because each seat has it's own state and has to be managed independently, and each table has mulpitple seats."""

    # Initialize the Table class
    def __init__(self, capacity: int):
        self.capacity: int = capacity  # Capacity of seats at the table
        self.seats: list[Seat] = []  # Empty list to loop through 4 seats
        for i in range(self.capacity): # Loops through the amount of seats
            seat: Seat = Seat() # Creating new instance of Seat class for each seat at the table. each seat must be an independent object with its own state (whether it's free or occupied, and who the occupant is).
            self.seats.append(seat)

    def __str__(self) -> str:
        return f"{self.capacity}, {self.seats}"

    def has_free_spot(self) -> bool:
        """
        Checks if there are any free seats at the table.
        """
        for i in self.seats: # Looping through seat instances to check if they are free, returning True or False depending on state.
            if i.free:
                return True
        return False    

    def assign_seat(self, name: str) -> None:
        """
        Assigning occupant to a seat if the seat is free.
        Without break, the loop would continue, and the 
        person could potentially be assigned to multiple seats, which is not what you want. 
        """
        for i in self.seats: # Loop goes through each seat in self.seats
            if i.free: # Checking if the seat is free from the seat list [] initialized from the Table constructor
                i.set_occupant(name) # Assigns the occupant to the free seat
                break # Breaks/stops the loop because only want one seat assigned per person, so will stop after the first assignment.

    def left_capacity(self) -> int:
        """
        Check how many seats are left by looping through the seats, 
        seeing if it's free and adding to the counter if free = True.
        """
        left_capacity: int = 0
        for i in self.seats:
            if i.free:
                left_capacity += 1
        return left_capacity
