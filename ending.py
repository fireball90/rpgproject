import tkinter as tk
import tkinter
from tkinter import *
from tkinter.constants import LEFT
from typing import Text
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.geometry("600x700")
root.resizable(False, False)

def bankScreen():
    root.destroy()
    os.system('python money.py')

splashArt = ImageTk.PhotoImage(Image.open("images/ending.gif"))

splashScreen = Label(root,image=splashArt)
splashScreen.place(x=0,y=0)

closeGame = Button(root, text="NO, BYE!", font=("Arial",20), fg="White", bg="Red",command=quit)
closeGame.place(x=40,y=560)

payButton = Button(root, text="TAKE MY MONEY", font=("Arial",30), fg="White", bg="Gold",command=bankScreen)
payButton.place(x=200,y=550)


root.mainloop()
