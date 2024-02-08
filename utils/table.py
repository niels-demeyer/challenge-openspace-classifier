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
        self.whitelist = []
        self.blacklist = []

    def set_occupant(self, name):
        """
        Assigns the seat to a person if it's free and the person is not in the blacklist.

        Args:
            name (str): The name of the person.
        """
        if self.free:
            self.occupant = name
            self.free = False

    def remove_occupant(self):
        """
        Removes the occupant from the seat and makes it free.

        Returns:
            str: The name of the person who was occupying the seat.
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

    def has_free_spot(self):
        """
        Checks if the table has a free spot.

        Returns:
            bool: True if there is a free spot, False otherwise.
        """
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name):
        """
        Assigns a seat to a person.

        Args:
            name (str): The name of the person.
        """
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                break

    def left_capacity(self):
        """
        Returns the number of free spots in the table.

        Returns:
            int: The number of free spots.
        """
        return sum(seat.free for seat in self.seats)

    def add_seat(self):
        """
        Adds a new seat to the table and increases its capacity by 1.
        """
        self.seats.append(Seat())
        self.capacity += 1
    def remove_occupant(self, name):
        """
        Removes an occupant from the table.

        Args:
            name (str): The name of the occupant to remove.

        Returns:
            bool: True if the occupant was removed, False otherwise.
        """
        for seat in self.seats:
            if seat.occupant == name:
                seat.remove_occupant()
                return True
        return False