import tkinter as tk
import sqlite3
import logging

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.screen()
        self.frames()
        self.start()
        self.root.mainloop()

    def screen(self):
        self.root.title("Quiz Game")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(background= "#FFF0C2")
    
    def frames(self):
        self.frameHeader = tk.Frame(self.root, bg= "#FFECB3")
        self.frameHeader.place(relx= 0.03, rely= 0.03, relwidth= 0.94, relheight= 0.17)

        self.frameQuestion = tk.Frame(self.root, bg= "#FFECB3")
        self.frameQuestion.place(relx= 0.03, rely= 0.23, relwidth= 0.94, relheight= 0.40)

        self.frameButtons = tk.Frame(self.root, bg= "#FFECB3")
        self.frameButtons.place(relx= 0.03, rely= 0.66, relwidth= 0.94, relheight= 0.31)
        
    def start(self):
        self.welcome = tk.Label(self.frameHeader, text= "Welcome to my Quiz Game", bg= "#FFECB3", font= ('verdanda', 30))
        self.welcome.place(relx= 0.1, rely= 0.05, relwidth= 0.8, relheight= 0.9)

        self.doYouWantToPlay = tk.Label(self.frameQuestion, text= "Do you want to play?", bg= "#FFECB3", font= ('verdanda', 25))
        self.doYouWantToPlay.place(relx= 0.1, rely= 0.05, relwidth= 0.8, relheight= 0.9)

        self.letsGo = tk.Button(self.frameButtons, text= "Let's go")
        self.letsGo.place(relx= 0.4, rely= 0.35, relwidth= 0.2, relheight= 0.3)

    def question(self):
        pass







App()