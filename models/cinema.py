class Cinema:
    def __init__(self, cinema_code, cinema_name, cinema_city):
        self.cinema_code = cinema_code
        self.cinema_name = cinema_name
        self.cinema_city = cinema_city

    def __str__(self):
        return f"{self.cinema_code}\t{self.cinema_name}\t{self.cinema_city}"
