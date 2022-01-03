import tkinter as tk
import tkinter
from tkinter import *
from tkinter.constants import LEFT
from typing import Text
from PIL import Image, ImageTk
import os

directory= os.path.dirname(__file__)

root = tk.Tk()
root.geometry("600x700")
root.resizable(False, False)

splashArt = ImageTk.PhotoImage(Image.open(os.path.join(directory,"images/startup.gif")))

splashScreen = Label(root,image=splashArt)
splashScreen.place(x=0,y=0)



playGame = Button(root, text="PLAY THE GAME", font=("Arial",30), fg="White", bg="Green",command=root.destroy)
playGame.place(x=120,y=570)

root.mainloop()

import base_v2