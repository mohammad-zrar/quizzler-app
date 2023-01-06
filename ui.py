from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, foreground="white", font=("Arial", 12, "normal"))
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40, padx=10)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="The question",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR
                                                     )

        true_img = PhotoImage(file="images/true.png")

        self.true_button = Button(image=true_img, command=self.ture_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reach the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def ture_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.get_next_question()

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#4CE080")
        else:
            self.canvas.config(bg="#E04A43")
        self.window.after(1000, self.white_bg)

    def white_bg(self):
        self.canvas.config(bg="white")
