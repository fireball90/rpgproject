import battle
import combat
import enemy
import tkinter as tk

player = combat.playerStats(10,100,0)
enemyName = "redEnemy"
battlePopUp=battle.battleWindow(player,enemyName)
battlePopUp.startBattle()