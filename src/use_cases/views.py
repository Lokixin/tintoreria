import tkinter as tk

from adapters.postal_code_adapter import get_locality_by_cp
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
    def __init__(self, parent, manager) -> None:
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        self.postal_code = tk.StringVar(self)
        self.locality = tk.StringVar(self)
        self.postal_code.trace("w", self.update_locality)
        self.init_widgets()

    def init_widgets(self) -> None:
        tk.Label(
            master=self, text="Guardar Codi Postal", justify=tk.CENTER, **styles.STYLE
        ).pack(**styles.PACK)

        tk.Label(
            master=self,
            text="Introdueix el Codi Postal:",
            justify=tk.CENTER,
            **styles.STYLE,
        ).pack(**styles.PACK)
        tk.Entry(
            self, textvariable=self.postal_code, justify=tk.CENTER, **styles.STYLE
        ).pack(**styles.PACK)

        tk.Label(
            master=self,
            text="Introdueix la localitat:",
            justify=tk.CENTER,
            **styles.STYLE,
        ).pack(**styles.PACK)
        tk.Entry(
            self, textvariable=self.locality, justify=tk.CENTER, **styles.STYLE
        ).pack(**styles.PACK)

        tk.Button(
            self,
            text="Guardar",
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT,
            command=self.save_new_postal_code,
            **styles.STYLE,
        ).pack(**styles.PACK)

    def save_new_postal_code(self) -> None:
        """
        This is a dummy implementation
        """
        postal_code = self.postal_code.get()
        locality = self.locality.get()
        print(f"{postal_code=} - {locality=}")

    def update_locality(self, *args) -> None:
        locality = get_locality_by_cp(cp=self.postal_code.get())
        self.locality.set(locality)
