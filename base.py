import tkinter as tk
import tkinter
from tkinter import *
from tkinter.constants import LEFT
from typing import Text
from PIL import Image, ImageTk



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


#GOMBOK megjelenítése 

controlMenu = tk.Button(buttonFrame,
    text="Control",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
)

attackMenu = tk.Button(buttonFrame,
    text="Attack",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
)

statusMenu = tk.Button(buttonFrame,
    text="Status",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
)

inventoryMenu = tk.Button(buttonFrame,
    text="Inventory",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
)

exitButton = tk.Button(buttonFrame,
    text="Exit",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
    command=quit
)

controlMenu.pack()
attackMenu.pack()
statusMenu.pack()
inventoryMenu.pack()
exitButton.pack()

#háttér státusznak /canvas

statusBG = tk.Canvas(statusFrame,width=460,height=250)
statusBG.pack()
img = ImageTk.PhotoImage(Image.open("images/statusbg.jpg"))
statusBG.background = img  # ha funkcióban lenne használva maradjon referencia
bg = statusBG.create_image(0, 0, anchor=tk.NW, image=img)
photoimage = ImageTk.PhotoImage(file="images/zugzug.png")
statusBG.create_image(420, 150, image=photoimage)

#canvas szövegek és beírásos helyek

statusInfo = tk.Label(master=statusBG, text="Status", font=("Arial", 20), bg="#888888", fg="Yellow")
statusInfo.place(x=170, y=5)

healthStatus = tk.Label(master=statusBG, text="Health", font=("Arial", 20), bg="#888888", fg="Yellow")
healthStatus.place(x=50, y=60)

damageStatus = tk.Label(master=statusBG, text="Damage", font=("Arial", 20), bg="#888888", fg="Yellow")
damageStatus.place(x=50, y=120)

healthEntry = tk.Entry(master=statusBG)
healthEntry.insert(0,"Placeholder")
healthEntry.place(x=240, y=70)
damageEntry = tk.Entry(master=statusBG)
damageEntry.insert(0,"Placeholder")
damageEntry.place(x=240, y=130)






root.mainloop()