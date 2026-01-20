import flet as ft
from UI.view import View
from model.Model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        if self._view.txtNumAlbumMin.value <= 0:
            self._view.show_alert("inserire un valore per la drop down")
        if self._view.txtNumAlbumMin.value>0:
            self._model.build_graph(self._view.txtNumAlbumMin.value)

    def popola_dd(self):
        self._view.ddArtist.options.clear()
        lista=self._model._lista_artisti
        for elemento in lista:
            self._view.ddArtist.options.append(ft.dropdown.Option(elemento))
        self._view.update_page()

    def num_edges(self):
        return self._model.get_number_of_edge()
    def num_node(self):
        return self._model.get_number_of_node()

    def elementi_collegati(self,nodo):
        lista=self._model.artisti_collegati(self._view.ddArtist.option.value)
        for elemento in lista:
            self._view.txt_result.append(ft.Text(elemento))
        self._view.update_page()

    def handle_connected_artists(self, e):
        pass


