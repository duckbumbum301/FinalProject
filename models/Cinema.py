class Cinema:
    def __init__(self, cinemaID, cinemaName, address, roomID, seatID, filmID, cusID, orderID
                 , number_of_customers, number_of_films, number_of_seats, number_of_rooms
                 , number_of_orders):
        self.cinemaID = cinemaID
        self.cinemaName = cinemaName
        self.address = address
        self.roomID = roomID
        self.seatID = seatID
        self.filmID = filmID
        self.cusID = cusID
        self.orderID = orderID
        self.number_of_customers = number_of_customers
        self.number_of_films = number_of_films
        self.number_of_seats = number_of_seats
        self.number_of_rooms = number_of_rooms
        self.number_of_orders = number_of_orders
    def __str__(self):
        return f'{self.cinemaID}\t{self.cinemaName}\t{self.address}'
    def revenue(self):
        pass