import tkinter as tk
from tkinter import ttk

from adapters.postal_code_adapter import get_locality_by_cp
from static import styles


class MainScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        self.init_widgets()

    def init_widgets(self):
        tk.Label(self, text="Hola Hola", justify=tk.CENTER, **styles.STYLE).pack(
            **styles.PACK
        )


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
        tk.Button(
            self,
            text="<- Afegir Client",
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT,
            command=lambda: self.manager.show_frame(AddClient),
            **styles.STYLE,
        ).pack(**styles.PACK)
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


class AddClient(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.clients_table = None
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        self.name_var = tk.StringVar(self)
        self.surname_var = tk.StringVar(self)
        self.phone_var = tk.StringVar(self)
        self.table_columns = ["name", "surname", "phone"]
        self.init_widgets()

    def save_new_client(self):
        name = self.name_var.get()
        surname = self.surname_var.get()
        phone = self.phone_var.get()
        self.clients_table.insert("", tk.END, values=(name, surname, phone))
        self.clients_table.update()
        print(f"Nou client: {name=} - {surname=} - {phone=}")

    def init_widgets(self):
        tk.Label(
            self, text="Aquí añadiremos clientes", justify=tk.CENTER, **styles.STYLE
        ).pack(**styles.PACK)

        form_frame = tk.Frame(self)
        form_frame.configure(background=styles.BACKGROUND)
        form_frame.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=5,
            pady=5,
        )
        form_frame.grid_columnconfigure(index=1, weight=3)
        form_frame.rowconfigure(index=0, weight=1)

        tk.Label(form_frame, text="Nom: ", justify=tk.CENTER, **styles.STYLE).grid(
            column=0,
            row=0,
            padx=5,
            pady=5,
            sticky=tk.EW,
        )

        tk.Entry(
            form_frame, textvariable=self.name_var, justify=tk.CENTER, **styles.STYLE
        ).grid(
            column=1,
            row=0,
            padx=5,
            pady=5,
            sticky=tk.EW,
        )

        tk.Label(form_frame, text="Cognom: ", justify=tk.CENTER, **styles.STYLE).grid(
            column=0,
            row=1,
            padx=5,
            pady=5,
            sticky=tk.EW,
        )

        tk.Entry(
            form_frame, textvariable=self.surname_var, justify=tk.CENTER, **styles.STYLE
        ).grid(
            column=1,
            row=1,
            padx=5,
            pady=5,
            sticky=tk.EW,
        )

        tk.Label(form_frame, text="Telèfon: ", justify=tk.CENTER, **styles.STYLE).grid(
            column=0,
            row=2,
            padx=5,
            pady=5,
            sticky=tk.EW,
        )

        tk.Entry(
            form_frame, textvariable=self.phone_var, justify=tk.CENTER, **styles.STYLE
        ).grid(
            column=1,
            row=2,
            padx=5,
            pady=5,
            sticky=tk.EW,
        )

        tk.Button(
            self,
            text="Guardar client",
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT,
            command=self.save_new_client,
            **styles.STYLE,
        ).pack(**styles.PACK)

        self.clients_table = ttk.Treeview(
            self, columns=self.table_columns, show="headings"
        )
        self.clients_table.heading("name", text="Nom")
        self.clients_table.heading("surname", text="Cognom")
        self.clients_table.heading("phone", text="Telèfon")

        fake_clients = [
            ("Dimas", "Ávila", "610880930"),
            ("Marc", "García", "689743561"),
        ]
        [
            self.clients_table.insert("", tk.END, values=client)
            for client in fake_clients
        ]
        self.clients_table.pack(**styles.PACK)

        tk.Button(
            self,
            text="Afegir codi postal ->",
            relief=tk.FLAT,
            activebackground=styles.BACKGROUND,
            activeforeground=styles.TEXT,
            command=lambda: self.manager.show_frame(AddCP),
            **styles.STYLE,
        ).pack(**styles.PACK)
