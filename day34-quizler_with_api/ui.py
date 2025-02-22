from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        label_score = Label(text="Score: ", fg="WHITE", bg=THEME_COLOR)
        label_score.grid(row=0, column=1, pady=20)

        self.question_canvas = Canvas(width=300, height=250)
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=20)

        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        button_false = Button(image=false_img)
        button_true = Button(image=true_img)

        button_false.grid(row=2, column=1, pady=20)
        button_true.grid(row=2, column=0, pady=20)



        self.window.mainloop()
