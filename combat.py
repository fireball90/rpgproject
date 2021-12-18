import random

def attackDamageCalc(damage):
    return damage + random.randrange(-2,3,2)

def playerAttack(damage,health,ultimateBar):
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

def playerUltimate(damage,health,ultimateBar,stunBool):
    ultimateBar = 0
    dmg_num = attackDamageCalc(2 *damage)
    health = health - dmg_num
    stunBool = True
    return health, ultimateBar,stunBool,dmg_num

def enemyAttackText(dmg):
    return "You took {} damage".format(dmg)

def playerAttackText(dmg):
    return "You hit {} for {} damage".format("<insert enemy here>",dmg)