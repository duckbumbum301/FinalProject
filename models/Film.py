class Film:
    def __init__(self, filmID, filmName, filmType, filmDuration, filmDescription, filmRating, director
                 , actor, releaseDate, filmImage, cusID, roomID, cinemaID, date, time, seatID
                 , number_of_seats, number_of_customers):
        self.filmID = filmID
        self.filmName = filmName
        self.filmType = filmType
        self.filmDuration = filmDuration
        self.filmDescription = filmDescription
        self.filmRating = filmRating
        self.filmImage = filmImage
        self.director = director
        self.actor = actor
        self.releaseDate = releaseDate
        self.cusID = cusID
        self.roomID = roomID
        self.cinemaID = cinemaID
        self.date = date
        self.time = time
        self.seatID = seatID
        self.number_of_seats = number_of_seats
        self.number_of_customers = number_of_customers
    def __str__(self):
        return (f'{self.filmID}\t{self.filmName}\t{self.filmType}\t{self.filmDescription}'
                f'\t{self.filmRating}\t{self.director}\t{self.actor}\t{self.releaseDate}'
                f'\t{self.date}\t{self.time}\t{self.number_of_seats}\t{self.number_of_customers}')
    def revenue(self):
        pass