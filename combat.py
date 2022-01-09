import random

class playerStats:
    def __init__(self,playerDamage,playerHealth,ultimateBar):
        self.playerDamage = playerDamage
        self.playerHealth = playerHealth
        self.ultimateBar = ultimateBar

def attackDamageCalc(damage):
    return damage + random.randrange(-2,3,2)

def playerAttack(damage,health,ultimateBar,defense):
    dmg_num = 0
    if defense==True:
        if damage%2==1:
            dmg_num = attackDamageCalc((damage/2)+1)
        else:
            dmg_num = attackDamageCalc(damage/2)
    else:
        dmg_num = attackDamageCalc(damage)
    health = health - dmg_num
    ultimateBar =ultimateBar+ 16+ random.randrange(-8,9,4)
    if ultimateBar>100:
        ultimateBar = 100
    return health, ultimateBar, dmg_num

def playerDef(defenseBool,ultimateBar):
    defenseBool = True
    ultimateBar += 30 + random.randrange(-4,5,4)
    if ultimateBar>100:
        ultimateBar = 100
    return defenseBool,ultimateBar

def playerUltimate(damage,health,ultimateBar,stunBool,defense):
    dmg_num = 0
    if defense==True:
        if damage%2==1:
            dmg_num = attackDamageCalc(((2*damage)/2)+1)
        else:
            dmg_num = attackDamageCalc((2*damage)/2)
    else:
        dmg_num = attackDamageCalc(2*damage)
    health = health - dmg_num
    stunBool = True
    ultimateBar = 0
    return health, ultimateBar,stunBool, dmg_num

def enemyAttackText(dmg):
    return "You took {} damage".format(dmg)

def playerAttackText(dmg,name):
    return "You hit {} for {} damage".format(name,dmg)