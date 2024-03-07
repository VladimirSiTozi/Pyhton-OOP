from project.movie_specification.movie import Movie


class Thriller(Movie):
    def __init__(self, title: str, year: int, owner, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)


    @Movie.age_restriction.setter
    def age_restriction(self, value):
        if value < 16:
            raise ValueError("Fantasy movies must be restricted for audience under 16 years!")
        self._Movie__age_restriction = value

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"
