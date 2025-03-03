class Ticket:
    def __init__(self,ticket_code,cinema_name,cinema_city,movie_name,price,quantity,seat_initial,seat_number,):
        self.ticket_code = ticket_code
        self.cinema_name = cinema_name
        self.cinema_city = cinema_city
        self.movie_name = movie_name
        self.price = price
        self.quantity = quantity
        self.seat_initial = seat_initial
        self.seat_number = seat_number

    def __str__(self):
        return f"{self.ticket_code}\t{self.cinema_name}\t{self.cinema_city}\t{self.movie_name}\t{self.price}\t{self.quantity}\t{self.seat_initial}\t{self.seat_number}"