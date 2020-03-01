from tkinter import  *
import random
import time
import string
import sys


baseWindow = Tk()
baseWindow.title("ROCK-PAPER-SCISSORS")
RPS_frame2 = Frame(baseWindow)
RPS_frame2.place(relx=0.5, rely=1, relwidth=0.9, relheight=0.5, anchor='s')


playerChoice = ""
computerMove = ""
resultPhoto = PhotoImage(file = "results.png")
resultsLabel = Label(RPS_frame2, bg="#92802E", fg = "#922E4B",justify="left", relief="ridge", font = ('Gothic', 30),pady=20)
resultsLabel.place(relx=0.5, rely=0.95, relheight=0.94, relwidth=1, anchor='s')

rockPhoto = PhotoImage(file = "rock.png")
rockPhotoButton = rockPhoto.subsample(3,3)

paperPhoto = PhotoImage(file = "paper.png")
paperPhotoButton = paperPhoto.subsample(3,3)
scissorsPhoto = PhotoImage(file = "scissors.png")
scissorsPhotoButton = scissorsPhoto.subsample(3,3)

class RPS:



    def show1(self):
        string1 = "COMPUTER ALSO PLAYED ROCK\nThis round is a TIE"
        return string1
    def show2 (self):
        string1 = "Computer Played ROCK\nYOU WIN this round"
        return string1
    def show3 (sel):
        string1 = "Computer Played ROCK\nYOU LOSE this round"
        return string1
    def show4 (self):
        string1 = "Computer played PAPER\nYOU LOSE this round"
        return string1
    def show5(self):
        string1 = "Computer Played Scissors\nYOU WIN this round"
        return string1
    def show6(self):
        string1 =  "Computer played SCISSORS\nYOU LOSE this round"
        return string1
    def show7(self):
        string1 = "Computer ALSO PLAYED PAPER\nThis round is a TIE"
        return string1
    def show8(self):
        string1 = "Computer played SCISSORS\nThis round is a TIE"
        return string1
    def show9(self):
        string1 = "COMPUTER PLAYED PAPER\nYOU WIN this round"
        return string1
    def chooseRock (self,Label):
        playerChoice = "rock"
        computerMove = random.choice(string.ascii_letters[:3])
        time.sleep(0.05)
        if computerMove == 'a' and playerChoice == "rock":
            resultsLabel['text'] = self.show1()
        if computerMove == 'b' and playerChoice == "rock":
            resultsLabel['text'] = self.show4()
        if computerMove == 'c' and playerChoice == "rock":
            resultsLabel['text'] = self.show5()

    def choosePaper(self,Label):
        playerChoice ="paper"
        computerMove = random.choice(string.ascii_letters[:3])
        time.sleep(0.05)
        if computerMove == 'a' and playerChoice == "paper":
            resultsLabel['text'] = self.show2()
        if computerMove == 'c' and playerChoice == "paper":
            resultsLabel['text'] = self.show6()
        if computerMove == 'b' and playerChoice == "paper":
            resultsLabel['text'] = self.show7()

    def chooseScissors(self,Label):
        playerChoice = "scissors"
        computerMove = random.choice(string.ascii_letters[:3])
        time.sleep(0.05)
        if computerMove == 'a' and playerChoice == "scissors":
            resultsLabel['text'] = self.show3()
        if computerMove == 'c' and playerChoice == "scissors":
            resultsLabel['text'] = self.show8()

RPSobject = RPS()

#RPS_canvas = Canvas(baseWindow, height=400, width=600)
#RPS_canvas.pack()

RPS_frame1 = Frame(baseWindow)
RPS_frame1.place(relx=0.5, relwidth=0.95, relheight=0.4, anchor='n')
gameLogo = Label(RPS_frame1, text="$$$$$$$$FEMI'S R-P-S INTERFACE$$$$$$$$", anchor='n', fg="#ffff99",
                 bg="#92802E", font=('Gothic', 30), relief="raise")
gameLogo.place(relwidth=1.0)

rockButton = Button(RPS_frame1, text="ROCK", bg  ='black', image = rockPhoto, highlightbackground="#3399ff", font=('Gothic', 20),command=lambda: RPSobject.chooseRock(resultsLabel))
rockButton.place(rely=0.17, relheight=1, relwidth=0.33)

paperButton = Button(RPS_frame1, text="PAPER", bg = 'black',font=('Gothic', 20), image = paperPhoto, command =lambda: RPSobject.choosePaper(resultsLabel))
paperButton.place(rely=0.17, relheight=1, relwidth=0.33, relx=0.33)

scissorButton = Button(RPS_frame1, text="SCISSORS", image = scissorsPhoto,font=('Gothic', 20), bg="white", command = lambda : RPSobject.chooseScissors(resultsLabel))
scissorButton.place(rely=0.17, relheight=1, relwidth=0.33, relx=0.66)

##AREA TO PUT RESULTS WINDOW
#
#
#
#
#
#
#
#
#
#
#
baseWindow.mainloop()
baseWindow = Tk()

