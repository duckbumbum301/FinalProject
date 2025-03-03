class Movie:
    def __init__(self, movie_code, movie_name, movie_genre, movie_duration):
        self.movie_code = movie_code
        self.movie_name = movie_name
        self.movie_genre = movie_genre
        self.movie_duration = movie_duration

    def __str__(self):
        return f"{self.movie_code}\t{self.movie_name}\t{self.movie_genre}\t{self.movie_duration}"
