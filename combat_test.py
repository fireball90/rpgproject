import random
import combat
import enemy    

combatLog = 0
playerHealth = 100
damage = 10
ultimateBar = 0
enemy = enemy.basicEnemy()

print(str(enemy))
while 1:
    print("Enemy health: {}".format(enemy.health))
    print("Your health: {}".format(playerHealth))
    print("Ultimate: {}%".format(ultimateBar))
    choice = input("Your action! Attack: a , Defend , d , Ultimate u :")
    if choice == "a".lower():
        enemy.health, ultimateBar, combatLog = combat.playerAttack(damage,enemy.health,ultimateBar)
        print(combat.playerAttackText(combatLog))
    if choice == "d".lower():
        enemy.playerDef, ultimateBar = combat.playerDef(enemy.playerDef,ultimateBar)
        print("You defend")      
    if choice == "u".lower():
        enemy.health, ultimateBar, enemy.stunBool, combatLog = combat.playerUltimate(damage,enemy.health,ultimateBar,enemy.stunBool)
        print(combat.playerAttackText(combatLog))
    playerHealth, enemy.stunBool, combatLog = enemy.notRlyAI(playerHealth)
    print(combat.enemyAttackText(combatLog))
    if playerHealth<=0:
        print("You lose")
        break
    elif enemy.health<=0:
        print("You win")
        break
