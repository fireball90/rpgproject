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

#combat units
player = combat.playerStats(10,100,0)
enemyMob = enemy.basicEnemy()

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


#gombok

btnAttack=tk.PhotoImage(file="images/buttonattack.gif")
btnDefend=tk.PhotoImage(file="images/buttondefend.gif")
btnUltimate=tk.PhotoImage(file="images/buttonultimate.gif")

#gomb függvények
def attackButton():
    global player,enemyMob
    combatLog = 0
    enemyMob.health, player.ultimateBar, combatLog = combat.playerAttack(player.playerDamage, enemyMob.health, player.ultimateBar, enemyMob.damageReduction)
    enemyCombatText.config(text = combat.playerAttackText(combatLog,enemyMob.unitName))
    if enemyMob.health>0:
        player.playerHealth, enemyMob.stunBool, combatLog, enemyMob.playerDef, enemyMob.damageReduction, enemyMob.damage = enemyMob.notRlyAI(player.playerHealth)
        playerCombatText.config(text = combat.enemyAttackText(combatLog))
        enemyHP.config(text = enemyMob.health)
    else:
        playerCombatText.config(text = "{} is dead!".format(enemyMob.unitName))
        enemyHP.config(text = "DEAD")
    playerHP.config(text = player.playerHealth)
    ultimate.config(text = player.ultimateBar)
    combatEndTest()

def defendButton():
    global player,enemyMob
    combatLog = 0
    enemyMob.playerDef, player.ultimateBar = combat.playerDef(enemyMob.playerDef,player.ultimateBar)
    enemyCombatText.config(text = "You defend")
    player.playerHealth, enemyMob.stunBool, combatLog, enemyMob.playerDef, enemyMob.damageReduction, enemyMob.damage = enemyMob.notRlyAI(player.playerHealth)
    playerCombatText.config(text = combat.enemyAttackText(combatLog))
    playerHP.config(text = player.playerHealth)
    ultimate.config(text = player.ultimateBar)
    combatEndTest()


def ultimateButton():
    global player,enemyMob
    combatLog = 0
    if player.ultimateBar==100:
        enemyMob.health, player.ultimateBar, combatLog = combat.playerAttack(player.playerDamage, enemyMob.health, player.ultimateBar, enemyMob.damageReduction)
        enemyCombatText.config(text = combat.playerAttackText(combatLog,enemyMob.unitName))
        if enemyMob.health>0:
            enemyMob.health, player.ultimateBar, enemyMob.stunBool, combatLog = combat.playerUltimate(player.playerDamage,enemyMob.health,player.ultimateBar,enemyMob.stunBool,enemyMob.damageReduction)
            playerCombatText.config(text = combat.enemyAttackText(combatLog))
            enemyHP.config(text = enemyMob.health)
        else:
            playerCombatText.config(text = "{} is dead!".format(enemyMob.unitName))
            enemyHP.config(text = "DEAD")
        playerHP.config(text = player.playerHealth)
        ultimate.config(text = player.ultimateBar)

    combatEndTest()

def defendButton():
    global player,enemyMob
    combatLog = 0
    enemyMob.playerDef, player.ultimateBar = combat.playerDef(enemyMob.playerDef,player.ultimateBar)
    enemyCombatText.config(text = "You defend")
    player.playerHealth, enemyMob.stunBool, combatLog, enemyMob.playerDef, enemyMob.damageReduction, enemyMob.damage = enemyMob.notRlyAI(player.playerHealth)
    playerCombatText.config(text = combat.enemyAttackText(combatLog))
    playerHP.config(text = player.playerHealth)
    ultimate.config(text = player.ultimateBar)
    combatEndTest()  



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




fightLabel = tk.Label(battleStatus, text=testvar, font=("Arial", 16), background="#BBBBBB", fg="red")
fightLabel.place(x=220,y=20)

enemyName=tk.Label(battleStatus, text=enemyMob.unitName, bg="red")
enemyName.place(x=120,y=120)

enemyCombatText=tk.Label(battleStatus, text="", bg="red")
enemyCombatText.place(x=120,y=220)
playerCombatText=tk.Label(battleStatus, text="", bg="red")
playerCombatText.place(x=120,y=260)
combatLog = 0

enemyHP=tk.Label(battleStatus, text=enemyMob.health, bg="red",font=("Arial", 16))
enemyHP.place(x=120,y=140)
playerHP=tk.Label(battleStatus, text=player.playerHealth, bg = "#41A317")
playerHP.place(x=360,y=400)
ultimate=tk.Label(battleStatus, text=player.ultimateBar, bg = "cyan")
ultimate.place(x=360,y=420)
#playerHealth, enemy.stunBool, combatLog = enemy.notRlyAI(playerHealth)
combatLabel=tk.Label(battleStatus, text=combat.enemyAttackText(combatLog))

attackBTN=tk.Button(battleControl,border="0",image=btnAttack, text="Attack", fg="Yellow", bg="#555555", font=("Arial",20), command=attackButton)
attackBTN.place(x=40,y=100)
defendBTN=tk.Button(battleControl,border="0",image=btnDefend, text="Defend", fg="Yellow", bg="#555555", font=("Arial",20), command=defendButton)
defendBTN.place(x=230,y=100)
ultimateBTN=tk.Button(battleControl,border="0",image=btnUltimate, text="Ultimate", fg="Yellow", bg="#555555", font=("Arial",20), command=ultimateButton)
ultimateBTN.place(x=430,y=100)

def exitButton():
    if player.playerHealth<=0:
        with open('battle.txt', 'a') as f:
            f.writelines('\n')
        root.destroy()
        import gameover
    else:
        with open('battle.txt', 'a') as f:
            f.writelines('\n')
        root.destroy()

def combatEndTest():
    if player.playerHealth<=0:
        loseLabel=tk.Label(battleStatus, text="You lose")
        loseLabel.place(x=200,y=150)
        attackBTN.destroy()
        defendBTN.destroy()
        ultimateBTN.destroy()
        exitBTN = tk.Button(battleControl,border="0",text="OK",fg="Yellow", bg="#555555", font=("Arial",20), command=exitButton)
        exitBTN.place(x=230,y=100)
    elif enemyMob.health<=0:
        winLabel=tk.Label(battleStatus, text="You win",fg="Yellow", bg="#555555", font=("Arial",20))
        winLabel.place(x=200,y=150)
        attackBTN.destroy()
        defendBTN.destroy()
        ultimateBTN.destroy()
        exitBTN = tk.Button(battleControl,border="0",text="OK",fg="Yellow", bg="#555555", font=("Arial",20), command=exitButton)
        exitBTN.place(x=230,y=100)






root.mainloop()
