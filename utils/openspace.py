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

    def __str__(self):
        return f"Openspace with {self.number_of_tables} tables and {self.total_seats()} total seats."

    def add_colleague(self, name: str):
        """
        Adds a colleague to the first available spot in the open space.

        :param name: The name of the colleague.
        """
        for table in self.tables:
            if table.has_free_spot():
                table.assign_seat(name)
                return

    def remove_colleague(self, name: str):
        """
        Removes a colleague from the open space.

        :param name: The name of the colleague to remove.
        """
        for table in self.tables:
            if table.remove_occupant(name):
                return

    def add_table(self, capacity: int):
        """
        Adds a table with a given capacity to the open space.

        :param capacity: The capacity of the new table.
        """
        self.tables.append(Table(capacity))
        self.number_of_tables += 1

    def total_seats(self) -> int:
        """
        Returns the total number of seats in the open space.

        :return: The total number of seats.
        """
        return sum(table.capacity for table in self.tables)

    def total_people(self) -> int:
        """
        Returns the total number of people in the open space.

        :return: The total number of people.
        """
        return sum(not seat.free for table in self.tables for seat in table.seats)

    def remaining_seats(self) -> int:
        """
        Returns the number of remaining seats in the open space.

        :return: The number of remaining seats.
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

    def organize(self, colleagues: list):
        """
        Organizes colleagues into tables. The colleagues are shuffled and then
        assigned to tables in the order they appear in the shuffled list.

        :param colleagues: A list of colleague names.
        """
        random.shuffle(colleagues)
        for name in colleagues:
            if not self.is_colleague_in_openspace(name):
                for table in self.tables:
                    if table.has_free_spot():
                        table.assign_seat(name)
                        break
        # Redistribute colleagues after adding all of them
        self.redistribute_colleagues()

    def is_colleague_in_openspace(self, name: str) -> bool:
        """
        Checks if a colleague is already in the open space.

        :param name: The name of the colleague.
        :return: True if the colleague is in the open space, False otherwise.
        """
        for table in self.tables:
            for seat in table.seats:
                if seat.occupant == name:
                    return True
        return False

    def redistribute_colleagues(self):
        """
        Redistributes colleagues to ensure that no table has only one person.
        """
        # Find all tables with only one person
        tables_with_one_person = [
            table
            for table in self.tables
            if table.left_capacity() == table.capacity - 1 and table.capacity > 1
        ]

        # If there are no tables with only one person, return
        if not tables_with_one_person:
            return

        # For each table with only one person
        for table_with_one_person in tables_with_one_person:
            # Find a table with more than one person
            for table in self.tables:
                if table.left_capacity() < table.capacity - 1:
                    # Find a person in the table
                    for seat in table.seats:
                        if not seat.free:
                            # Remove the person from the table
                            person_to_move = seat.remove_occupant()
                            # Add the person to the table with only one person
                            table_with_one_person.assign_seat(person_to_move)
                            break
                    # If a person was moved, break the loop
                    if person_to_move:
                        break
