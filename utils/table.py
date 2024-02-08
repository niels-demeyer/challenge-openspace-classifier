class Seat:
    def __init__(self):
        self.free = True
        self.occupant = None
        self.whitelist = []
        self.blacklist = []

    def set_occupant(self, name):
        if self.free and (not self.whitelist or name in self.whitelist) and name not in self.blacklist:
            self.occupant = name
            self.free = False

    def remove_occupant(self):
        occupant = self.occupant
        self.occupant = None
        self.free = True
        return occupant

    def set_whitelist(self, names):
        self.whitelist = names

    def set_blacklist(self, names):
        self.blacklist = names


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

    def add_seat(self):
        self.seats.append(Seat())
        self.capacity += 1