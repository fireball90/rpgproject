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

#layout megjelenítése 

gameName = tk.Frame(root, background="#111111", height=25)
gameMap = tk.PanedWindow(root, background="#777777", height=400)
gameControl = tk.PanedWindow(root, background="#333333", height=250)
gameMakers = tk.Frame(root, background="#BBBBBB", height=25)
mapPlease = tk.Frame(gameMap, background="#666666", height=400)
buttonFrame = tk.Frame(gameControl,background="#444444",width=180)
statusFrame = tk.Frame(gameControl,background="#888888",width=420)

gameMap.add(mapPlease)
gameControl.add(buttonFrame)
gameControl.add(statusFrame)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
gameName.grid(row=0, column=0, sticky="ew")
gameMap.grid(row=1, column=0, sticky="nsew")
gameControl.grid(row=2, column=0, sticky="nsew")
gameMakers.grid(row=3, column=0, sticky="ew")

#főszöveg megjelenítése 

label1 = tk.Label(master=gameName, text="RPG Játék",bg="#111111", fg="Yellow")
label1.place(x=280, y=2)

label2 = tk.Label(master=gameMakers, text="Copyright (c) Jancsurák Bence, Mészáros Balázs és Lekner Norbert 2021",bg="#BBBBBB", fg="Black")
label2.place(x=115, y=2)

#grid megjelenítése 

for row in range(20):
    for column in range(30):
        f = tk.Frame(mapPlease, background="white",
                     bd=1, relief="sunken",width=20, height=20)
        f.grid(row=row, column=column)

#háttér státusznak /canvas
statusBG = tk.Canvas(statusFrame,width=460,height=250)
statusBG.pack()
img = ImageTk.PhotoImage(Image.open("images/statusbg.jpg"))
statusBG.background = img  # ha funkcióban lenne használva maradjon referencia
bg = statusBG.create_image(0, 0, anchor=tk.NW, image=img)
photoimage = ImageTk.PhotoImage(file="images/zugzug.png")
statusBG.create_image(420, 150, image=photoimage)

def bonusPlay():
    os.system('python bonusgame.py')

def endScreen():
    root.destroy()
    os.system('python ending.py')

def clearFrame():
    for widget in statusFrame.winfo_children():
       widget.destroy()   
    
def clearCanvas():
    statusBG.delete("all")

def showbgpls():
    showBG = tk.Canvas(statusFrame,width=460,height=250)
    showBG.pack()
    img2 = ImageTk.PhotoImage(Image.open("images/statusbg.jpg"))
    showBG.background = img2  # ha funkcióban lenne használva maradjon referencia
    bg2 = showBG.create_image(0, 0, anchor=tk.NW, image=img2)
    photoimage2 = ImageTk.PhotoImage(file="images/zugzug.png")
    showBG.create_image(220, 150, image=photoimage2)

def showControl():
    clearFrame()
    showbgpls()
    moveInfo = tk.Label(master=statusFrame, text="Moving options", font=("Arial", 20), bg="#888888", fg="Yellow")
    moveInfo.place(x=120, y=5)
    moveForward = tk.Button(master=statusFrame, text="Forward", font=("Arial", 16), bg="#888888",fg="Red")
    moveForward.place(x=170, y=60)
    moveBackward = tk.Button(master=statusFrame, text="Backward", font=("Arial", 16), bg="#888888",fg="Red")
    moveBackward.place(x=170, y=120)
    moveLeft = tk.Button(master=statusFrame, text="Left", font=("Arial", 16), bg="#888888",fg="Red")
    moveLeft.place(x=100, y=90)
    moveRight = tk.Button(master=statusFrame, text="Right", font=("Arial", 16), bg="#888888",fg="Red")
    moveRight.place(x=290, y=90)

def showAttack():
    clearFrame()
    showbgpls()
    attackInfo = tk.Label(master=statusFrame, text="Attack options", font=("Arial", 20), bg="#888888", fg="Yellow")
    attackInfo.place(x=170, y=5)
    basicAttack = tk.Button(master=statusFrame, text="Basic attack", font=("Arial", 16), bg="#888888",fg="Red")
    basicAttack.place(x=170, y=60)
    heavyAttack = tk.Button(master=statusFrame, text="Heavy attack", font=("Arial", 16), bg="#888888",fg="Red")
    heavyAttack.place(x=170, y=120)
    specialAttack = tk.Button(master=statusFrame, text="Special attack", font=("Arial", 16), bg="#888888",fg="Red")
    specialAttack.place(x=170, y=180)

def showStatus():
    clearFrame()
    showbgpls()
    statusInfo = tk.Label(master=statusFrame, text="Status", font=("Arial", 20), bg="#888888", fg="Yellow")
    statusInfo.place(x=170, y=5)

    healthStatus = tk.Label(master=statusFrame, text="Health", font=("Arial", 20), bg="#888888", fg="Yellow")
    healthStatus.place(x=50, y=60)

    damageStatus = tk.Label(master=statusFrame, text="Damage", font=("Arial", 20), bg="#888888", fg="Yellow")
    damageStatus.place(x=50, y=120)

    healthEntry = tk.Entry(master=statusFrame)
    healthEntry.insert(0,"Placeholder")
    healthEntry.place(x=240, y=70)
    damageEntry = tk.Entry(master=statusFrame)
    damageEntry.insert(0,"Placeholder")
    damageEntry.place(x=240, y=130)

def showInventory():
    clearFrame()
    showbgpls()
    inventoryInfo = tk.Label(master=statusFrame, text="Inventory", font=("Arial", 20), bg="#888888", fg="Yellow")
    inventoryInfo.place(x=170, y=5)
    healingItem = tk.Button(master=statusFrame, text="Healing item", font=("Arial", 16), bg="#888888",fg="Red")
    healingItem.place(x=170, y=60)



#GOMBOK megjelenítése 

controlMenu = tk.Button(buttonFrame,
    text="Control",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
    command=showControl
)

attackMenu = tk.Button(buttonFrame,
    text="Attack",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
    command=showAttack
)

statusMenu = tk.Button(buttonFrame,
    text="Status",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
    command=showStatus,
)

inventoryMenu = tk.Button(buttonFrame,
    text="Inventory",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
    command=showInventory
)


exitButton = tk.Button(buttonFrame,
    text="Exit",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
    command=endScreen
)

bonusButton = tk.Button(buttonFrame,
    text="Bonus game",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
    command=bonusPlay
)

controlMenu.pack()
attackMenu.pack()
statusMenu.pack()
inventoryMenu.pack()
exitButton.pack()
bonusButton.pack()



root.mainloop()