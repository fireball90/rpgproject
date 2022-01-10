import random
import combat
import enemy    
import tkinter
import tkinter as tk

player = combat.playerStats(10,100,0)
print(str(player.playerDamage)+ " " + str(player.playerHealth))
enemyMob = enemy.basicEnemy()
while 1:
    enemySelect = input("Select enemy: Basic enemy: q, Defender enemy: d, Berserker enemy: b:")
    if enemySelect == "q":
        enemyMob = enemy.basicEnemy()
        break
    elif enemySelect == "d":
        enemyMob = enemy.defenderEnemy()
        break
    elif enemySelect == "b":
        enemyMob = enemy.berserkerEnemy()
        break
print(enemyMob.unitName)
attackBool = False
print(str(enemy))
while 1:
    if attackBool == False:
        choice = input("Your action! Attack: a , Defend , d , Ultimate u :")
    else:
        attackBool = False
        print("Enemy health: {}".format(enemyMob.health))
        print("Your health: {}".format(player.playerHealth))
        print("Ultimate: {}%".format(player.ultimateBar))
        choice = input("Your action! Attack: a , Defend , d , Ultimate u :")
    
    if choice == "a".lower():
        enemyMob.health, player.ultimateBar, combatLog = combat.playerAttack(player.playerDamage, enemyMob.health, player.ultimateBar, enemyMob.damageReduction)
        print(combat.playerAttackText(combatLog,enemyMob.unitName))
        attackBool = True
    if choice == "d".lower():
        enemyMob.playerDef, player.ultimateBar = combat.playerDef(enemyMob.playerDef,player.ultimateBar)
        print("You defend")
        attackBool = True      
    if choice == "u".lower():
        if player.ultimateBar < 100:
            print("Need 100% to use that!")
        else:
            enemyMob.health, player.ultimateBar, enemyMob.stunBool, combatLog = combat.playerUltimate(player.playerDamage,enemyMob.health,player.ultimateBar,enemyMob.stunBool,enemyMob.damageReduction)
            print(combat.playerAttackText(combatLog,enemyMob.unitName))
            attackBool = True
    if attackBool == True and enemyMob.health>0:
        player.playerHealth, enemyMob.stunBool, combatLog, enemyMob.playerDef, enemyMob.damageReduction, enemyMob.damage = enemyMob.notRlyAI(player.playerHealth)
        print(combat.enemyAttackText(combatLog))
    if player.playerHealth<=0:
        print("You lose")
        break
    elif enemyMob.health<=0:
        print("You win")
        break
    #with open('battle.txt', 'a') as f:
        #f.writelines('\n')
    
