class Movies:
    def __init__(self, movies=None):
        if movies is None:
            movies = []
        self.movies = movies

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def __init__(self, movies=None):
        if movies is None:
            movies = []
        super().__init__(movies)


    def add_movie(self, movie):
        self.movies.append(movie)
        print("Комедии:", self.movies)


class Drama(Movies):
    def __init__(self, movies=None):
        if movies is None:
            movies = []
        super().__init__(movies)

    def add_movie(self, movie):
        self.movies.append(movie)
        print("Драмы:", self.movies)


film1 = Comedy()
film1.add_movie('Большой куш')

film2 = Drama()
film2.add_movie('Оружейный барон')