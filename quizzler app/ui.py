THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class UI:
      def __init__(self,quiz_brain:QuizBrain):
            self.quiz = quiz_brain
            self.screen = Tk()
            self.screen.title("Quiz Game")
            self.screen.config(padx=20,pady=20,bg=THEME_COLOR)

            self.score_label = Label(text="Score : 0",fg="white",bg=THEME_COLOR)
            self.score_label.grid(row=0,column=1)
            self.canvas = Canvas(width=300,height=250,bg="white")
            self.question_text = self.canvas.create_text(150,125,width=280,text="Some questions",fill=THEME_COLOR,font=('Arial',20,'italic'))
            self.canvas.grid(row=1,column=0,columnspan=2,pady=20)
            true_img = PhotoImage(file="images/true.png")
            false_img = PhotoImage(file="images/false.png")
            
            self.true_button = Button(image=true_img,highlightthickness=0,command=self.true_pressed)
            self.false_button = Button(image=false_img,highlightthickness=0,command=self.false_pressed)

            self.true_button.grid(row=2,column=0)
            self.false_button.grid(row=2,column=1)

            self.get_next()

            self.screen.mainloop()

      def get_next(self):
          self.canvas.config(bg="white")
          if self.quiz.still_has_questions():  
            self.score_label.config(text=f"Score : {self.quiz.score}")
            quz = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=quz)
          else:
               self.canvas.itemconfig(self.question_text,text="You've reached the end.")
               self.true_button.config(state="disabled")
               self.false_button.config(state="disabled")

      def true_pressed(self):
           is_right = self.quiz.check_answer("True")
           self.feedback(is_right)
      def false_pressed(self):
            is_right=self.quiz.check_answer("True")
            self.feedback(is_right)

      def feedback(self,is_right):
            if is_right:
                  self.canvas.config(bg="green")
            else:
                  self.canvas.config(bg="red")


            self.screen.after(1000,self.get_next)
     
                 