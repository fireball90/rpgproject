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

def drawBattleBG():
    attackBG = tk.Canvas(battleStatus,width=600,height=600)
    attackBG.pack()
    img5 = ImageTk.PhotoImage(file="images/fightBG.gif")
    attackBG.background = img5
    bg = attackBG.create_image(0, 0, anchor=tk.NW, image=img5)
    fightLabel = tk.Label(battleStatus, text="Enemy encounter!", font=("Arial", 16), background="#BBBBBB", fg="red")
    fightLabel.place(x=220,y=20)


def clearLabel():
    attackBG.delete("all")

def attackBtn():
    enemy.health, ultimateBar, combatLog = combat.playerAttack(damage,enemy.health,ultimateBar)
    attackLabel=tk.Label(battleStatus, textvariable=combat.playerAttackText(combatLog))
    attackLabel.place(x=200,y=200)

def defenseBtn():
    enemy.playerDef, ultimateBar = combat.playerDef(enemy.playerDef,ultimateBar)
    defenseLabel=tk.Label(battleStatus, text="You defend")
    defenseLabel.place(x=200,y=260)

def ultimateBtn():
    enemy.health, ultimateBar, enemy.stunBool, combatLog = combat.playerUltimate(damage,enemy.health,ultimateBar,enemy.stunBool)
    ultimateLabel=tk.Label(battleStatus, textvariable=combat.playerAttackText(combatLog))
    ultimateLabel.place(x=200,y=320)

#gombok

btnAttack=tk.PhotoImage(file="images/buttonattack.gif")
btnDefend=tk.PhotoImage(file="images/buttondefend.gif")
btnUltimate=tk.PhotoImage(file="images/buttonultimate.gif")


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
img4 = ImageTk.PhotoImage(file="images/combatbg.gif")
attackBG2.background = img4
bg = attackBG2.create_image(0, 0, anchor=tk.NW, image=img4)

testvar = 'elso szoveg'

def update():
    global testvar
    testvar = 'masodik szoveg'

    fightLabel = tk.Label(battleStatus, text=testvar, font=("Arial", 16), background="#BBBBBB", fg="red")
    fightLabel.place(x=220,y=20)

attackBTN=tk.Button(battleControl,border="0",image=btnAttack, text="Attack", fg="Yellow", bg="#555555", font=("Arial",20), command=update)
attackBTN.place(x=40,y=100)
defendBTN=tk.Button(battleControl,border="0",image=btnDefend, text="Defend", fg="Yellow", bg="#555555", font=("Arial",20), command=defenseBtn)
defendBTN.place(x=230,y=100)
ultimateBTN=tk.Button(battleControl,border="0",image=btnUltimate, text="Ultimate", fg="Yellow", bg="#555555", font=("Arial",20), command=ultimateBtn)
ultimateBTN.place(x=430,y=100)

fightLabel = tk.Label(battleStatus, text=testvar, font=("Arial", 16), background="#BBBBBB", fg="red")
fightLabel.place(x=220,y=20)

combatLog = 0
playerHealth = 100
damage = 10
ultimateBar = 0
enemy = enemy.basicEnemy()


enemyName=tk.Label(battleStatus, textvariable=str(enemy))
enemyName.place(x=100,y=80)


enemyHP=tk.Label(battleStatus, textvariable=enemy.health)
enemyHP.place(x=100,y=100)
playerHP=tk.Label(battleStatus, textvariable="Your health: {}".format(playerHealth))
playerHP.place(x=100,y=120)
ultimate=tk.Label(battleStatus, textvariable="Ultimate: {}%".format(ultimateBar))
enemyHP.place(x=100,y=120)
playerHealth, enemy.stunBool, combatLog = enemy.notRlyAI(playerHealth)
combatLabel=tk.Label(battleStatus, textvariable=combat.enemyAttackText(combatLog))
if playerHealth<=0:
    clearLabel()
    drawBattleBG()
    loseLabel=tk.Label(battleStatus, textvariable="You lose")
    loseLabel.place(x=200,y=150)
elif enemy.health<=0:
    clearLabel()
    drawBattleBG()
    winLabel=tk.Label(battleStatus, textvariable="You win")
    winLabel.place(x=200,y=150)
with open('battle.txt', 'a') as f:
    f.writelines('\n')




root.mainloop()