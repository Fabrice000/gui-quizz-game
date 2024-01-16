from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
class QuizzInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)
        self.score = Label(text=f"Score: {self.quiz.score}",background=THEME_COLOR,fg="white",font=("Arial",15,"normal"))
        self.score.grid(column=1,row=0)
        #self.background= PhotoImage(file="/home/carlos/Bureau/100 days of python/Day 34/image/background.png")
        self.canvas = Canvas(width=300,height=250,bg="white") 
        #self.canvas.create_image(133,144,image = self.background)
        self.question_text = self.canvas.create_text(150,125,text="The question is here",font=("Arial",20,"italic"),fill=THEME_COLOR,width=200)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        self.ok_image = PhotoImage(file="image/ok_button.png")
        self.ok_button = Button(image=self.ok_image,highlightthickness=0,command=self.true)
        self.ok_button.grid(column=0,row=2)
        self.cross_image = PhotoImage(file="image/cross_button.png")
        self.cross_button = Button(image=self.cross_image,highlightthickness=0,command=self.false)
        self.cross_button.grid(column=1,row=2)
        self.get_next_question()
        self.window.mainloop()
        
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quizz.")
            self.ok_button.config(state="disabled")
            self.cross_button.config(state="disabled")
            
    
    def true(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right=is_right)
    
    def false(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right=is_right)
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,func=self.get_next_question)
        