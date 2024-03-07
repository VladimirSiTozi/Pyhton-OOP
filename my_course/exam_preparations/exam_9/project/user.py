from typing import List


class User:

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: List = []
        self.movies_owned: List = []

    def __str__(self):
        result = [f"Username: {self.username}, Age: {self.age}", "Liked movies:"]
        if not self.movies_liked:
            result.append("No movies liked.")
        else:
            liked_movies = [m.details() for m in self.movies_liked]
            for m in liked_movies:
                result.append(m)

        result.append("Owned movies:")
        if not self.movies_owned:
            result.append("No movies owned.")
        else:
            owned_movies = [m.details() for m in self.movies_liked]
            for m in owned_movies:
                result.append(m)

        return '\n'.join(result)
