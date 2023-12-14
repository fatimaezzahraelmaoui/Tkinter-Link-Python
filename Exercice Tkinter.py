from tkinter import *
import webbrowser

def myfunction():
    lien = mytext.get()
    webbrower.open(lien)
    
mypage = Tk()
mypage.title("my home")
mypage.geometry("200x100")

mylabel = Label(mypage, text="Browser", font="Tahoma 30 bold")
mylabel.pack()

mytext = Entry(mypage, width=50, hieght=10)
mytext.pack()

mybutton = Button(mypage, text="Envoyer", fg="black", bg="yellow", font="helvatice 10 bold")
mybutton.pack()

myframe.mainloop()