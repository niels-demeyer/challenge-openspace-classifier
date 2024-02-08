from .table import Table
import random

class Openspace:
    def __init__(self, number_of_tables, table_capacity):
        self.tables = [Table(table_capacity) for _ in range(number_of_tables)]
        self.number_of_tables = number_of_tables

    def organize(self, colleagues):
        random.shuffle(colleagues)
        for name, whitelist, blacklist in colleagues:
            for table in self.tables:
                if table.has_free_spot():
                    for seat in table.seats:
                        if seat.free:
                            seat.set_whitelist(whitelist)
                            seat.set_blacklist(blacklist)
                            seat.set_occupant(name)
                            break

    def add_colleague(self, name):
        for table in self.tables:
            if table.has_free_spot():
                table.assign_seat(name)
                return
        print("No free spot available.")

    def add_table(self, capacity):
        self.tables.append(Table(capacity))
        self.number_of_tables += 1

    def total_seats(self):
        return sum(table.capacity for table in self.tables)

    def total_people(self):
        return sum(not seat.free for table in self.tables for seat in table.seats)

    def remaining_seats(self):
        return self.total_seats() - self.total_people()

    def display(self):
        for i, table in enumerate(self.tables, 1):
            print(f"Table {i}:")
            for seat in table.seats:
                print(f"  Seat: {'Free' if seat.free else seat.occupant}")