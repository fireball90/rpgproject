import tkinter as tk
import tkinter
from tkinter import *
from tkinter.constants import LEFT
from typing import Text
from PIL import Image, ImageTk
import os
from tkinter import filedialog
import sys
import combat
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
        master=statusFrame, text="Open map", font=("Arial", 14), bg="#888888",fg="Red",
        command = openMap)
    openMapButton.place(x=170,y=60)
    
    openPath = Entry(statusFrame)
    openPath.place(x=100,y=30, width=260)

    openMapEditorButton = tk.Button(
        master=statusFrame, text="Map editor", font=("Arial", 14), bg="#888888",fg="Red",
        command = mapEditor)
    openMapEditorButton.place(x=170,y=180)

mapName=""
folderName=""

def openMap():
    tf = filedialog.askopenfilename(
            initialdir="/levels", 
            title="Open Text file", 
            filetypes=(("Text Files", "*.txt"),)
            )
    mapName = os.path.basename(tf)
    folderName = os.path.basename(os.path.dirname(tf))
    currentlyUsedMap=(folderName+"/"+mapName)
    openPath = Entry(statusFrame)
    openPath.place(x=100,y=30, width=260)
    openPath.insert(END, tf)
    
    buttonwhat= tk.Button(statusFrame, text="Use map",font=("Arial", 14), bg="#888888",fg="Red", command=lambda:[map.Loading(currentlyUsedMap),map.Drawing()])
    buttonwhat.place(x=170,y=120)

def buttonClicked(coords):
    tag = map.UpdatePlayer(coords)

    if tag == 'enemy_level_1':
        battlePlay()


def showControl():
    clearFrame()
    showbgpls()
    moveInfo = tk.Label(master=statusFrame, text="Moving options", font=("Arial", 20), bg="#888888", fg="Yellow")
    moveInfo.place(x=120, y=5)
    moveForward = tk.Button(
        master=statusFrame, text="Forward", font=("Arial", 16), bg="#888888",fg="Red",
        command = lambda:buttonClicked([-1, 0])
        )
    moveForward.place(x=170, y=60)
    moveBackward = tk.Button(
        master=statusFrame, text="Backward", font=("Arial", 16), bg="#888888",fg="Red",
        command = lambda:buttonClicked([1, 0])
        )
    moveBackward.place(x=170, y=120)
    moveLeft = tk.Button(
        master=statusFrame, text="Left", font=("Arial", 16), bg="#888888",fg="Red",
        command = lambda:buttonClicked([0, -1])
        )
    moveLeft.place(x=100, y=90)
    moveRight = tk.Button(
        master=statusFrame, text="Right", font=("Arial", 16), bg="#888888",fg="Red",
        command = lambda:buttonClicked([0, 1])
        )
    moveRight.place(x=290, y=90)

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

    damageStatus = tk.Label(master=statusFrame, text="Damage", font=("Arial", 20), bg="#888888", fg="Yellow")
    damageStatus.place(x=50, y=120)

    healthEntry = tk.Entry(master=statusFrame)
    healthEntry.insert(0,"Placeholder")
    healthEntry.place(x=240, y=70)
    damageEntry = tk.Entry(master=statusFrame)
    damageEntry.insert(0,"Placeholder")
    damageEntry.place(x=240, y=130)

def showInventory():
    clearFrame()
    showbgpls()
    inventoryInfo = tk.Label(master=statusFrame, text="Inventory", font=("Arial", 20), bg="#888888", fg="Yellow")
    inventoryInfo.place(x=170, y=5)
    healingItem = tk.Button(master=statusFrame, text="Healing item", font=("Arial", 16), bg="#888888",fg="Red")
    healingItem.place(x=170, y=60)

#A pálya kirajzolásához szükséges csempéknek, és a mozgó objektumoknak az osztályai
class Tile:
    def __init__(self, sprite, hitbox = False):
        self.sprite = sprite
        self.hitbox = hitbox

class Object:
    def __init__(self, sprite, tag):
        self.sprite = sprite
        self.tag = tag

class EnemyLevel1:
    def __init__(self, sprite, tag):
        self.sprite = sprite
        self.tag = tag

    step_direction_x = 1

    def nextStep(self, actual_coords, map_tiles, map_objects):
        new_coords = [actual_coords[0], actual_coords[1] + self.step_direction_x]

        if map_tiles[new_coords[0]][new_coords[1]].hitbox or map_objects[new_coords[0]][new_coords[1]] != 'empty':
            self.step_direction_x = -self.step_direction_x
            new_coords = [actual_coords[0], actual_coords[1] + self.step_direction_x]

        return new_coords

class EnemyLevel2:
    def __init__(self, sprite, tag):
        self.sprite = sprite
        self.tag = tag

    step_direction_y = 1

    def nextStep(self, actual_coords, map_tiles, map_objects):
        new_coords = [actual_coords[0] + self.step_direction_y, actual_coords[1]]

        if map_tiles[new_coords[0]][new_coords[1]].hitbox or map_objects[new_coords[0]][new_coords[1]] != 'empty':
            self.step_direction_y = -self.step_direction_y
            new_coords = [actual_coords[0] + self.step_direction_y, actual_coords[1]]
            

        return new_coords

class Map:
    map_canvas = tk.Canvas(mapPlease,width = 576, height = 600)
    map_tiles = []
    map_objects = []
    player_coords = []
    enemy_coords = []

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
                self.map_objects.append([])

                for j in range(24):
                    if map_string[j] == '*':
                        self.map_objects[i].append('empty')
                    elif map_string[j] == '1':
                        self.map_objects[i].append(EnemyLevel1(self.sprites[12], 'enemy_lvl_1'))
                        self.enemy_coords.append([i, j])
                    elif map_string[j] == '2':
                        self.map_objects[i].append(EnemyLevel2(self.sprites[13], 'enemy_lvl_2'))
                        self.enemy_coords.append([i, j])
                    elif map_string[j] == '3':
                        self.map_objects[i].append(Object(self.sprites[14], 'enemy_lvl_3'))
                        self.enemy_coords.append([i, j])
                    elif map_string[j] == '4':
                        self.map_objects[i].append(Object(self.sprites[15], 'enemy_lvl_4'))
                        self.enemy_coords.append([i, j])
                    elif map_string[j] == 'p':
                        self.map_objects[i].append(Object(self.sprites[16], 'player'))
                        self.player_coords = [i, j]
                    elif map_string[j] == 'f':
                        self.map_objects[i].append(Object(self.sprites[17], 'fire'))
                    elif map_string[j] == 'c':
                        self.map_objects[i].append(Object(self.sprites[18], 'chest'))
                    elif map_string[j] == 'b':
                        self.map_objects[i].append(Object(self.sprites[19], 'bandage'))
                    elif map_string[j] == 's':
                        self.map_objects[i].append(Object(self.sprites[20], 'star')) 

    def Drawing(self):
        self.map_canvas.pack(expand=True, fill="both", padx=9, pady=10)

        for i in range(24):
            for j in range(24):
                self.map_canvas.create_image(j * 24, i * 24, image = self.map_tiles[i][j].sprite, anchor = NW)

        for i in range(24):
            for j in range(24):
                if self.map_objects[i][j] != 'empty':
                    self.map_canvas.create_image(j * 24, i * 24, image = self.map_objects[i][j].sprite, anchor = NW)

    def UpdatePlayer(self, direction):
        tag = ''
        player_new_y = self.player_coords[0] + direction[0]
        player_new_x = self.player_coords[1] + direction[1]

        if not self.map_tiles[player_new_y][player_new_x].hitbox:
            if self.map_objects[player_new_y][player_new_x] != 'empty':
                level = self.map_objects[player_new_y][player_new_x].tag
            
            self.map_objects[self.player_coords[0]][self.player_coords[1]] = 'empty'
            self.map_objects[player_new_y][player_new_x] = Object(self.sprites[16], 5)

            self.map_canvas.delete('all')
            self.Drawing()

            self.player_coords = [player_new_y, player_new_x]

        return tag

    def UpdateEnemy(self):

        for i in range(len(self.enemy_coords)):
            enemy_new_coords = self.map_objects[self.enemy_coords[i][0]][self.enemy_coords[i][1]].nextStep(self.enemy_coords[i], self.map_tiles, self.map_objects)
            
            tmp_enemy = self.map_objects[self.enemy_coords[i][0]][self.enemy_coords[i][1]]
            self.map_objects[self.enemy_coords[i][0]][self.enemy_coords[i][1]] = 'empty'
            self.map_objects[enemy_new_coords[0]][enemy_new_coords[1]] = tmp_enemy

            self.enemy_coords[i] = enemy_new_coords
            
        self.map_canvas.delete('all')
        self.Drawing()
        self.map_canvas.after(1000, self.UpdateEnemy)

    def fightScreen(self):
        map.map_canvas.delete('all')
        enemyBG = tk.Canvas(enemyFrame,width=600,height=600)
        enemyBG.pack()
        fightLabel = tk.Label(enemyFrame, text="Enemy encounter!", font=("Arial", 16), background="#BBBBBB", fg="red")
        fightLabel.place(x=220,y=20)
        img3 = ImageTk.PhotoImage(Image.open("images/fightBG.gif"))
        enemyBG.background = img3 
        bg3 = enemyBG.create_image(0, 0, anchor=tk.NW, image=img3)

        photo = tk.PhotoImage(file="images/zugzug.png")
        enemyFrame.photo = photo
        enemyBG.create_image(450, 80, image=photo, anchor=tk.NW)
        fightText=tk.Text(enemyFrame)
        fightText.place(x=20, y=70, width=400, height=500)
        fightText.insert(END, combat)

map = Map()
map.Loading('maps/first_level.txt')
map.Drawing()
map.UpdateEnemy()


#################################################################################

#GOMBOK megjelenítése 

controlMenu = tk.Button(buttonFrame,
    text="Control",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
    command=showControl
)

attackMenu = tk.Button(buttonFrame,
    text="Attack",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
    command=showAttack
)

statusMenu = tk.Button(buttonFrame,
    text="Status",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
    command=showStatus,
)

inventoryMenu = tk.Button(buttonFrame,
    text="Inventory",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
    command=showInventory
)

exitButton = tk.Button(buttonFrame,
    text="Exit",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
    command=endScreen
)

mapsButton = tk.Button(buttonFrame,
    text="Map selection",
    width=20,
    height=2,
    bg="#555555",
    fg="yellow",
    command=mapSelection
)

controlMenu.pack()
attackMenu.pack()
statusMenu.pack()
inventoryMenu.pack()
mapsButton.pack()
exitButton.pack()




root.mainloop()