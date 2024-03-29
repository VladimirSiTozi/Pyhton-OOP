from project.movie_specification.movie import Movie


class Action(Movie):
    def __init__(self, title: str, year: int, owner, age_restriction=12):
        super().__init__(title, year, owner, age_restriction)


    @Movie.age_restriction.setter
    def age_restriction(self, value):
        if value < 12:
            raise ValueError("Fantasy movies must be restricted for audience under 12 years!")
        self._Movie__age_restriction = value

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, " \
               f"Likes:{self.likes}, Owned by:{self.owner.username}"
