from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for al in self.albums:
            if al.name == album_name:
                if al.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(al)
                return f"Album {al.name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = [f'Band {self.name}']
        for al in self.albums:
            result.append(al.details())
        return '\n'.join(result)


