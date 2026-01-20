from networkx.readwrite.graph6 import data_to_n

from database.DB_connect import DBConnect
from model.artist import Artist
from model.connessione import Connessione
class DAO:

    @staticmethod
    def get_all_artists():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select a.id, a.name, (select count(album.id) 
                from album 
                where album.artist_id =a.id
                group by album.artist_id ) as num_album
                from artist a
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'],num_album=row["num_album"])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_edge():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select distinct artist.id , track.genre_id 
                from track, album, artist
                where track.album_id = album.id and album.artist_id = artist.id
                """
        cursor.execute(query)
        for row in cursor:
            connessione = Connessione(artist_id=row['id'], genre_id=row['genre_id'])
            result.append(connessione)
        cursor.close()
        conn.close()
        return result