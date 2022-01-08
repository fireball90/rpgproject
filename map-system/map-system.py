from tkinter import *

window = Tk()
window.geometry('576x620')

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
        self.hitbox = False

    def NextStep(self, direction_x, direction_y, map_tiles, map_objects):
        new_x = self.x_coord + direction_x
        new_y = self.y_coord + direction_y

        if map_tiles[new_x][new_y].hitbox == False:
            self.x_coord = new_x
            self.y_coord = new_y
        
        for object in map_objects:
            if object.x_coord == self.x_coord and object.y_coord == self.y_coord:
                object.UpdateHealth(self.damage)

    def UpdateHealth(self, update_value):
        self.health += update_value

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

        if player_object.x_coord == self.x_coord and player_object.y_coord == self.y_coord:
            self.UpdateHealth(player_object.damage)

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

        if player_object.x_coord == self.x_coord and player_object.y_coord == self.y_coord:
            self.UpdateHealth(player_object.damage)

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

    def NextStep(self, map_tiles, map_objects, player_object):
        self.step_counter += 1

        if self.step_counter > 3:
            tmp = -self.step_direction_x
            self.step_direction_x = self.step_direction_y
            self.step_direction_y = tmp
            self.step_counter = 0

        self.x_coord += self.step_direction_x
        self.y_coord += self.step_direction_y

        if player_object.x_coord == self.x_coord and player_object.y_coord == self.y_coord:
            self.UpdateHealth(player_object.damage)
        

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
        self.damage = -60
        self.health = 100
        self.hitbox = True

    def NextStep(self, map_tiles, map_objects, player_object):
        pass

    def UpdateHealth(self, update_value):
        self.health += update_value

class Bandage:
    def __init__(self, sprite, x_coord, y_coord):
        self.sprite = sprite
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.name = 'Bandage'
        self.damage = 40
        self.health = 100
        self.hitbox = True

    def NextStep(self, map_tiles, map_objects, player_object):
        pass

    def UpdateHealth(self, update_value):
        self.health += update_value

class Map:
    map_canvas = Canvas(width = 576, height = 576)
    map_tiles = []
    map_objects = []
    player_object = None

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

        self.map_canvas.create_image(self.player_object.y_coord * 24, self.player_object.x_coord * 24, image = self.player_object.sprite, anchor = NW)

        for object in self.map_objects:
            if object.health > 0:
                self.map_canvas.create_image(object.y_coord * 24, object.x_coord * 24, image = object.sprite, anchor = NW)

    def Update(self):
        for object in self.map_objects:
            object.NextStep(self.map_tiles, self.map_objects, self.player_object)

        self.Drawing()
        map.map_canvas.after(1000, self.Update)

map = Map()
map.Loading('maps/third_level.txt')
map.Drawing()
map.Update()

def buttonClicked(direction_x, direction_y):
    map.player_object.NextStep(direction_x, direction_y, map.map_tiles, map.map_objects)
    map.Drawing()

up_arrow = Button(window, text = "↑", command = lambda:buttonClicked(-1, 0), padx = 10, pady = 10)
down_arrow = Button(window, text = "↓", command = lambda:buttonClicked(1, 0), padx = 10, pady = 10)
left_arrow = Button(window, text = "←", command = lambda:buttonClicked(0, -1), padx = 10, pady = 10)
right_arrow = Button(window, text = "→", command = lambda:buttonClicked(0, 1),  padx = 10, pady = 10)

up_arrow.place(x = 0, y = 576)
down_arrow.place(x = 35, y = 576)
left_arrow.place(x = 70, y = 576)
right_arrow.place(x = 109, y = 576)


window.mainloop()