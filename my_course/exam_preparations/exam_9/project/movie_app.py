from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        if self.is_user_exist_by_name_and_age(username, age):
            raise Exception("User already exists!")

        current_user = User(username, age)
        self.users_collection.append(current_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        current_user = self.is_user_exist_by_name(username)

        if current_user is None:
            raise Exception("This user does not exist!")

        if not movie.owner == current_user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        current_user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        current_user = self.is_user_exist_by_name(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not movie.owner == current_user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            if key == 'title':
                movie.title = value
            elif key == 'year':
                movie.year = value
            elif key == 'age_restriction':
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        current_user = self.is_user_exist_by_name(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if not movie.owner == current_user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        current_user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        current_user = self.is_user_exist_by_name(username)

        if movie.owner == current_user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in current_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        current_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        current_user = self.is_user_exist_by_name(username)

        if movie not in current_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        current_user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        sorted_movies_collection = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        result = [m.details() for m in sorted_movies_collection]
        return '\n'.join(result)

    def __str__(self):
        result = 'All users: '
        if not self.users_collection:
            result += "No users."
        else:
            users = [u.username for u in self.users_collection]
            result += ', '.join(users)

        result += "\nAll movies: "
        if not self.movies_collection:
            result += 'No users.'
        else:
            movies = [m.title for m in self.movies_collection]
            result += ', '.join(movies)

        return result

    def is_user_exist_by_name(self, username):
        user = next((u for u in self.users_collection if u.username == username), None)
        return user

    def is_user_exist_by_name_and_age(self, username, age):
        user = next((u for u in self.users_collection if u.username == username and u.age == age), None)
        return user
