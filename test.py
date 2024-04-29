import math, random

def randint(a, b):
    """Retourne un entier au hasard entre a et b inclut"""
    return int(random.random() * (b - a + 1)) + a


class Board:
    
    def __init__(self, col, row):
        self.row = row
        self.col = col
        self.wrong_move = 0
        self.grid = self.generate_2d_array(row, col, 0)

        self.generate_coins()

    def generate_2d_array(self, rows, cols, initial_value):
        array_2d = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(initial_value)
            array_2d.append(row)
        return array_2d
    
    def generate_coins(self):
        min_amount_coins = math.floor(self.col * self.row * 0.15)
        max_amount_coins = math.floor(self.col * self.row * 0.20)

        amount_coins = randint(min_amount_coins, max_amount_coins)

        while amount_coins > 0:
            row = randint(0, self.col - 1)
            col = randint(0, self.row - 1)
            if self.grid[row][col] == 0:
                self.grid[row][col] = "*"
                self.update_neighboring_tiles(row, col)
                amount_coins -= 1

        return self.grid
    
    def get_list_of_neighboring_tiles(self, x, y):
        return [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),   (x, y),   (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1)
        ]
        
    
    def get_amout_coins_in_neighboring_tiles(self, x, y):

        coins_amount = 0

        for neighboring_tile in self.get_list_of_neighboring_tiles(x, y):
            _x, _y = neighboring_tile[0], neighboring_tile[1]
            if not (0 <= _x < self.col) or not (0 <= _y < self.row):
                continue
            if self.grid[_x][_y] == '*':
                coins_amount += 1

        return coins_amount
    
    def update_neighboring_tiles(self, x, y):
        for neighboring_tile in self.get_list_of_neighboring_tiles(x, y):
            _x, _y = neighboring_tile[0], neighboring_tile[1]
            
            if not (0 <= _x < self.col) or not (0 <= _y < self.row):
                continue
            if self.grid[_x][_y] == '*':
                continue

            self.grid[_x][_y] += 1


    def generate_html_grid(self):
        html_grid = "<table>\n"
        
        for row in self.grid:
            html_grid += "<tr>"

            for tile in row:
                html_grid += "<td>" + str(tile) + "</td>"
            html_grid += "</tr>\n"
        
        html_grid += "</table>"
        
        return html_grid
    
