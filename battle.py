from tkinter.font import Font
from PIL import Image, ImageTk
import tkinter as tk
import tkinter
from tkinter import *
import os
import sys
import random
import combat
import enemy    

root = tk.Tk()
root.geometry("600x900")
root.resizable(False, False)

# kirajzolás

battleName = tk.Frame(root, background="#111111", height=25)
battleStatus = tk.PanedWindow(root, background="#111111", width=600, height=600)
battleControl = tk.PanedWindow(root, background="#333333", width=600, height=250)
battleMakers = tk.Frame(root, background="#BBBBBB", height=25)

battleFrame = tk.Frame(battleStatus,background="#888888",width=600,height=600)
battleStatus.add(battleFrame)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
battleName.grid(row=0, column=0, sticky="ew")
battleStatus.grid(row=1, column=0, sticky="nsew")
battleControl.grid(row=2, column=0, sticky="nsew")
battleMakers.grid(row=3, column=0, sticky="ew")

label1 = tk.Label(master=battleName, text="Battle screen",bg="#111111", fg="Yellow")
label1.place(x=280, y=2)

label2 = tk.Label(master=battleMakers, text="Copyright (c) Jancsurák Bence, Mészáros Balázs és Lekner Norbert 2021",bg="#BBBBBB", fg="Black")
label2.place(x=115, y=2)

attackBG = tk.Canvas(battleStatus,width=600,height=600)
attackBG.pack()
img5 = ImageTk.PhotoImage(file="images/fightBG.gif")
attackBG.background = img5
bg = attackBG.create_image(0, 0, anchor=tk.NW, image=img5)

attackBG2 = tk.Canvas(battleControl,width=600,height=250, bg="#444444")
attackBG2.pack()
img4 = ImageTk.PhotoImage(file="images/statusbg.jpg")
attackBG2.background = img4
bg = attackBG2.create_image(0, 0, anchor=tk.NW, image=img4)

attackBTN=tk.Button(battleControl, text="Attack", fg="Yellow", bg="#555555", font=("Arial",20), command="")
attackBTN.place(x=40,y=100)
defendBTN=tk.Button(battleControl, text="Defend", fg="Yellow", bg="#555555", font=("Arial",20), command="")
defendBTN.place(x=230,y=100)
ultimateBTN=tk.Button(battleControl, text="Ultimate", fg="Yellow", bg="#555555", font=("Arial",20), command="")
ultimateBTN.place(x=430,y=100)

fightLabel = tk.Label(battleStatus, text="Enemy encounter!", font=("Arial", 16), background="#BBBBBB", fg="red")
fightLabel.place(x=220,y=20)

fightText=tk.Text(battleStatus)
fightText.place(x=20, y=70, width=400, height=500)
with open("battle.txt", 'r') as fightText:
    fightText.insert(INSERT, fightText.read())
#kirajzolás vége



root.mainloop()