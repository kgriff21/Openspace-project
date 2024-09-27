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
    """"""

    # Initialize the Table class
    def __init__(self, capacity: int):
        self.capacity: int = capacity  # Capacity of seats at the table
        self.seats: list[Seat] = []  # Empty list to loop through 4 seats
        for i in range(self.capacity):
            seat: Seat = Seat()
            self.seats.append(seat)

    def __str__(self) -> str:
        return f"{self.capacity}, {self.seats}"

    def has_free_spot(self) -> bool:
        """
        Checks if there are any free seats at the table.
        """
        for i in self.seats:
            if i.free:
                return True
        return False    

    def assign_seat(self, name: str) -> None:
        for i in self.seats:
            if i.free:
                i.set_occupant(name)
                break

    def left_capacity(self) -> int:
        left_capacity: int = 0
        for i in self.seats:
            if i.free:
                left_capacity += 1
        return left_capacity
