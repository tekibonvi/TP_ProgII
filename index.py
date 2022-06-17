from tkinter import ttk
from tkinter import *
import sqlite3

class Programa():
    
    
    def __init__(self, window, master = None):
        self.wind = window
        self.wind.title("Colegio CHESTER")
if __name__ == "__main__":
    window = Tk()
    app = Programa(window)
    window.mainloop()