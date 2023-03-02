import tkinter as tk

from static import styles


class MainScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        self.init_widgets()

    def init_widgets(self):
        tk.Label(
            self, text="Crea o realiza tests", justify=tk.CENTER, **styles.STYLE
        ).pack(**styles.PACK)


class AddCP(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        self.init_widgets()

    def init_widgets(self):
        tk.Label(
            self, text="Crea o realiza tests", justify=tk.CENTER, **styles.STYLE
        ).pack(**styles.PACK)