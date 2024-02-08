from .table import Table
import random

class Openspace:
    def __init__(self, number_of_tables, table_capacity):
        self.tables = [Table(table_capacity) for _ in range(number_of_tables)]
        self.number_of_tables = number_of_tables

    def organize(self, names):
        random.shuffle(names)
        for name in names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break

    def display(self):
        for i, table in enumerate(self.tables, 1):
            print(f"Table {i}:")
            for seat in table.seats:
                print(f"  Seat: {'Free' if seat.free else seat.occupant}")

    def store(self, filename):
        # Implement storing the repartition in an excel file
        pass