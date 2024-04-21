import math
import random

class Board:
    def __init__(self, width=10, height=10):
        self.height = height
        self.width = width
        self.wrong_move = 0
        self.grid = [[0] * self.width] * self.height
        self.generate_coins()

        print(self.grid)

    def generate_coins(self):
        min_amount_coins = math.floor(self.width * self.height * 0.15)
        max_amount_coins = math.floor(self.width * self.height * 0.20)
        current_amount_coins = 0

        while min_amount_coins <= current_amount_coins <= max_amount_coins: 
            grid = [[0] * self.width] * self.height
            current_amount_coins = 0
            for x in self.width:
                for y in self.height:
                    if random.random < 0.175 and self.get_tile_value(x, y):
                        grid[x][y] = '*'
                        current_amount_coins += 1
        print(grid)
        return self.grid
    
    def get_tile_value(self, x, y):
        neighboring_tiles = [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),   (x, y),   (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1)
        ]
        tile_value = 0
        for neighboring_tile in neighboring_tiles:
            x = neighboring_tile[0]
            y = neighboring_tile[1]
            if x < 1 or x > self.width or y < 1 or y > self.height:
                continue
            if self.grid[x][y] == '*':
                tile_value += 1
        return tile_value

x = Board()