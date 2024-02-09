class Seat:
    """
    The Seat class represents a seat in a table.
    """

    def __init__(self):
        """
        Initializes a new instance of the Seat class.
        """
        self.free = True
        self.occupant = None

    def __str__(self):
        return f"Seat occupied by {self.occupant}" if not self.free else "Seat is free"

    def set_occupant(self, name: str):
        """
        Assigns the seat to a person if it's free and the person is not in the blacklist.

        :param name: The name of the person.
        """
        if self.free:
            self.occupant = name
            self.free = False

    def remove_occupant(self) -> str:
        """
        Removes the occupant from the seat and makes it free.

        :return: The name of the person who was occupying the seat.
        """
        occupant = self.occupant
        self.occupant = None
        self.free = True
        return occupant


class Table:
    """
    The Table class represents a table with a certain capacity.
    """

    def __init__(self, capacity):
        """
        Initializes a new instance of the Table class.

        Args:
            capacity (int): The capacity of the table.
        """
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    def __str__(self):
        return f"Table with capacity {self.capacity}, {self.left_capacity()} seats left"

    def has_free_spot(self) -> bool:
        """
        Checks if the table has a free spot.

        :return: True if there is a free spot, False otherwise.
        """
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name: str):
        """
        Assigns a seat to a person.

        :param name: The name of the person.
        """
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                break

    def left_capacity(self) -> int:
        """
        Returns the number of free spots in the table.

        :return: The number of free spots.
        """
        return sum(seat.free for seat in self.seats)

    def add_seat(self):
        """
        Adds a new seat to the table and increases its capacity by 1.
        """
        self.seats.append(Seat())
        self.capacity += 1

    def remove_occupant(self, name: str) -> bool:
        """
        Removes an occupant from the table.

        :param name: The name of the occupant to remove.
        :return: True if the occupant was removed, False otherwise.
        """
        for seat in self.seats:
            if seat.occupant == name:
                seat.remove_occupant()
                return True
        return False

    def to_dict(self):
        """
        Returns a dictionary representation of the Table object.
        """
        result = {
            "capacity": self.capacity,
            "seats": [
                {"free": seat.free, "occupant": seat.occupant} for seat in self.seats
            ],
        }
        return result
