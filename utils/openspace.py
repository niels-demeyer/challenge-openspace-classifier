from .table import Table
import random

class Openspace:
    """
    The Openspace class represents an open space with a number of tables.
    Each table has a certain capacity.
    """

    def __init__(self, number_of_tables, table_capacity):
        """
        Initializes an Openspace with a given number of tables and table capacity.

        Args:
            number_of_tables (int): The number of tables in the open space.
            table_capacity (int): The capacity of each table.
        """
        self.tables = [Table(table_capacity) for _ in range(number_of_tables)]
        self.number_of_tables = number_of_tables

    def add_colleague(self, name):
        """
        Adds a colleague to the first available spot in the open space.

        Args:
            name (str): The name of the colleague.
        """
        for table in self.tables:
            if table.has_free_spot():
                table.assign_seat(name)
                return
    def remove_colleague(self, name):
        """
        Removes a colleague from the open space.

        Args:
            name (str): The name of the colleague to remove.
        """
        for table in self.tables:
            if table.remove_occupant(name):
                return

    def add_table(self, capacity):
        """
        Adds a table with a given capacity to the open space.

        Args:
            capacity (int): The capacity of the new table.
        """
        self.tables.append(Table(capacity))
        self.number_of_tables += 1

    def total_seats(self):
        """
        Returns the total number of seats in the open space.

        Returns:
            int: The total number of seats.
        """
        return sum(table.capacity for table in self.tables)

    def total_people(self):
        """
        Returns the total number of people in the open space.

        Returns:
            int: The total number of people.
        """
        return sum(not seat.free for table in self.tables for seat in table.seats)

    def remaining_seats(self):
        """
        Returns the number of remaining seats in the open space.

        Returns:
            int: The number of remaining seats.
        """
        return self.total_seats() - self.total_people()

    def display(self):
        """
        Prints the current state of the open space, including the number of each table
        and the occupants of each seat.
        """
        for i, table in enumerate(self.tables, 1):
            print(f"Table {i}:")
            for seat in table.seats:
                print(f"  Seat: {'Free' if seat.free else seat.occupant}")
    def check_capacity(self):
        """
        Checks the number of people and seats and prints a message accordingly.
        """
        total_people = self.total_people()
        total_seats = self.total_seats()

        if total_people > total_seats:
            print("Warning: There are more people than seats!")
        elif total_people < total_seats:
            print("Notice: There are more seats than people.")
        else:
            print("Just right: There are enough seats for everyone.")
    def organize(self, colleagues):
        """
        Organizes colleagues into tables. The colleagues are shuffled and then
        assigned to tables in the order they appear in the shuffled list.

        Args:
            colleagues (list): A list of colleague names.
        """
        random.shuffle(colleagues)
        for name in colleagues:
            if not self.is_colleague_in_openspace(name):
                for table in self.tables:
                    if table.has_free_spot():
                        table.assign_seat(name)
                        break

    def is_colleague_in_openspace(self, name):
        """
        Checks if a colleague is already in the open space.

        Args:
            name (str): The name of the colleague.

        Returns:
            bool: True if the colleague is in the open space, False otherwise.
        """
        for table in self.tables:
            for seat in table.seats:
                if seat.occupant == name:
                    return True
        return False