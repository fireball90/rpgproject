import combat

class basicEnemy:
    def __init__(self,unitName = "Soldier ZugZug",health = 100,damage = 6, abilityUp = True ,stunBool = False, playerDef = False, damageReduction = False):
        self.unitName = unitName
        self.health = health
        self.damage = damage
        self.abilityUp = abilityUp
        self.stunBool = stunBool
        self.playerDef = playerDef
        self.damageReduction = damageReduction
    
    def __str__(self):
        description = "{}: ATTACK: 6, ABILITY: MORTAL STRIKE - A devastating strike that does double damage".format(self.unitName)
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
                    self.playerDef = False
                else:
                    damageLog = int(combat.attackDamageCalc(self.damage)/2)
                    playerHealth = playerHealth - damageLog
                    self.playerDef = False
            else:
                if self.abilityUp == True and self.health < 40:
                    damageLog = combat.attackDamageCalc(2 * self.damage)
                    playerHealth = playerHealth - damageLog
                    self.abilityUp = False
                else:
                    damageLog = combat.attackDamageCalc(self.damage)
                    playerHealth = playerHealth - damageLog
        return playerHealth, self.stunBool, damageLog, self.playerDef, self.damageReduction, self.damage

class defenderEnemy:
    def __init__(self,unitName = "ZugZug Defender",health = 140,damage = 6, abilityUp = True ,stunBool = False, playerDef = False,damageReduction = False):
        self.unitName = unitName
        self.health = health
        self.damage = damage
        self.abilityUp = abilityUp
        self.stunBool = stunBool
        self.playerDef = playerDef
        self.damageReduction = damageReduction
    
    def __str__(self):
        description = "{}: ATTACK: 6, ABILITY: DEFENSIVE STANCE - reduces incoming damage at the expense of offensive capabilities".format(self.unitName)
        return description
    
    def notRlyAI(self,playerHealth):
        damageLog = 0
        if self.health < 70:
            self.damageReduction = True
            self.damage = 4
        if self.stunBool == True:
            self.stunBool = False
        else:
            if self.playerDef == True:
                damageLog = int(combat.attackDamageCalc(self.damage)/2)
                playerHealth = playerHealth - damageLog
                self.playerDef = False
            else:
                damageLog = combat.attackDamageCalc(self.damage)
                playerHealth = playerHealth - damageLog                
        return playerHealth, self.stunBool, damageLog, self.playerDef, self.damageReduction, self.damage

class berserkerEnemy:
    def __init__(self,unitName = "Angry ZugZug",health = 120,damage = 7, abilityUp = True ,stunBool = False, playerDef = False,damageReduction = False):
        self.unitName = unitName
        self.health = health
        self.damage = damage
        self.abilityUp = abilityUp
        self.stunBool = stunBool
        self.playerDef = playerDef
        self.damageReduction = damageReduction
    
    def __str__(self):
        description = "{}: ATTACK: 7, ABILITY: BERSERK - increased damage at less than half health"
        return description
    
    def notRlyAI(self,playerHealth):
        damageLog = 0
        if self.abilityUp == True and self.health<60:
            self.abilityUp = False
            self.damage = 10
        if self.stunBool == True:
            self.stunBool = False
        else:
            if self.playerDef == True:
                damageLog = int(combat.attackDamageCalc(2 * self.damage)/2)
                playerHealth = playerHealth - damageLog
            else:
                damageLog = combat.attackDamageCalc(self.damage)
                playerHealth = playerHealth - damageLog
        return playerHealth, self.stunBool, damageLog, self.playerDef, self.damageReduction, self.damage