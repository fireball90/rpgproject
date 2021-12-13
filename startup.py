import tkinter as tk
import tkinter
from tkinter import *
from tkinter.constants import LEFT
from typing import Text
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x700")
root.resizable(False, False)

splashArt = ImageTk.PhotoImage(Image.open("images/startup.gif"))

splashScreen = Label(root,image=splashArt)
splashScreen.place(x=0,y=0)



playGame = Button(root, text="PLAY THE GAME", font=("Arial",30), fg="White", bg="Green",command=root.destroy)
playGame.place(x=120,y=400)

root.mainloop()

import basev2