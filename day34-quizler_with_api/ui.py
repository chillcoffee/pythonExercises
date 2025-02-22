from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label_score = Label(text="Score: ", fg="WHITE", bg=THEME_COLOR, font=("Arial", 14, "bold"))
        self.label_score.grid(row=0, column=1, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="WHITE")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Calibri", 18, "italic")
        )

        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        self.button_false = Button(image=false_img, highlightthickness=0)
        self.button_true = Button(image=true_img, highlightthickness=0)

        self.button_false.grid(row=2, column=1, pady=20)
        self.button_true.grid(row=2, column=0, pady=20)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)



