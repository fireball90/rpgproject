from tkinter import *


window = Tk()


class Tile:
    def __init__(self, hitbox, sprite, level = 0):
        self.hitbox = hitbox
        self.sprite = sprite
        self.level = level

class Map:
    map = []
    map_canvas = Canvas(width = 638, height = 638)

    player_actual_coord = {'x':0, 'y':0}

    sprites = (
        PhotoImage(file = 'sprites/side.gif').zoom(4),
        PhotoImage(file = 'sprites/roof.gif').zoom(4),
        PhotoImage(file = 'sprites/grass.gif').zoom(4),
        PhotoImage(file = 'sprites/enemygreen.gif').zoom(4),
        PhotoImage(file = 'sprites/enemyblue.gif').zoom(4),
        PhotoImage(file = 'sprites/enemyred.gif').zoom(4),
        PhotoImage(file = 'sprites/enemyboss.gif').zoom(4),
        PhotoImage(file = 'sprites/player.gif').zoom(4)
    )

    def Loading(self, map_name):
            try:
                with open(map_name, 'r', encoding = 'utf-8') as file:
                    for i in range(20):
                        map_string = file.readline()
                        self.map.append([])
                        
                        for j in range(20):
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
        self.map_canvas.pack(expand=YES, fill=BOTH)

        for i in range(20):
            for j in range(20):
                self.map_canvas.create_image(j * 32, i * 32, image = self.map[i][j].sprite, anchor = NW)                

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
map.Loading('levels/first_level.txt')
map.Drawing()

left = Button(text = 'left', command = lambda:map.Update([-1, 0]))
right = Button(text = 'right', command = lambda:map.Update([1, 0]))
up = Button(text = 'up', command = lambda:map.Update([0, -1]))
down = Button(text = 'down', command = lambda:map.Update([0, 1]))

left.pack()
right.pack()
up.pack()
down.pack()

window.mainloop()