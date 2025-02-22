"""
Martin Solis
02/21/25
Math quiz
"""
from tkinter import*
import random
from random import randint, choice
#Create the main window 
mainWindow = Tk()

#Setting the size 
mainWindow.geometry("500x260")
#Name of window
mainWindow.title("Math Wiz")
#Creating frame 1
f1 = Label(mainWindow, text = "Hi There! Welcome to Math Quiz Click Proceed to Begin", padx = 10, pady= 10)
# Adding the frame to the main windows
f1.grid(row=0, column=0, rowspan=10, columnspan=10)

#Create a function to launch the next window 
def nextWindow():
    newWindow = Toplevel(mainWindow)
    newWindow.title("Next window")
    newWindow.geometry("500x500")
    submitButton.configure(state="disabled")

    #Loading the next label for the next window 
    #Create the label1
    fname = Label(newWindow, text="First Name")
    fname.grid(row=2, column=0)
    #Create the textbox
    enterfname = Entry(newWindow, width=20)
    enterfname.grid( row=2, column=5)
    #Create the label1
    lname = Label(newWindow, text="Last Name")
    lname.grid(row=5, column=0)
    #Create the textbox
    enterlname = Entry(newWindow, width=20)
    enterlname.grid(row=5, column=5)
    fullname = str(enterfname.get()) , str(enterlname.get())
#Create a function that launches problem depending on what expression user selects
    def add1():
        
        newWindow.destroy()
        window1 = Toplevel(mainWindow)
        window1.title("Main Game")
        window1.geometry("500x500")
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        HUD = Label(window1, text=fullname , padx=10, pady=10) 
        HUD.grid(row=0, column=0, rowspan=10, columnspan=10)
        operater= choice(['+', '-', '*', '/'])
        question = str(num1) + operater + str(num2)
        Sum_answer = eval(question)
        #Create the textbox
        reply = Entry(window1, width=20)
        reply.grid( row=62, column=5)
      
        #Check if answer for addition problem is correct
        def answercheck():
            Ans = int(reply.get())
            if Ans != Sum_answer:
                wrong = Toplevel(window1)
                wrong.title("Main Game")
                wrong.geometry("500x500")
                resultw = Label(wrong, background= "red",text="Im sorry but you had typed in the wrong answer")
                resultw.grid(row=0, column=0, rowspan=10, columnspan=10)
                retry = Button(wrong, text= "Retry", command=wrong.destroy)
                retry.grid(row=45, column=0)
                
            else:
                window1
                rightAns = Toplevel(window1)
                rightAns.title("Main Game")
                rightAns.geometry("500x500")
                resultR = Label(rightAns, background= "green", text= "Congrats you've earned a star")
                resultR.grid(row=0, column=0, rowspan=10, columnspan=10)
                Cont = Label(rightAns, foreground= "White", text= "Do you wish to continue?")
                Cont.grid(row=30, column=0, rowspan=10, columnspan=10)
                y = Button(rightAns, text="Yes", command=add1)
                y.grid(row=45, column =0,)
                n = Button(rightAns, text="no", command=window1.destroy)
                n.grid(row=45, column =30)


        #Create the textbox
        reply = Entry(window1, width=20)
        reply.grid( row=62, column=5)  

        


        #Insert the label asking user a math question

        
        QnA = Label(window1, text=question, padx= 10, pady= 10)
        QnA.grid(row=10, column=0, rowspan=10, columnspan=10)
        #Create another submit button
        Submit = Button(window1, text="Submit", command= answercheck)
        Submit.grid(row =25, column=00)
        
        
   

        

    #Buttons for selecting the math expression
    add = Button(newWindow, text= "Submit", command=add1)
    add.grid(row =65, column=00)
    






#A button to launch the next window 
submitButton = Button(mainWindow, text= "Proceed", command=nextWindow)
submitButton.grid(row =25, column=00)



mainWindow.mainloop()
