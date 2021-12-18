import combat

class basicEnemy:
    def __init__(self,health = 100,damage = 6, abilityUp = True ,stunBool = False, playerDef = False):
        self.health = health
        self.damage = damage
        self.abilityUp = abilityUp
        self.stunBool = stunBool
        self.playerDef = playerDef
    
    def __str__(self):
        description = "ATTACK: 6, ABILITY: MORTAL STRIKE - A devastating strike that does double damage"
        return description
    
    def notRlyAI(self,playerHealth):
        damageLog = 0
        if self.stunBool == True:
            self.stunBool = False
        else:
            if self.playerDef == True:
                if self.abilityUp == True and self.health < 40:
                    damageLog = int(combat.attackDamageCalc(2 * self.damage)/2)
                    playerHealth = playerHealth - damageLog
                    self.abilityUp = False
                else:
                    damageLog = int(combat.attackDamageCalc(self.damage)/2)
                    playerHealth = playerHealth - damageLog
            else:
                if self.abilityUp == True and self.health < 40:
                    damageLog = combat.attackDamageCalc(2 * self.damage)
                    playerHealth = playerHealth - damageLog
                    self.abilityUp = False
                else:
                    damageLog = combat.attackDamageCalc(self.damage)
                    playerHealth = playerHealth - damageLog
        return playerHealth, self.stunBool, damageLog

class defenderEnemy:
    def __init__(self,health = 100,damage = 6, abilityUp = True ,stunBool = False, playerDef = False):
        self.health = health
        self.damage = damage
        self.abilityUp = abilityUp
        self.stunBool = stunBool
        self.playerDef = playerDef
    
    def __str__(self):
        description = "ATTACK: 8, ABILITY: MORTAL STRIKE - A devastating strike that does double damage"
        return description
    
    def notRlyAI(self,playerHealth):
        damageLog = 0
        if self.stunBool == True:
            self.stunBool = False
        else:
            if self.playerDef == True:
                if self.abilityUp == True and self.health < 40:
                    damageLog = int(combat.attackDamageCalc(2 * self.damage)/2)
                    playerHealth = playerHealth - damageLog
                    self.abilityUp = False
                else:
                    damageLog = int(combat.attackDamageCalc(self.damage)/2)
                    playerHealth = playerHealth - damageLog
            else:
                if self.abilityUp == True and self.health < 40:
                    damageLog = combat.attackDamageCalc(2 * self.damage)
                    playerHealth = playerHealth - damageLog
                    self.abilityUp = False
                else:
                    damageLog = combat.attackDamageCalc(self.damage)
                    playerHealth = playerHealth - damageLog
        return playerHealth, self.stunBool, damageLog

class berserkerEnemy:
    def __init__(self,health = 100,damage = 6, abilityUp = True ,stunBool = False, playerDef = False):
        self.health = health
        self.damage = damage
        self.abilityUp = abilityUp
        self.stunBool = stunBool
        self.playerDef = playerDef
    
    def __str__(self):
        description = "ATTACK: 8, ABILITY: MORTAL STRIKE - A devastating strike that does double damage"
        return description
    
    def notRlyAI(self,playerHealth):
        damageLog = 0
        if self.stunBool == True:
            self.stunBool = False
        else:
            if self.playerDef == True:
                if self.abilityUp == True and self.health < 40:
                    damageLog = int(combat.attackDamageCalc(2 * self.damage)/2)
                    playerHealth = playerHealth - damageLog
                    self.abilityUp = False
                else:
                    damageLog = int(combat.attackDamageCalc(self.damage)/2)
                    playerHealth = playerHealth - damageLog
            else:
                if self.abilityUp == True and self.health < 40:
                    damageLog = combat.attackDamageCalc(2 * self.damage)
                    playerHealth = playerHealth - damageLog
                    self.abilityUp = False
                else:
                    damageLog = combat.attackDamageCalc(self.damage)
                    playerHealth = playerHealth - damageLog
        return playerHealth, self.stunBool, damageLog