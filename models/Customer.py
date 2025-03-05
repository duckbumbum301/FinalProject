class Customer:
    def __init__(self, ID, name, email, phone_number, filmID, roomID, cinemaID, date, time, price, seatID):
        self.cusID = ID
        self.cusName = name
        self.email = email
        self.phone_number = phone_number
        self.filmID = filmID
        self.roomID = roomID
        self.cinemaID = cinemaID
        self.date = date
        self.time = time
        self.price = price
        self.seatID = seatID
    def __str__(self):
        return (f"{self.cusID}\t{self.cusName}\t{self.email}\t{self.phone_number}"
                f"\t{self.filmID}\t{self.roomID}\t{self.cinemaID}\t{self.date}"
                f"\t{self.time}\t{self.price}\t{self.seatID}")
    def price(self):
        return 80000