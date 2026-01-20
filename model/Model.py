import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self._mappa_artisti={}
        self._lista_artisti=[]
        self.load_all_artists()
        self.lista_collegamenti=[]

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        for elemento in self._artists_list:
            self._mappa_artisti[elemento.id] = elemento
            self._lista_artisti.append(elemento)

    def load_artists_with_min_albums(self, min_albums):
        pass

    def build_graph(self,n):

        for artista in self._artists_list:
            if artista.num_album is not None:
                if artista.num_album>n:
                    self._graph.add_node(artista)
        collegamento=DAO.get_all_edge()  #collegamento artista -> genere

        for elemento in collegamento:
            for elemento2 in collegamento:
                if elemento.genre_id==elemento2.genre_id:
                    self.lista_collegamenti.append((elemento.artist_id, elemento2.artist_id))
        print(self.lista_collegamenti)

        for elemento in self.lista_collegamenti:
            self._graph.add_edge( self._mappa_artisti[elemento[0]],  self._mappa_artisti[elemento[1]])
        for elemento in self._graph.edges:
            print (elemento)
        return self._graph

    def artisti_collegati(self, nodo):
        return list(self._graph.nodes_connected_component(nodo))

    def get_number_of_edge(self):
        return self._graph.number_of_edges()
    def get_number_of_node(self):
        return self._graph.number_of_nodes()

