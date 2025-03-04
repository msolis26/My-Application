"""
Martin Solis
02/21/25
Math quiz
"""
from tkinter import*
import random
from random import randint, choice
from PIL import Image, ImageTk


#Create the main window 
mainWindow = Tk()

#Setting the size 
mainWindow.geometry("500x260")



#Name of window
mainWindow.title("Math Wiz")


#Creating frame 1
f1 = Label(mainWindow, text = "Hi There! Welcome to Math Quiz!! Insert your name below", padx = 10, pady= 10)
# Adding the frame to the main windows
f1.grid(row=0, column=0, rowspan=10, columnspan=10)




 #Create the label1
fname = Label(mainWindow, text="Full Name")
fname.grid(row=15, column=0)




#Create the textbox
enterfname = Entry(mainWindow, width=20)
enterfname.grid( row=15, column=5)





fullname = str(enterfname.get())



#Images for the UI
TitleImg = ImageTk.PhotoImage(file="Math title screen.jpg")
Title_Screen = Label(mainWindow, image=TitleImg, height=50, width=50)
Title_Screen.grid(row=10, column=0)
Img = ImageTk.PhotoImage(file="Math.jpg")
Img2 = ImageTk.PhotoImage(file="Bird mascot.jpg")
Img3 = ImageTk.PhotoImage(file="Angry Emoji.jpg")
Img4 = ImageTk.PhotoImage(file="Happy Emoji.jpg")
Img5 = ImageTk.PhotoImage(file="Teacher.jpg")




##Setting the questions 
operator= choice(['+', '-', '*'])
question = StringVar()
answer = StringVar()




#Setting the question counter 
Questions = IntVar()
CorrectAnswer = IntVar()

#Limit so once it reaches it will end the game and show user the score.
limit = 11



#Create a function to launch the next window showing the instructions IF the user typed in their name and not an empty box
def namecheck():
   if enterfname.get()== "":
    error = Toplevel(mainWindow)
    error.title("Error: Name not typed")
    error.geometry("300x200")
    errorLabel = Label(error, text="Please type in name")
    errorLabel.grid(row=0, column=0, rowspan=10, columnspan=10)
    nextButton = Button(error, text= "Okay", command=error.destroy)
    nextButton.grid(row =65, column=00)

   else:

    
    newWindow = Toplevel(mainWindow)
    newWindow.title("Instructions")
    newWindow.geometry("800x300")
    submitButton.configure(state="disabled")
    Greeting = "Welcome", str(enterfname.get()),"Heres how it works, You have 10 random questions of different math expressions to solve"
    welcome = Label(newWindow, text=Greeting , padx=10, pady=10) 
    welcome.grid(row=0, column=0, rowspan=10, columnspan=10)
    Attract_Screen = Label(newWindow, image=Img)
    Attract_Screen.grid(row=10, column=3)
    

    
#This function launches the main game
    def add1():
        newWindow.destroy()
        window1 = Toplevel(mainWindow)
        window1.title("Main Game")
        window1.geometry("500x500")


        #This function would generate a question
        def generateQuestion(): 
            
            global QuestionLabel
            global question, answer 
            num1 = randint(1, 10)
            num2 = randint(1, 10)
            operator= choice(['+', '-', '*'])
            question.set(str(num1) + operator + str(num2))
            answer.set(eval(question.get()))
            hud = "Question" + str(Questions.get())
            Hud = Label(window1, text=hud, fg = "white")
            Hud.grid(row=3, column=0)
            Questions.set(Questions.get()+ 1)
            QuestionLabel = Label(window1, text=question.get(), padx= 10, pady= 10)
            QuestionLabel.grid(row=1, column=0, rowspan=10, columnspan=10)
            Bird = Label(window1, image=Img2)
            Bird.grid(row=10, column=8)
        generateQuestion()   
        



        #This function would check if the answer the user types in is the right answer
        #User gets a pop up saying that the answer is correct or incorrect
        def answercheck():
            if str(answer.get()) != givenAns.get():
                Incorrect = Toplevel(window1)
                Incorrect.title("Results")
                Incorrect.geometry("300x300")
                result = Label(Incorrect, text="Incorrect", fg = "red")
                result.grid(row=3, column=0)
                nextButton = Button(Incorrect, text= "Continue", command=Incorrect.destroy)
                nextButton.grid(row =65, column=00)
                Mad_Emoji = Label(Incorrect, image=Img3)
                Mad_Emoji.grid(row=40, column=1)
                
            else:
                
                Correct = Toplevel(window1)
                Correct.title("Results")
                Correct.geometry("300x300")
                result = Label(Correct, text="Correct you get a star", fg = "green")
                result.grid(row=3, column=0)
                nextButton = Button(Correct, text= "Continue", command=Correct.destroy)
                nextButton.grid(row =65, column=00)
                CorrectAnswer.set(CorrectAnswer.get()+ 1)
                Happy_Emoji = Label(Correct, image=Img4)
                Happy_Emoji.grid(row=40, column=0)
                
                
            generateQuestion() #Returns the function to regenerate another question


            #This Function would pop up a message telling the user they've reach the end of the quiz and show the user the score
            def gameComplete():
                if (Questions.get()) == limit:
                        Submit.config(state="disabled")
                        Complete = Toplevel(window1)
                        Complete.title("End of Game")
                        Complete.geometry("400x400")
                        #End results text
                        Result = "You have gotten" , (str(CorrectAnswer.get())), "out of 10"
                        ResultLabel = Label(Complete, text=Result, fg= "white")
                        ResultLabel.grid(row=3, column=0)
                        ExitButton = Button(Complete, text= "Exit Game", command= mainWindow.destroy)
                        ExitButton.grid(row =75, column=00)
                        Teacher = Label(Complete, image=Img5)
                        Teacher.grid(row=40, column=0)
            gameComplete()  #Returns the function
            
        givenAns = StringVar()
            
                
        
             

    
        #Insert the label asking user a math question
        QuestionLabel = Label(window1, text=question.get(), padx= 10, pady= 10)
        QuestionLabel.grid(row=1, column=0, rowspan=10, columnspan=10)
        #Create the textbox
        reply = Entry(window1, textvariable=givenAns, width=20)
        reply.grid( row=62, column=5)

        #Create another submit button
        Submit = Button(window1, text="Submit", command= answercheck)
        Submit.grid(row =25, column=00)
        hud = "Question: " + str(Questions.get())
        Hud = Label(window1, text=hud, fg = "white")
        Hud.grid(row=3, column=0)

        


       

        
        
        
        
        
   

        

    #Button to start the game 
    start = Button(newWindow, text= "Begin Game", command=add1)
    start.grid(row =65, column=00)
    






#A button to launch the next window 
submitButton = Button(mainWindow, text= "Submit", command=namecheck)
submitButton.grid(row =75, column=00)



mainWindow.mainloop()
