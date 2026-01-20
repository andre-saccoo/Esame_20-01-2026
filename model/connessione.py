

from dataclasses import dataclass

@dataclass
class Connessione:
    artist_id : int
    genre_id : int

    def __str__(self):
        return f"{self.artist_id}, {self.genre_id}"

    def __hash__(self):
        return hash(self.artist_id)