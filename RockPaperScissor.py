from tkinter import *
import random

master = Tk()
master.geometry("350x350")
master.title("Rock-Paper-Scissor Game")

computer_options = {
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}

def play_again():
    button1["state"] = "active"
    button2["state"] = "active"
    button3["state"] = "active"
    label1.config(text="  Player\t")
    label3.config(text="Computer")
    label4.config(text="")

def button_disable():
    button1["state"] = "disable"
    button2["state"] = "disable"
    button3["state"] = "disable"

def isrock():
    c_o = computer_options[str(random.randint(0, 2))]
    if c_o == "Rock":
        match_result = "Match Draw"
    elif c_o == "Scissor":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    label4.config(text=match_result)
    label1.config(text="Rock")
    label3.config(text=c_o)
    button_disable()

def ispaper():
    c_o = computer_options[str(random.randint(0, 2))]
    if c_o == "Paper":
        match_result = "Match Draw"
    elif c_o == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    label4.config(text=match_result)
    label1.config(text="Paper")
    label3.config(text=c_o)
    button_disable()


def isscissor():
    c_o = computer_options[str(random.randint(0, 2))]
    if c_o == "Rock":
        match_result = "Computer Win"
    elif c_o == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Win"
    label4.config(text=match_result)
    label1.config(text="Scissor")
    label3.config(text=c_o)
    button_disable()


Label(master, text="Rock-Paper-Scissor",font="Verdana 14 bold",fg="purple",bg="light blue").pack(pady=20)

frame = Frame(master)
frame.pack(pady=21)

label1 = Label(frame, text="  Player\t",font="Verdana 11")
label1.pack(side=LEFT)

label2 = Label(frame, text="    VS        ",font="Verdana 11 bold",fg="dark blue")
label2.pack(side=LEFT)

label3 = Label(frame, text="Computer", font="Verdana 11")
label3.pack()

label4 = Label(master, text="",font="Verdana 20 bold",bg="light blue",width=16,borderwidth=1.5,relief="solid")
label4.pack(pady=20)

frame1 = Frame(master).pack()

button1 = Button(frame1, text="Rock", font="Verdana 10",width=6,command=isrock)
button1.place(relx = 0.1 , rely= 0.65,relwidth = 0.2 , relheight = 0.08)

button2 = Button(frame1, text="Paper", font="Verdana 10",width=6,command=ispaper)
button2.place(relx = 0.4 , rely= 0.65,relwidth = 0.2 , relheight = 0.08)

button3 = Button(frame1, text="Scissor", font="Verdana 10",width=6,command=isscissor)
button3.place(relx = 0.7, rely= 0.65,relwidth = 0.2 , relheight = 0.08)

button4 = Button(master,text="Play Again",font="Verdana 10 bold",fg="white",bg="purple",command=play_again)
button4.place(relx = 0.33 , rely= 0.8, relwidth = 0.35 , relheight = 0.1)


master.mainloop()














