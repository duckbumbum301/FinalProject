class Room:
    def __init__(self, roomID, roomName, cinemaID, seatID, filmID, cusID, number_of_seats, date, time, number_of_customers):
        self.roomID = roomID
        self.roomName = roomName
        self.cinemaID = cinemaID
        self.seatID = seatID
        self.filmID = filmID  #each filmID has its own date and time
        self.cusID = cusID
        self.number_of_seats = number_of_seats
        self.number_of_customers = number_of_customers
        self.date = date
        self.time = time
    def __str__(self):
        return f'{self.roomID}\t{self.roomName}\t{self.cinemaID}\t{self.number_of_seats}\t{self.date}\t{self.time}'