from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Test I. True or False")
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

        self.button_false = Button(image=false_img, highlightthickness=0, command=self.click_false)
        self.button_true = Button(image=true_img, highlightthickness=0, command=self.click_true)

        self.button_false.grid(row=2, column=1, pady=20)
        self.button_true.grid(row=2, column=0, pady=20)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your score: {self.quiz.score}/30")
            self.canvas.config(bg="white")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def click_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def click_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)





