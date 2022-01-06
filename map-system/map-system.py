from tkinter import *

window = Tk()
window.geometry('576x620')

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

        if map_tiles[new_coords[0]][new_coords[1]].hitbox or map_objects[new_coords[0]][new_coords[1]].tag != 'empty':
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

        if map_tiles[new_coords[0]][new_coords[1]].hitbox or map_objects[new_coords[0]][new_coords[1]].tag != 'empty':
            self.step_direction_y = -self.step_direction_y
            new_coords = [actual_coords[0] + self.step_direction_y, actual_coords[1]]
            
        return new_coords

class Map:
    map_canvas = Canvas(width = 576, height = 576)
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
                        self.map_objects[i].append(Object('empty', 'empty'))
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
        self.map_canvas.pack(expand=YES, fill=BOTH)
        self.map_canvas.delete('all')

        for i in range(24):
            for j in range(24):
                self.map_canvas.create_image(j * 24, i * 24, image = self.map_tiles[i][j].sprite, anchor = NW)

        for i in range(24):
            for j in range(24):
                if self.map_objects[i][j].tag != 'empty':
                    self.map_canvas.create_image(j * 24, i * 24, image = self.map_objects[i][j].sprite, anchor = NW)

    def UpdatePlayer(self, direction):
        pass
    def UpdateEnemy(self):
        for i in range(len(self.enemy_coords)):
            enemy_new_coords = self.map_objects[self.enemy_coords[i][0]][self.enemy_coords[i][1]].nextStep(self.enemy_coords[i], self.map_tiles, self.map_objects)
            
            if enemy_new_coords == self.player_coords:
                self.enemy_coords.pop(i)
                self.map_objects[self.enemy_coords[i][0]][self.enemy_coords[i][1]] = Object('empty', 'empty')
                print('harc')
            else:
                tmp_enemy = self.map_objects[self.enemy_coords[i][0]][self.enemy_coords[i][1]]
                self.map_objects[self.enemy_coords[i][0]][self.enemy_coords[i][1]] = Object('empty', 'empty')
                self.map_objects[enemy_new_coords[0]][enemy_new_coords[1]] = tmp_enemy
                self.enemy_coords[i] = enemy_new_coords
            
        self.map_canvas.delete('all')
        self.Drawing()
        self.map_canvas.after(1000, self.UpdateEnemy)
    
map = Map()
map.Loading('maps/first_level.txt')
map.Drawing()
map.UpdateEnemy()


up_arrow = Button(window, text = "↑", command = lambda:map.UpdatePlayer([-1, 0]), padx = 10, pady = 10)
down_arrow = Button(window, text = "↓", command = lambda:map.UpdatePlayer([1, 0]), padx = 10, pady = 10)
left_arrow = Button(window, text = "←", command = lambda:map.UpdatePlayer([0, -1]), padx = 10, pady = 10)
right_arrow = Button(window, text = "→", command = lambda:map.UpdatePlayer([0, 1]), padx = 10, pady = 10)

up_arrow.place(x = 0, y = 576)
down_arrow.place(x = 35, y = 576)
left_arrow.place(x = 70, y = 576)
right_arrow.place(x = 109, y = 576)


window.mainloop()