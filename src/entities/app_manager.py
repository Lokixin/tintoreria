import inspect
import sys
import tkinter as tk

from config import APP_NAME
from static import styles
from use_cases import views
from use_cases.views import AddClient, AddCP, MainScreen


class ScreenManager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(APP_NAME)
        self.views_ = {}
        self.views_container = tk.Frame(self)
        self._setup_screen_container()
        self._add_views_to_screen_container()

    def show_frame(self, view_class: tk.Frame):
        frame = self.views_[view_class]
        frame.tkraise()

    def _setup_screen_container(self):
        self.views_container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
        )
        self.views_container.configure(background=styles.BACKGROUND)
        self.views_container.grid_columnconfigure(index=0, weight=1)
        self.views_container.rowconfigure(index=0, weight=1)

    def _add_views_to_screen_container(self):
        views_list = self._get_all_views()
        for View in views_list:
            _frame = View(self.views_container, self)
            self.views_[View] = _frame
            _frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.show_frame(AddClient)

    def _get_all_views(self):
        views_list = inspect.getmembers(sys.modules[views.__name__], inspect.isclass)
        views_list = [class_name[1] for class_name in views_list]
        return views_list
