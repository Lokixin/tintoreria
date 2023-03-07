import inspect
import sys
import tkinter as tk

from config import APP_NAME
from static import styles
from use_cases import views
from use_cases.views import AddClient, AddCP, MainScreen


class ScreenManager(tk.Tk):
    """
    Classe principal que conté i gestiona les diferents pantalles del projecte.
    Conté una referencia a totes les pantalles actives.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title(APP_NAME)
        self.views_ = {}
        self.views_container = tk.Frame(self)
        self._setup_screen_container()
        self._add_views_to_screen_container()

    def show_frame(self, view_class: tk.Frame) -> None:
        """Ubica el Frame indicat a sobre de tot.
        S'utilitza per canviar de pantalla.

        :param view_class:
        :return:
        """
        frame = self.views_[view_class]
        frame.tkraise()

    def _setup_screen_container(self):
        """Configura el Frame principal (el que contindrà la resta) per adaptar-se
        a la mida de la pantalla.

        :return:
        """
        # fill -> ocupa tant d'espai com sigui possible en la direcció establerta
        # expand -> distribueix l'espai disponible entre tots els elements amb expand=True
        self.views_container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
        )
        self.views_container.configure(
            background=styles.BACKGROUND
        )  # Canvi de color de fons
        # Distribuir el frame com una única columna i fila de la mateixa mida (un quadrat).
        # D'aquesta forma s'adapta a la mida de la finestra.
        # index: En quina posició de la graella s'ubica.
        # weight: Quina proporció de la graella ocupa.
        self.views_container.grid_columnconfigure(index=0, weight=1)
        self.views_container.rowconfigure(index=0, weight=1)

    def _add_views_to_screen_container(self):
        """Afegeix totes les pantalles definides al mòdul views
        al controlador de pantalles. Crea una instància de cada classe.

        :return:
        """
        views_list = self._get_all_views()
        for View in views_list:
            _frame = View(self.views_container, self)
            self.views_[View] = _frame
            _frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.show_frame(AddClient)

    def _get_all_views(self):
        """Inspecciona el mòdul 'views' i retorna totes les classes definides en aquest.

        :return:
        """
        views_list = inspect.getmembers(sys.modules[views.__name__], inspect.isclass)
        views_list = [class_name[1] for class_name in views_list]
        return views_list
