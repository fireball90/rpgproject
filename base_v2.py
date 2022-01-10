import tkinter as tk
import tkinter
from tkinter import *
from tkinter.constants import LEFT
from typing import Text
from PIL import Image, ImageTk
import os
from tkinter import filedialog
import sys
import enemy
import random

root = tk.Tk()
root.geometry("600x900")
root.resizable(False, False)
directory= os.path.dirname(__file__)
#layout megjelenítése 

gameName = tk.Frame(root, background="#111111", height=25)
gameMap = tk.PanedWindow(root, background="#777777", width=600, height=600)
gameControl = tk.PanedWindow(root, background="#333333", height=250)
gameMakers = tk.Frame(root, background="#BBBBBB", height=25)
mapPlease = tk.Frame(gameMap, background="#666666", width=600, height=400)
buttonFrame = tk.Frame(gameControl,background="#444444",width=180)
statusFrame = tk.Frame(gameControl,background="#888888",width=420)
enemyFrame = tk.Frame(gameMap, background="#BBBBBB", height=400)

gameMap.add(mapPlease, width=600, height=600)
gameMap.add(enemyFrame)
gameControl.add(buttonFrame)
gameControl.add(statusFrame)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
gameName.grid(row=0, column=0, sticky="ew")
gameMap.grid(row=1, column=0, sticky="nsew")
gameControl.grid(row=2, column=0, sticky="nsew")
gameMakers.grid(row=3, column=0, sticky="ew")

#főszöveg megjelenítése 

label1 = tk.Label(master=gameName, text="RPG Játék",bg="#111111", fg="Yellow")
label1.place(x=280, y=2)

label2 = tk.Label(master=gameMakers, text="Copyright (c) Jancsurák Bence, Mészáros Balázs és Lekner Norbert 2021",bg="#BBBBBB", fg="Black")
label2.place(x=115, y=2)

#gombok

btnImage=tk.PhotoImage(file="images/buttonbg2.gif")
btnImage2=tk.PhotoImage(file="images/buttonbg.gif")
btnControl=tk.PhotoImage(file="images/buttoncontrol.gif")
btnInventory=tk.PhotoImage(file="images/buttoninventory.gif")
btnStatus=tk.PhotoImage(file="images/buttonstatus.gif")
btnExit=tk.PhotoImage(file="images/buttonexit.gif")
btnMapEditor=tk.PhotoImage(file="images/buttonmapedit.gif")
btnOpenMap=tk.PhotoImage(file="images/buttonopenmap.gif")
btnLoadMap=tk.PhotoImage(file="images/buttonloadmap.gif")
btnEditMap=tk.PhotoImage(file="images/buttonmapedit2.gif")
btnBandage=tk.PhotoImage(file="images/buttonbandage.gif")
btnForward=tk.PhotoImage(file="images/buttonforward.gif")
btnBackward=tk.PhotoImage(file="images/buttonbackward.gif")
btnLeft=tk.PhotoImage(file="images/buttonleft.gif")
btnRight=tk.PhotoImage(file="images/buttonright.gif")

#háttér státusznak /canvas
statusBG = tk.Canvas(statusFrame,width=460,height=250)
statusBG.pack()
img = ImageTk.PhotoImage(Image.open("images/statusbg.jpg"))
statusBG.background = img  # ha funkcióban lenne használva maradjon referencia
bg = statusBG.create_image(0, 0, anchor=tk.NW, image=img)
photoimage = ImageTk.PhotoImage(file="images/zugzug.png")
statusBG.create_image(420, 150, image=photoimage)

def bonusPlay():
    os.system('python bonusgame.py')

def battlePlay():
    os.system('python battle.py')

def mapEditor():
    os.system('python mapeditor.py')

def endScreen():
    root.destroy()
    os.system('python ending.py')

def clearFrame():
    for widget in statusFrame.winfo_children():
       widget.destroy()   
    
def clearCanvas():
    statusBG.delete("all")

#grid megjelenítése 
def showMap():
    clearFrame()
    #for row in range(11):
    #    for column in range(11):
    #        f = tk.Frame(mapPlease, background="white",
    #                    bd=1, relief="sunken",width=20, height=20)
    #        f.grid(row=row, column=column)

def showbgpls():
    showBG = tk.Canvas(statusFrame,width=460,height=250)
    showBG.pack()
    img2 = ImageTk.PhotoImage(Image.open("images/statusbg.jpg"))
    showBG.background = img2  # ha funkcióban lenne használva maradjon referencia
    bg2 = showBG.create_image(0, 0, anchor=tk.NW, image=img2)
    photoimage2 = ImageTk.PhotoImage(file="images/zugzug.png")
    showBG.create_image(220, 150, image=photoimage2)


def mapSelection():
    clearFrame()
    showbgpls()
    mapPath = Entry(statusFrame)
    mapPath.pack(expand=True, fill=X, padx=10,pady=5)   

    openMapButton = tk.Button(
        master=statusFrame, text="Open map", font=("Arial", 14), bg="black",fg="Red", image=btnOpenMap,border="0",
        command = openMap)
    openMapButton.place(x=170,y=60)
    
    openPath = Entry(statusFrame)
    openPath.place(x=100,y=30, width=260)

    openMapEditorButton = tk.Button(
        master=statusFrame, text="Map editor", font=("Arial", 14), bg="black",fg="Red",image=btnEditMap,border="0",
        command = mapEditor)
    openMapEditorButton.place(x=170,y=180)

mapName=""
folderName=""

def openMap():
    tf = filedialog.askopenfilename(
            initialdir="/maps", 
            title="Open Text file", 
            filetypes=(("Text Files", "*.txt"),)
            )
    mapName = os.path.basename(tf)
    folderName = os.path.basename(os.path.dirname(tf))
    currentlyUsedMap=(folderName+"/"+mapName)
    openPath = Entry(statusFrame)
    openPath.place(x=100,y=30, width=260)
    openPath.insert(END, tf)
    
    buttonwhat= tk.Button(statusFrame, text="Use map",font=("Arial", 14),bg="black",fg="Red",image=btnLoadMap,border="0",
     command=lambda:[map.Loading(currentlyUsedMap),map.Drawing()])
    buttonwhat.place(x=170,y=120)

def showControl():
    clearFrame()
    showbgpls()
    moveInfo = tk.Label(master=statusFrame, text="Moving options", font=("Arial", 20), bg="#888888", fg="Yellow")
    moveInfo.place(x=115, y=10)
    moveForward = tk.Button(
        master=statusFrame, text="Forward", font=("Arial", 16), bg="black",fg="Red",image=btnForward ,border="0",
        command = lambda:buttonClicked(-1, 0)
        )
    moveForward.place(x=170, y=60)
    moveBackward = tk.Button(
        master=statusFrame, text="Backward", font=("Arial", 16), bg="black",fg="Red",image=btnBackward ,border="0",
        command = lambda:buttonClicked(1, 0)
        )
    moveBackward.place(x=170, y=150)
    moveLeft = tk.Button(
        master=statusFrame, text="Left", font=("Arial", 16), bg="black",fg="Red",image=btnLeft ,border="0",
        command = lambda:buttonClicked(0, -1)
        )
    moveLeft.place(x=80, y=100)
    moveRight = tk.Button(
        master=statusFrame, text="Right", font=("Arial", 16), bg="black",fg="Red",image=btnRight ,border="0",
        command = lambda:buttonClicked(0, 1)
        )
    moveRight.place(x=260, y=100)

def showAttack():
    clearFrame()
    showbgpls()
    attackInfo = tk.Label(master=statusFrame, text="Attack options", font=("Arial", 20), bg="#888888", fg="Yellow")
    attackInfo.place(x=170, y=5)
    basicAttack = tk.Button(master=statusFrame, text="Basic attack", font=("Arial", 16), bg="#888888",fg="Red", command=combat.playerAttack)
    basicAttack.place(x=170, y=60)
    heavyAttack = tk.Button(master=statusFrame, text="Defend", font=("Arial", 16), bg="#888888",fg="Red",command=combat.playerDef)
    heavyAttack.place(x=170, y=120)
    specialAttack = tk.Button(master=statusFrame, text="Ultimate", font=("Arial", 16), bg="#888888",fg="Red", command=combat.playerUltimate)
    specialAttack.place(x=170, y=180)

def showStatus():
    clearFrame()
    showbgpls()
    statusInfo = tk.Label(master=statusFrame, text="Status", font=("Arial", 20), bg="#888888", fg="Yellow")
    statusInfo.place(x=170, y=5)

    healthStatus = tk.Label(master=statusFrame, text="Health", font=("Arial", 20), bg="#888888", fg="Yellow")
    healthStatus.place(x=50, y=60)

    ultimateStatus = tk.Label(master=statusFrame, text="Damage", font=("Arial", 20), bg="#888888", fg="Yellow")
    ultimateStatus.place(x=50, y=120)

    healthCount = tk.Label(master=statusFrame)
    healthCount.configure(text="{}".format(map.player_object.getHealth()))
    healthCount.place(x=240, y=70)
    ultimateCount = tk.Label(master=statusFrame)
    ultimateCount.configure(text="{}".format(map.player_object.getUltimate()))
    ultimateCount.place(x=240, y=130)

def showInventory():
    clearFrame()
    showbgpls()
    inventoryInfo = tk.Label(master=statusFrame, text="Inventory", font=("Arial", 20), bg="#888888", fg="Yellow")
    inventoryInfo.place(x=170, y=5)
    healingItem = tk.Button(master=statusFrame, text="Healing item", font=("Arial", 16), bg="black",fg="Red",image=btnBandage ,border="0",)
    healingItem.place(x=170, y=60)


#A pálya kirajzolásához szükséges csempéknek, és a mozgó objektumoknak az osztályai
class Tile:
    def __init__(self, sprite, hitbox = False):
        self.sprite = sprite
        self.hitbox = hitbox


#Az objektumok külön koordinátát kaptak, hogy ne kelljen 24*24-es listában tárolni őket a poziciójuk eléréséhez

class Tile:
    def __init__(self, sprite, hitbox = False):
        self.sprite = sprite
        self.hitbox = hitbox

class Player:
    def __init__(self, sprite, x_coord, y_coord):
        self.sprite = sprite
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.name = 'Player'
        self.damage = -200
        self.health = 100
        self.ultimate = 0
        self.hitbox = False

    def NextStep(self, direction_x, direction_y, map_tiles, map_objects):
        new_x = self.x_coord + direction_x
        new_y = self.y_coord + direction_y

        if map_tiles[new_x][new_y].hitbox == False:
            self.x_coord = new_x
            self.y_coord = new_y
        
        for object in map_objects:
            if object.x_coord == self.x_coord and object.y_coord == self.y_coord and object.hitbox:
                object.UpdateHealth(self.damage)
                if not (object.name == "Fire" or object.name == "Bandage"):
                    file = open('battle.txt', 'w')
                    file.write("{}\n{}\n{}".format(object.name,self.health,self.ultimate))
                    file.close()
                    startBattle()
                    file = open('battle.txt', 'r')
                    self.health = int(file.readline())
                    self.ultimate = int(file.readline())
                    file.close()
                object.hitbox = False
                self.UpdateHealth(object.damage)

    def UpdateHealth(self, update_value):
        self.health += update_value

    def getHealth(self):
        return self.health
    def getUltimate(self):
        return self.ultimate
class EnemyBlue:
    def __init__(self, sprite, x_coord, y_coord):
        self.sprite = sprite
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.name = 'EnemyBlue'
        self.damage = 0
        self.health = 100
        self.hitbox = True

    step_direction_x = 1

    def NextStep(self, map_tiles, map_objects, player_object):
        if map_tiles[self.x_coord + self.step_direction_x][self.y_coord].hitbox:
            self.step_direction_x = -self.step_direction_x
        
        for object in map_objects:
            if object.x_coord == self.x_coord + self.step_direction_x and object.y_coord == self.y_coord and object.hitbox:
                self.step_direction_x = -self.step_direction_x
        
        self.x_coord += self.step_direction_x

        if player_object.x_coord == self.x_coord and player_object.y_coord == self.y_coord and self.hitbox:
            self.UpdateHealth(player_object.damage)
            self.hitbox = False
            file = open('battle.txt', 'w')
            file.write("{}\n{}\n{}".format(self.name,player_object.health,player_object.ultimate))
            file.close()
            startBattle()
            file = open('battle.txt', 'r')
            player_object.health = int(file.readline())
            player_object.ultimate = int(file.readline())
            file.close()

    def UpdateHealth(self, update_value):
        self.health += update_value

class EnemyGreen:
    def __init__(self, sprite, x_coord, y_coord):
        self.sprite = sprite
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.name = 'EnemyGreen'
        self.damage = 0
        self.health = 120
        self.hitbox = True

    step_direction_y = 1

    def NextStep(self, map_tiles, map_objects, player_object):
        if map_tiles[self.x_coord][self.y_coord + self.step_direction_y].hitbox:
            self.step_direction_y = -self.step_direction_y
        
        for object in map_objects:
            if object.x_coord == self.x_coord and object.y_coord == self.y_coord + self.step_direction_y and object.hitbox:
                self.step_direction_y = -self.step_direction_y
        
        self.y_coord += self.step_direction_y

        if player_object.x_coord == self.x_coord and player_object.y_coord == self.y_coord and self.hitbox:
            self.UpdateHealth(player_object.damage)
            self.hitbox = False
            file = open('battle.txt', 'w')
            file.write("{}\n{}\n{}".format(self.name,player_object.health,player_object.ultimate))
            file.close()
            startBattle()
            file = open('battle.txt', 'r')
            player_object.health = int(file.readline())
            player_object.ultimate = int(file.readline())
            file.close()

    def UpdateHealth(self, update_value):
        self.health += update_value

class EnemyRed:
    def __init__(self, sprite, x_coord, y_coord):
        self.sprite = sprite
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.name = 'EnemyRed'
        self.damage = 0
        self.health = 140
        self.hitbox = True

    step_direction_x = 1
    step_direction_y = 0
    step_counter = 0
    turn = 1

    def NextStep(self, map_tiles, map_objects, player_object):
        self.step_counter += 1

        if self.step_counter > 2 and self.turn:
            tmp = self.step_direction_x
            self.step_direction_x = -self.step_direction_y
            self.step_direction_y = tmp

            self.step_counter = 0
        elif self.step_counter > 2 and self.turn == 0:
            tmp = self.step_direction_x
            self.step_direction_x = self.step_direction_y
            self.step_direction_y = -tmp

            self.step_counter = 0

        if map_tiles[self.x_coord + self.step_direction_x][self.y_coord + self.step_direction_y].hitbox:
            self.step_direction_x = -self.step_direction_x
            self.step_direction_y = -self.step_direction_y

            self.turn = not self.turn
            self.step_counter = 3 - self.step_counter

        for object in map_objects:
            if object.x_coord == self.x_coord + self.step_direction_x and object.y_coord == self.y_coord + self.step_direction_y and object.hitbox:
                self.step_direction_x = -self.step_direction_x
                self.step_direction_y = -self.step_direction_y

                self.turn = not self.turn
                self.step_counter = 3 - self.step_counter

        self.x_coord += self.step_direction_x
        self.y_coord += self.step_direction_y

        if player_object.x_coord == self.x_coord and player_object.y_coord == self.y_coord and self.hitbox:
            self.UpdateHealth(player_object.damage)
            self.hitbox = False
            file = open('battle.txt', 'w')
            file.write("{}\n{}\n{}".format(self.name,player_object.health,player_object.ultimate))
            file.close()
            startBattle()
            file = open('battle.txt', 'r')
            player_object.health = int(file.readline())
            player_object.ultimate = int(file.readline())
            file.close()

    def UpdateHealth(self, update_value):
        self.health += update_value

class EnemyBoss:
    def __init__(self, sprite, x_coord, y_coord):
        self.sprite = sprite
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.name = 'EnemyBoss'
        self.damage = 0
        self.health = 100
        self.hitbox = True

    def NextStep(self, map_tiles, map_objects, player_object):
        pass

    def UpdateHealth(self, update_value):
        self.health += update_value

class Fire:
    def __init__(self, sprite, x_coord, y_coord):
        self.sprite = sprite
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.name = 'Fire'
        self.damage = -10
        self.health = 100
        self.hitbox = True

    def NextStep(self, map_tiles, map_objects, player_object):
        if player_object.x_coord == self.x_coord and player_object.y_coord == self.y_coord:
            player_object.UpdateHealth(self.damage)

    def UpdateHealth(self, update_value):
        self.health += 0

class Bandage:
    def __init__(self, sprite, x_coord, y_coord):
        self.sprite = sprite
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.name = 'Bandage'
        self.damage = 60
        self.health = 100
        self.hitbox = True

    def NextStep(self, map_tiles, map_objects, player_object):
        pass

    def UpdateHealth(self, update_value):
        self.health += update_value

#battle ablak generálás
def startBattle():
    from subprocess import call
    call(["python","battle.py"])

class Map:
    map_canvas = tk.Canvas(mapPlease,width = 576, height = 600)
    map_tiles = []
    map_objects = []
    player_object = None
    update = True

    sprites = (
        PhotoImage(file = 'sprites/grass.gif').zoom(3),
        PhotoImage(file = 'sprites/sand.gif').zoom(3),
        PhotoImage(file = 'sprites/snow.gif').zoom(3),
        PhotoImage(file = 'sprites/side.gif').zoom(3),
        PhotoImage(file = 'sprites/side2.gif').zoom(3),
        PhotoImage(file = 'sprites/side3.gif').zoom(3),
        PhotoImage(file = 'sprites/roof.gif').zoom(3),
        PhotoImage(file = 'sprites/roof2.gif').zoom(3),
        PhotoImage(file = 'sprites/roof3.gif').zoom(3),
        PhotoImage(file = 'sprites/tree1.gif').zoom(3),
        PhotoImage(file = 'sprites/tree2.gif').zoom(3),
        PhotoImage(file = 'sprites/tree3.gif').zoom(3),
        PhotoImage(file = 'sprites/enemyblue.gif').zoom(3),
        PhotoImage(file = 'sprites/enemygreen.gif').zoom(3),
        PhotoImage(file = 'sprites/enemyred.gif').zoom(3),
        PhotoImage(file = 'sprites/enemyboss.gif').zoom(3),
        PhotoImage(file = 'sprites/player.gif').zoom(3),
        PhotoImage(file = 'sprites/fire.gif').zoom(3),
        PhotoImage(file = 'sprites/chest.gif').zoom(3),
        PhotoImage(file = 'sprites/bandage.gif').zoom(3),
        PhotoImage(file = 'sprites/star.gif').zoom(3)
    )

    def Loading(self, map_name):
        self.map_tiles.clear()
        self.map_objects.clear()

        with open(map_name, 'r', encoding = 'utf-8') as file:
            for i in range(24):
                map_string = file.readline()
                self.map_tiles.append([])
                        
                for j in range(24):
                    if map_string[j] == '.':
                        self.map_tiles[i].append(Tile(self.sprites[0]))
                    elif map_string[j] == ':':
                        self.map_tiles[i].append(Tile(self.sprites[1]))
                    elif map_string[j] == ';':
                        self.map_tiles[i].append(Tile(self.sprites[2]))
                    elif map_string[j] == '(':
                        self.map_tiles[i].append(Tile(self.sprites[3],True))
                    elif map_string[j] == '{':
                        self.map_tiles[i].append(Tile(self.sprites[4], True))
                    elif map_string[j] == '[':
                        self.map_tiles[i].append(Tile(self.sprites[5], True))
                    elif map_string[j] == '-':
                        self.map_tiles[i].append(Tile(self.sprites[6], True))
                    elif map_string[j] == '=':
                        self.map_tiles[i].append(Tile(self.sprites[7], True))
                    elif map_string[j] == '_':
                        self.map_tiles[i].append(Tile(self.sprites[8], True))
                    elif map_string[j] == '!':
                        self.map_tiles[i].append(Tile(self.sprites[9], True))
                    elif map_string[j] == '|':
                        self.map_tiles[i].append(Tile(self.sprites[10], True))
                    elif map_string[j] == '/':
                        self.map_tiles[i].append(Tile(self.sprites[11], True))

            for i in range(24):
                map_string = file.readline()

                for j in range(24):
                    if map_string[j] == 'p':
                        self.player_object = (Player(self.sprites[16], i, j))
                    elif map_string[j] == '1':
                        self.map_objects.append(EnemyBlue(self.sprites[12], i, j))
                    elif map_string[j] == '2':
                        self.map_objects.append(EnemyGreen(self.sprites[13], i, j))
                    elif map_string[j] == '3':
                        self.map_objects.append(EnemyRed(self.sprites[14], i, j))
                    elif map_string[j] == '4':
                        self.map_objects.append(EnemyBoss(self.sprites[15], i, j))
                    elif map_string[j] == 'f':
                        self.map_objects.append(Fire(self.sprites[17], i, j))
                    elif map_string[j] == 'b':
                        self.map_objects.append(Bandage(self.sprites[19], i, j))

    def Drawing(self):
        self.map_canvas.pack(expand=YES, fill=BOTH)

        self.map_canvas.delete('all')

        for i in range(24):
            for j in range(24):
                self.map_canvas.create_image(j * 24, i * 24, image = self.map_tiles[i][j].sprite, anchor = NW)
        if self.player_object.health > 0:
            self.map_canvas.create_image(self.player_object.y_coord * 24, self.player_object.x_coord * 24, image = self.player_object.sprite, anchor = NW)
        else:
            root.destroy()
            import gameover

        for object in self.map_objects:
            if object.health > 0:
                self.map_canvas.create_image(object.y_coord * 24, object.x_coord * 24, image = object.sprite, anchor = NW)

    def Update(self):
        for object in self.map_objects:
            if object.health > 0:
                object.NextStep(self.map_tiles, self.map_objects, self.player_object)
        
        if self.player_object.health < 40:
            self.player_object.UpdateHealth(2)

        self.Drawing()
        map.map_canvas.after(1000, self.Update)



map = Map()
map.Loading('maps/first_level.txt')
map.Drawing()
map.Update()

def buttonClicked(direction_x, direction_y):
    map.player_object.NextStep(direction_x, direction_y, map.map_tiles, map.map_objects)
    print(map.player_object.health)
    map.Drawing()

#################################################################################

#GOMBOK megjelenítése 

controlMenu = tk.Button(buttonFrame,
    text="Control",
    image=btnControl,
    border="0",
    width=130,
    height=41,
    bg="#444444",
    fg="yellow",
    command=showControl
)

attackMenu = tk.Button(buttonFrame,
    text="Attack",
    border="0",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
    command=showAttack
)

statusMenu = tk.Button(buttonFrame,
    text="Status",
    image=btnStatus,
    border="0",
    width=130,
    height=41,
    bg="#444444",
    fg="yellow",
    command=showStatus,
)

inventoryMenu = tk.Button(buttonFrame,
    text="Inventory",
    image=btnInventory,
    border="0",
    width=130,
    height=41,
    bg="#444444",
    fg="yellow",
    command=showInventory
)

exitButton = tk.Button(buttonFrame,
    text="Exit",
    image=btnExit,
    border="0",
    width=130,
    height=41,
    bg="#444444",
    fg="yellow",
    command=endScreen
)

mapsButton = tk.Button(buttonFrame,
    text="Map selection",
    image=btnMapEditor,
    border="0",
    width=130,
    height=41,
    bg="#444444",
    fg="yellow",
    command=mapSelection
)

controlMenu.pack()
#attackMenu.pack()
statusMenu.pack()
inventoryMenu.pack()
mapsButton.pack()
exitButton.pack()




root.mainloop()