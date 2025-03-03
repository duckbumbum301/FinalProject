class Seat:
    def __init__(self, seat_initial, seat_number):
        self.seat_initial = seat_initial
        self.seat_number = seat_number

    def __str__(self):
        return f"{self.seat_initial}\t{self.seat_number}"
