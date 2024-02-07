import tkinter as tk
import sqlite3
import logging

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.screen()
        self.frames()
        self.root.mainloop()

    def screen(self):
        self.root.title("Quiz Game")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(background= "#FFF0C2")
    
    def frames(self):
        self.frameHeader = tk.Frame(self.root, bg= "#FFECB3")
        self.frameHeader.place(relx= 0.03, rely= 0.03, relwidth= 0.94, relheight= 0.17)










App()