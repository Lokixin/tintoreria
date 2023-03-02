import logging
import tkinter as tk

from entities.app_manager import ScreenManager

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
    logger.info("Tkinter app starting")
    app = ScreenManager()
    app.mainloop()
    app = tk.Tk()
    logger.info("Tkinter app closing")
