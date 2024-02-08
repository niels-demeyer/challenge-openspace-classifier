import pandas as pd
import random
class Office:
    def __init__(self, tables=6, seats_per_table=4):
        self.tables = {i: [] for i in range(1, tables+1)}
        self.seats_per_table = seats_per_table
        self.total_seats = tables * seats_per_table
        self.colleagues = []

    def load_colleagues(self, filepath):
        with open(filepath, 'r') as file:
            self.colleagues = [line.strip() for line in file]

    def assign_seats(self):
        if len(self.colleagues) > self.total_seats:
            print("Too many people for the available seats.")
            return

        random.shuffle(self.colleagues)
        for i, colleague in enumerate(self.colleagues):
            self.tables[(i % len(self.tables)) + 1].append(colleague)

    def remaining_seats(self):
        return self.total_seats - len(self.colleagues)

    def print_assignment(self):
        for table, colleagues in self.tables.items():
            print(f"Table {table}: {', '.join(colleagues)}")

# Usage
office = Office()
office.load_colleagues('new_colleagues.txt')
office.assign_seats()
office.print_assignment()
print(f"Remaining seats: {office.remaining_seats()}")