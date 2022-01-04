import tkinter as tk
import tkinter
from tkinter import *
from tkinter import font
from tkinter.constants import LEFT
from typing import Text
from PIL import Image, ImageTk
import os


    

root = tk.Tk()
root.geometry("600x600")
root.resizable(False, False)



directory= os.path.dirname(__file__)

gameOver = ImageTk.PhotoImage(Image.open("images/dead.gif"))
gameoverBG = Label(root,image=gameOver)
gameoverBG.place(x=0,y=0)

goexitBTN=tk.PhotoImage(file="images/buttonbg.gif")

tryAgain = Button(root,image=goexitBTN ,bg="black", border=0, command=root.destroy)
tryAgain.place(x=100,y=460)

exitBTN = Button(root,image=goexitBTN,  bg="black", border=0,command=root.destroy)
exitBTN.place(x=350,y=460)

exitTxt= Label(root, text="Exit", bg="gold", fg="black", font=("Arial",16))
exitTxt.place(x=395,y=465)

tryAgainTxt= Label(root, text="Try again", bg="gold", fg="black", font=("Arial",16))
tryAgainTxt.place(x=115,y=465)

root.mainloop()
import base_v2