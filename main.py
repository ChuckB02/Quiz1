import tkinter as tk
import logging
import time
import questions

logging.basicConfig(
    filename= "logs/basic.log",
    level = logging.DEBUG,
    format = "%(asctime)s %(levelname)s %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S",
)

class App:
    def __init__(self):
        logging.info("Program started")
        self.root = tk.Tk()
        self.screen()
        self.frames()
        self.start()
        self.root.mainloop()
        logging.info("Program ended")

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

        self.letsGo = tk.Button(self.frameButtons, text= "Let's go", command= self.startQuestion)
        self.letsGo.place(relx= 0.4, rely= 0.35, relwidth= 0.2, relheight= 0.3)

    def startQuestion(self):
        self.frameHeader.destroy()
        self.frameQuestion.destroy()
        self.frameButtons.destroy()
        self.frames()

        self.header = tk.Label(self.frameHeader, text= "Can you answer?", bg= "#FFECB3", font= ('verdanda', 30))
        self.header.place(relx= 0.1, rely= 0.05, relwidth= 0.8, relheight= 0.9)

        self.question = questions.get_question()

        self.labelQuestion = tk.Label(self.frameQuestion, text= self.question.title, bg= "#FFECB3", font= ('verdanda', 25), wraplength= 600)
        self.labelQuestion.place(relx= 0.1, rely= 0.05, relwidth= 0.8, relheight= 0.9)
        
        self.answer1 = tk.Button(self.frameButtons, text= self.question.answers[0], command= lambda: self.checkAnswer(0))
        self.answer1.place(relx= 0.04, rely= 0.35, relwidth= 0.2, relheight= 0.3)

        self.answer2 = tk.Button(self.frameButtons, text= self.question.answers[1], command= lambda: self.checkAnswer(1))
        self.answer2.place(relx= 0.28, rely= 0.35, relwidth= 0.2, relheight= 0.3)

        self.answer3 = tk.Button(self.frameButtons, text= self.question.answers[2], command= lambda: self.checkAnswer(2))
        self.answer3.place(relx= 0.52, rely= 0.35, relwidth= 0.2, relheight= 0.3)

        self.answer4 = tk.Button(self.frameButtons, text= self.question.answers[3], command= lambda: self.checkAnswer(3))
        self.answer4.place(relx= 0.76, rely= 0.35, relwidth= 0.2, relheight= 0.3)

    def checkAnswer(self, index: int):
        if self.question.check(index):
            self.labelQuestion.config(text= "Correct", fg= "#67FF32")
            time.sleep(1)
        else:
            self.labelQuestion.config(text= "Wrong", fg= "#FF4040")
            time.sleep(1)

        if questions.list_of_questions:
            self.startQuestion()
        else:
            self.endWindow()
    
    def endWindow(self):
        self.frameHeader.destroy()
        self.frameQuestion.destroy()
        self.frameButtons.destroy()

        self.thanks = tk.Label(self.root, text= "Thanks for playing", font= ('verdanda', 30), bg= "#FFF0C2")
        self.thanks.place(relx= 0.2, rely= 0.4, relwidth= 0.6, relheight= 0.2)




App()