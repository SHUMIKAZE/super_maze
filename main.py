from pynput import keyboard
from math import sin, cos, pi
import time

import os

if os.name == "nt":
    os.system("mode con: cols=130 lines=40")

shader_loading = """
██████  ██   ██  █████  ██████  ███████ ██████      ██       ██████   █████  ██████  ██ ███    ██  ██████  
██      ██   ██ ██   ██ ██   ██ ██      ██   ██     ██      ██    ██ ██   ██ ██   ██ ██ ████   ██ ██       
███████ ███████ ███████ ██   ██ █████   ██████      ██      ██    ██ ███████ ██   ██ ██ ██ ██  ██ ██   ███ 
     ██ ██   ██ ██   ██ ██   ██ ██      ██   ██     ██      ██    ██ ██   ██ ██   ██ ██ ██  ██ ██ ██    ██ 
███████ ██   ██ ██   ██ ██████  ███████ ██   ██     ███████  ██████  ██   ██ ██████  ██ ██   ████  ██████
"""
connecting = """
██████  ██████   ███    ██ ███    ██ ███████  ██████ █████████ ██ ███    ██  ██████  
██      ██    ██ ████   ██ ████   ██ ██      ██         ██     ██ ████   ██ ██       
██      ██    ██ ██ ██  ██ ██ ██  ██ █████   ██         ██     ██ ██ ██  ██ ██   ███ 
██      ██    ██ ██  ██ ██ ██  ██ ██ ██      ██         ██     ██ ██  ██ ██ ██    ██ 
 ██████  ██████  ██   ████ ██   ████ ███████  ██████    ██     ██ ██   ████  ██████
"""
map_generation = """
███    ███  █████  ██████       ██████  ███████ ███    ██ ███████ ██████   █████  ████████ ██  ██████  ███    ██ 
████  ████ ██   ██ ██   ██     ██       ██      ████   ██ ██      ██   ██ ██   ██    ██    ██ ██    ██ ████   ██ 
██ ████ ██ ███████ ██████      ██   ███ █████   ██ ██  ██ █████   ██████  ███████    ██    ██ ██    ██ ██ ██  ██ 
██  ██  ██ ██   ██ ██          ██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██    ██    ██ ██    ██ ██  ██ ██ 
██      ██ ██   ██ ██           ██████  ███████ ██   ████ ███████ ██   ██ ██   ██    ██    ██  ██████  ██   ████
"""
rendering = """
██████  ███████ ███    ██ ██████  ███████ ██████  ██ ███    ██  ██████  
██   ██ ██      ████   ██ ██   ██ ██      ██   ██ ██ ████   ██ ██       
██████  █████   ██ ██  ██ ██   ██ █████   ██████  ██ ██ ██  ██ ██   ███ 
██   ██ ██      ██  ██ ██ ██   ██ ██      ██   ██ ██ ██  ██ ██ ██    ██ 
██   ██ ███████ ██   ████ ██████  ███████ ██   ██ ██ ██   ████  ██████
"""
congratulations = """
██████  ███████  ███    ██  ██████  ██████   █████  ████████ ██    ██ ██       █████  ████████ ██  ██████  ███    ██ ███████ 
██      ██    ██ ████   ██ ██       ██   ██ ██   ██    ██    ██    ██ ██      ██   ██    ██    ██ ██    ██ ████   ██ ██      
██      ██    ██ ██ ██  ██ ██   ███ ██████  ███████    ██    ██    ██ ██      ███████    ██    ██ ██    ██ ██ ██  ██ ███████ 
██      ██    ██ ██  ██ ██ ██    ██ ██   ██ ██   ██    ██    ██    ██ ██      ██   ██    ██    ██ ██    ██ ██  ██ ██      ██ 
 ██████  ██████  ██   ████  ██████  ██   ██ ██   ██    ██     ██████  ███████ ██   ██    ██    ██  ██████  ██   ████ ███████
"""
game_over = """
 ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
 ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██
"""
shubin_games = """
███████ ██   ██ ██    ██ ██████  ██ ███    ██      ██████   █████  ███    ███ ███████ ███████ 
██      ██   ██ ██    ██ ██   ██ ██ ████   ██     ██       ██   ██ ████  ████ ██      ██      
███████ ███████ ██    ██ ██████  ██ ██ ██  ██     ██   ███ ███████ ██ ████ ██ █████   ███████ 
     ██ ██   ██ ██    ██ ██   ██ ██ ██  ██ ██     ██    ██ ██   ██ ██  ██  ██ ██           ██ 
███████ ██   ██  ██████  ██████  ██ ██   ████      ██████  ██   ██ ██      ██ ███████ ███████ 

                      ██████  ██████  ███████ ███████ ███████ ███    ██ ████████ 
                      ██   ██ ██   ██ ██      ██      ██      ████   ██    ██    
                      ██████  ██████  █████   ███████ █████   ██ ██  ██    ██    
                      ██      ██   ██ ██           ██ ██      ██  ██ ██    ██    
                      ██      ██   ██ ███████ ███████ ███████ ██   ████    ██
"""
super_maze = """
███████ ██    ██ ██████  ███████ ██████      ███    ███  █████  ███████ ███████     ██████  
██      ██    ██ ██   ██ ██      ██   ██     ████  ████ ██   ██      ██ ██         ██  __██ 
███████ ██    ██ ██████  █████   ██████      ██ ████ ██ ███████     ██  █████      ██ ██ ██ 
     ██ ██    ██ ██      ██      ██   ██     ██  ██  ██ ██   ██    ██   ██         ██ ██  ██ 
███████  ██████  ██      ███████ ██   ██     ██      ██ ██   ██   █████ ███████    ██  ████ 

      ███████ ███    ██ ██████  ██      ███████ ███████ ███████     ███    ███  █████  ███████ ███████ 
      ██      ████   ██ ██   ██ ██      ██      ██      ██          ████  ████ ██   ██      ██ ██      
      █████   ██ ██  ██ ██   ██ ██      █████   ███████ ███████     ██ ████ ██ ███████     ██  █████   
      ██      ██  ██ ██ ██   ██ ██      ██           ██      ██     ██  ██  ██ ██   ██    ██   ██      
      ███████ ██   ████ ██████  ███████ ███████ ███████ ███████     ██      ██ ██   ██   █████ ███████
"""


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class SymbolGrid:
    def __init__(self, rows, cols, default_char="."):
        self.rows = rows
        self.cols = cols
        self.grid = [[default_char for _ in range(cols)] for _ in range(rows)]

    def display(self):
        for row in self.grid:
            print("".join(char * 2 for char in row))

    def set_symbol(self, row, col, char):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = char
        else:
            print("Ошибка: Индекс вне границ массива")


class Maze:
    def __init__(self):
        self.grid = SymbolGrid(16, 16, " ")
        self.map = """
        #  #############
        #  #     #     #
        #  #     #     #
        #  #  #  #  #  #
        #  #  #  #  #  #
        #  #  #  #  #  #
        #  #  #  #     #
        #     #  #     #
        #     #  #  #  #
        ####  #  #  #  #
        #     #     #  #
        #     #     #  #
        #  ##########  #
        #              #
        #              #
        ################
        """.strip().splitlines()
        self.wall = "█"

    def draw_map(self, player_x, player_y, player_sym):
        for row, row_line in enumerate(self.map):
            line = row_line.strip()
            for col, char in enumerate(line):
                if char != " ":
                    self.grid.set_symbol(row, col, self.wall)
                else:
                    self.grid.set_symbol(row, col, " ")
        self.grid.set_symbol(player_y, player_x, player_sym)


class Player:
    x, y = 2, 14
    direction = 270
    sym = "@"

    keys_pressed = {"left": False, "right": False, "up": False, "down": False}

    kill = 0


class Raycaster:
    def __init__(self):
        self.RAY_COUNT = 60
        self.SCREEN_HEIGHT = 24
        self.MAX_DISTANCE = 10
        self.FIELD_OF_VIEW = 90
        self.grid = SymbolGrid(self.SCREEN_HEIGHT, self.RAY_COUNT, " ")

    def cast_single_ray(self, ray_index, player_x, player_y, player_angle):
        relative_angle = (ray_index / self.RAY_COUNT) * self.FIELD_OF_VIEW - (
            self.FIELD_OF_VIEW / 2
        )
        ray_angle_rad = (player_angle + relative_angle) * pi / 180

        distance = 0
        step_size = 0.1

        while distance < self.MAX_DISTANCE:
            distance += step_size
            test_x = player_x + distance * cos(ray_angle_rad)
            test_y = player_y + distance * sin(ray_angle_rad)

            row = int(test_y)
            col = int(test_x)

            if (
                row < 0
                or row >= len(game_maze.map)
                or col < 0
                or col >= len(game_maze.map[0].strip())
            ):
                return self.MAX_DISTANCE

            if game_maze.map[row].strip()[col] == "#":
                return distance * cos(relative_angle * pi / 180)

        return self.MAX_DISTANCE

    def draw_vertical_line(self, ray_index, distance):
        if distance < 0.2:
            distance = 0.2

        line_height = int(self.SCREEN_HEIGHT / distance)

        if line_height > self.SCREEN_HEIGHT:
            line_height = self.SCREEN_HEIGHT

        start = (self.SCREEN_HEIGHT - line_height) // 2
        end = start + line_height

        for i in range(self.SCREEN_HEIGHT):
            if i < start:
                self.grid.grid[i][ray_index] = " "
            elif i < end:
                self.grid.grid[i][ray_index] = game_maze.wall
            else:
                self.grid.grid[i][ray_index] = "#"

    def cast_rays(self, player_x, player_y, player_angle):
        for ray_index in range(self.RAY_COUNT):
            distance = self.cast_single_ray(ray_index, player_x, player_y, player_angle)
            self.draw_vertical_line(ray_index, distance)

    def get_render_lines(self):
        return ["".join(row) for row in self.grid.grid]


game_maze = Maze()
game_maze.draw_map(int(Player.x), int(Player.y), Player.sym)
raycaster = Raycaster()
raycaster.cast_rays(Player.x, Player.y, Player.direction)


def on_press(key):
    try:
        if key == keyboard.Key.left:
            Player.keys_pressed["left"] = True
        elif key == keyboard.Key.right:
            Player.keys_pressed["right"] = True
        elif key == keyboard.Key.up:
            Player.keys_pressed["up"] = True
        elif key == keyboard.Key.down:
            Player.keys_pressed["down"] = True
    except AttributeError:
        pass


def on_release(key):
    if key == keyboard.Key.left:
        Player.keys_pressed["left"] = False
    elif key == keyboard.Key.right:
        Player.keys_pressed["right"] = False
    elif key == keyboard.Key.up:
        Player.keys_pressed["up"] = False
    elif key == keyboard.Key.down:
        Player.keys_pressed["down"] = False

    if key == keyboard.Key.esc:
        Player.kill = 1
        return False

if 0:
    clear()
    time.sleep(1)
    print(shubin_games)
    time.sleep(2)
    clear()
    print(super_maze)
    time.sleep(3)
    clear()
    print(" ")
    time.sleep(2)
    clear()
    print(shader_loading)
    time.sleep(2.5)
    clear()
    print(connecting)
    time.sleep(2.5)
    clear()
    print(map_generation)
    time.sleep(2)
    clear()
    print(rendering)
    time.sleep(3)

listener = keyboard.Listener(on_press=on_press, on_release=on_release, suppress=True)
listener.start()

first = 1
while True:
    if Player.kill == 1:
        break

    if first == 0:
        drawing = 0
    else:
        first = 0
        drawing = 1
    new_x, new_y = Player.x, Player.y

    if Player.keys_pressed["left"]:
        drawing = 1
        Player.direction = (Player.direction - 5) % 360
    if Player.keys_pressed["right"]:
        drawing = 1
        Player.direction = (Player.direction + 5) % 360

    move_step = 0.15
    angle_rad = Player.direction * pi / 180

    if Player.keys_pressed["up"]:
        new_x += move_step * cos(angle_rad)
        new_y += move_step * sin(angle_rad)
        drawing = 1
    if Player.keys_pressed["down"]:
        new_x -= move_step * cos(angle_rad)
        new_y -= move_step * sin(angle_rad)
        drawing = 1

    if drawing == 1:
        if (
            int(new_y) < 0
            or int(new_y) >= len(game_maze.map)
            or int(new_x) < 0
            or int(new_x) >= len(game_maze.map[0].strip())
        ):
            break

        target_char = game_maze.map[int(new_y)].strip()[int(new_x)]

        if target_char != "#":
            Player.x, Player.y = new_x, new_y

        game_maze.draw_map(int(Player.x), int(Player.y), Player.sym)
        raycaster.cast_rays(Player.x, Player.y, Player.direction)

        clear()

        print(f" POSITION: {Player.x:.1f}, {Player.y:.1f} | ANGLE: {Player.direction}°")
        print("=" * 120)

        maze_lines = ["".join(char * 2 for char in row) for row in game_maze.grid.grid]
        view_lines = raycaster.get_render_lines()

        for i in range(raycaster.SCREEN_HEIGHT):
            if i < 16:
                map_part = maze_lines[i]
            view_part = view_lines[i]
            print(f"{map_part}   |   {view_part}")

        print("=" * 120)
        print(" Controls: ARROW KEYS | ESC - Exit")
    time.sleep(0.03)

clear()
if Player.kill == 1:
    print(game_over)
else:
    print(congratulations)
