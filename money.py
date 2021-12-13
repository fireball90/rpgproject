import tkinter as tk
import tkinter
from tkinter import *
from tkinter import font
from tkinter.constants import LEFT
from typing import Text
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)

bankArt = ImageTk.PhotoImage(Image.open("images/money.gif"))
moneyBG = Label(root,image=bankArt)
moneyBG.place(x=0,y=0)

creditCardNumber = Label(root, text="Enter credit card number: ", bg="Green", fg="white", font=("Arial",12))
creditCardNumber.place(x=20,y=100)
creditCardInput = Entry(root)
creditCardInput.insert(0,"0000-0000-0000-0000")
creditCardInput.place(x=210, y=102)

creditCardName = Label(root, text="Enter your name: ", bg="Green", fg="white", font=("Arial",12))
creditCardName.place(x=20,y=130)
creditNameInput = Entry(root)
creditNameInput.insert(0,"Placeholder Joe Doe")
creditNameInput.place(x=210, y=132)

creditCardDate = Label(root, text="Enter expiration date: ", bg="Green", fg="white", font=("Arial",12))
creditCardDate.place(x=20,y=160)
creditDateInput = Entry(root)
creditDateInput.insert(0,"MM/YY")
creditDateInput.place(x=210, y=162)

creditCardCode = Label(root, text="Enter your CCV (Code): ", bg="Green", fg="white", font=("Arial",12))
creditCardCode.place(x=20,y=190)
creditCodeInput = Entry(root)
creditCodeInput.insert(0,"XXX")
creditCodeInput.place(x=210, y=192)

overallMoney = Label(root, text="Payment: 10$ ", bg="Green", fg="white", font=("Arial",30))
overallMoney.place(x=20,y=260)

payButton = Button(root, text="PAY and Exit", font=("Arial",20), fg="White", bg="Green",command=root.destroy)
payButton.place(x=320,y=255)


root.mainloop()