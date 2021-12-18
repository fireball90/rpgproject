import tkinter as tk
import tkinter
from tkinter import *
from tkinter.constants import LEFT
from typing import Text
from PIL import Image, ImageTk
import os
from tkinter import filedialog
import sys

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

    applyMapButton = tk.Button(
        master=statusFrame, text="Use selected map", font=("Arial", 14), bg="#888888",fg="Red",
        command = clicker)
    applyMapButton.place(x=170,y=120)

    openMapEditorButton = tk.Button(
        master=statusFrame, text="Map editor", font=("Arial", 14), bg="#888888",fg="Red",
        command = mapEditor)
    openMapEditorButton.place(x=170,y=180)


def openMap():
    tf = filedialog.askopenfilename(
            initialdir="/levels", 
            title="Open Text file", 
            filetypes=(("Text Files", "*.txt"),)
            )
    global mapName, folderName
    mapName = os.path.basename(tf)
    folderName = os.path.basename(os.path.dirname(tf))
    print(folderName+"/"+mapName)
    openPath = Entry(statusFrame)
    openPath.place(x=100,y=30, width=260)
    openPath.insert(END, tf)

    

whateverNumber=0
def clicker():
    global whateverNumber
    whateverNumber=whateverNumber+1
    

def showControl():
    clearFrame()
    showbgpls()
    moveInfo = tk.Label(master=statusFrame, text="Moving options", font=("Arial", 20), bg="#888888", fg="Yellow")
    moveInfo.place(x=120, y=5)
    moveForward = tk.Button(
        master=statusFrame, text="Forward", font=("Arial", 16), bg="#888888",fg="Red",
        command = lambda:map.Update([0, -1])
        )
    moveForward.place(x=170, y=60)
    moveBackward = tk.Button(
        master=statusFrame, text="Backward", font=("Arial", 16), bg="#888888",fg="Red",
        command = lambda:[map.Update([0, 1])]
        )
    moveBackward.place(x=170, y=120)
    moveLeft = tk.Button(
        master=statusFrame, text="Left", font=("Arial", 16), bg="#888888",fg="Red",
        command = lambda:map.Update([-1, 0])
        )
    moveLeft.place(x=100, y=90)
    moveRight = tk.Button(
        master=statusFrame, text="Right", font=("Arial", 16), bg="#888888",fg="Red",
        command = lambda:map.Update([1, 0])
        )
    moveRight.place(x=290, y=90)

def showAttack():
    clearFrame()
    showbgpls()
    attackInfo = tk.Label(master=statusFrame, text="Attack options", font=("Arial", 20), bg="#888888", fg="Yellow")
    attackInfo.place(x=170, y=5)
    basicAttack = tk.Button(master=statusFrame, text="Basic attack", font=("Arial", 16), bg="#888888",fg="Red")
    basicAttack.place(x=170, y=60)
    heavyAttack = tk.Button(master=statusFrame, text="Heavy attack", font=("Arial", 16), bg="#888888",fg="Red")
    heavyAttack.place(x=170, y=120)
    specialAttack = tk.Button(master=statusFrame, text="Special attack", font=("Arial", 16), bg="#888888",fg="Red")
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

def fightScreen():
    clearFrame()
    enemyBG = tk.Canvas(enemyFrame,width=600,height=600)
    enemyBG.pack()
    fightLabel = tk.Label(enemyFrame, text="Enemy encounter!", font=("Arial", 16), background="#BBBBBB", fg="red")
    fightLabel.place(x=220,y=20)
    img3 = ImageTk.PhotoImage(Image.open("images/statusbg.jpg"))
    enemyBG.background = img3 
    bg3 = enemyBG.create_image(0, 0, anchor=tk.NW, image=img3)

    photo = tk.PhotoImage(file="images/zugzug.png")
    enemyFrame.photo = photo
    enemyBG.create_image(450, 80, image=photo, anchor=tk.NW)
    fightText=tk.Text(enemyFrame)
    fightText.place(x=20, y=70, width=400, height=300)

class Tile:
    def __init__(self, hitbox, sprite, level = 0):
        self.hitbox = hitbox
        self.sprite = sprite
        self.level = level

class Map:
    map = []
    map_canvas = tk.Canvas(mapPlease,width = 576, height = 600)

    player_actual_coord = {'x':0, 'y':0}

    sprites = (
        PhotoImage(file = 'sprites/side.gif').zoom(3),
        PhotoImage(file = 'sprites/roof.gif').zoom(3),
        PhotoImage(file = 'sprites/grass.gif').zoom(3),
        PhotoImage(file = 'sprites/enemygreen.gif').zoom(3),
        PhotoImage(file = 'sprites/enemyblue.gif').zoom(3),
        PhotoImage(file = 'sprites/enemyred.gif').zoom(3),
        PhotoImage(file = 'sprites/enemyboss.gif').zoom(3),
        PhotoImage(file = 'sprites/player.gif').zoom(3)
    )



    def Loading(self):
            if whateverNumber==0:
                map_name="levels/first_level.txt"
            else:
                openMap()
                map_name=(folderName+"/"+mapName)
            try:
                with open(map_name, 'r', encoding = 'utf-8') as file:
                    for i in range(24):
                        map_string = file.readline()
                        self.map.append([])

                        for j in range(24):
                            if map_string[j] == '#':
                                wall_vertical = Tile(True, self.sprites[0])
                                self.map[i].append(wall_vertical)

                            elif map_string[j] == '=':
                                wall_horizontal = Tile(True, self.sprites[1])
                                self.map[i].append(wall_horizontal)

                            elif map_string[j] == '.':
                                empty_field = Tile(False, self.sprites[2])
                                self.map[i].append(empty_field)

                            elif map_string[j] == '1':
                                enemy_level_1 = Tile(False, self.sprites[3] , 1)
                                self.map[i].append(enemy_level_1)

                            elif map_string[j] == '2':
                                enemy_level_2 = Tile(False, self.sprites[4] , 2)
                                self.map[i].append(enemy_level_2)

                            elif map_string[j] == '3':
                                enemy_level_3 = Tile(False, self.sprites[5] , 3)
                                self.map[i].append(enemy_level_3)

                            elif map_string[j] == '4':
                                enemy_level_4 = Tile(False, self.sprites[6] , 4)
                                self.map[i].append(enemy_level_4)   

                            elif map_string[j] == 'p':
                                self.player_actual_coord['x'] = j 
                                self.player_actual_coord['y'] = i 

                                player_object = Tile(False, self.sprites[7])
                                self.map[i].append(player_object)
                
            except:
                print('Hiba történt a pálya betöltése közben!')

    def Drawing(self):
        self.map_canvas.pack(expand=True, fill="both", padx=9, pady=10)

        for i in range(24):
            for j in range(24):
                self.map_canvas.create_image(j * 24, i * 24, image = self.map[i][j].sprite, anchor = NW)             

    def Update(self, movement_direction):
        player_new_x = self.player_actual_coord['x'] + movement_direction[0]
        player_new_y = self.player_actual_coord['y'] + movement_direction[1]

        level = self.map[player_new_y][player_new_x].level

        if not self.map[player_new_y][player_new_x].hitbox:
            self.map_canvas.delete('all')
            
            empty_field = Tile(False, self.sprites[2])
            self.map[self.player_actual_coord['y']][self.player_actual_coord['x']] = empty_field

            player_object = Tile(False, self.sprites[7])
            self.map[player_new_y][player_new_x] = player_object

            self.Drawing()

            self.player_actual_coord['x'] = player_new_x
            self.player_actual_coord['y'] = player_new_y

        return level

map = Map()
map.Loading()
map.Drawing()

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