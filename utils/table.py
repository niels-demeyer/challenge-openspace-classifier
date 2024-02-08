class Seat:
    def __init__(self):
        self.free = True
        self.occupant = None

    def set_occupant(self, name):
        if self.free:
            self.occupant = name
            self.free = False

    def remove_occupant(self):
        occupant = self.occupant
        self.occupant = None
        self.free = True
        return occupant


class Table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    def has_free_spot(self):
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                break

    def left_capacity(self):
        return sum(seat.free for seat in self.seats)