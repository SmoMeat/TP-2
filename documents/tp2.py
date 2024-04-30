"""tp2.py : Jeu de la cueillette de sous

Ce fichier permet d'animer une page html dans un navigateur web pour que l'utilisateur
puisse jouer au jeu de la cueillette de sous. C'est assez similaire à démineur, mais
ici on ne veut pas éviter les bombes, on veut plutot les trouver ! Le corps du jeu est
développer en python dans l'environement codeboot qui sert de traducteur pour que le code
soit interpreté directement dans le navigateur.

Afin de jouer, démarrer le serveur avec 'python serveur-web.py' et accéder ensuite
à l'adresse 'localhost:8000/tp2.html'.

@Date: 29 avril 2024
@Authors: Mathieu Ducharme & Loïc Buisson-Fechter
@Contacts: mathieu.ducharme@umontreal.ca & loic.buisson-fechter@umontreal.ca
"""

import random
import time

ROWS = 10
COLS = 10
RUN_UNIT_TEST = True

def init():
    """Initialise la page web avec la grille qui listen aux clics de l'utilisateur.
    Est appelé dès que la page initiale est chargée"""
    
    # Active les tests unitaires
    global RUN_UNIT_TEST
    if RUN_UNIT_TEST:
        run_tests()
        RUN_UNIT_TEST = False

    # Établit la structure du html
    main = document.querySelector("#main")
    main.innerHTML = """
        <div id="newGame"><button onclick="init()">Nouvelle partie</button></div>
        <div id="msg">Jouer!</div>
        <div id="errors">Erreurs: 0</div>
        <div id="coinsLeft"></div>
        <div id="grid">""" + generate_html_grid(ROWS, COLS) + """</div>
    """

    # Affiche le message
    global message_element
    message_element = document.querySelector('#msg')

    # Affiche la grille de jeu
    global grid
    grid = generate_grid(ROWS, COLS)
    update_html_grid()

    # Affiche le nombre d'erreur que le joueur a fait
    global errors, error_element
    errors = 0
    error_element = document.querySelector('#errors')

    # Affiche le nombre de pièce à trouver
    global coins_left, coins_left_element
    coins_left = coins_amount
    coins_left_element = document.querySelector('#coinsLeft')
    coins_left_element.innerHTML = 'Nombre de sous cachées: ' + str(coins_left)


def run_tests():
    """Execute les tests unitaires pour toutes les fonctions visées"""
    test_randint()
    test_generate_html_grid()
    test_generate_2d_array()
    test_generate_grid()
    test_get_list_of_neighboring_tiles()
    test_update_neighboring_tiles()


def randint(a, b):
    """Retourne un entier au hasard entre a et b inclut"""
    return int(random.random() * (b - a + 1)) + a


def test_randint():
    """Test unitaire de la fonction randint()"""
    assert randint(0, 0) == 0
    assert randint(10, 10) == 10
    assert randint(-3, -3) == -3
    for _ in range(100):
        assert 0 <= randint(0, 5) <= 5


def generate_html_grid(rows, cols):
    """Génère le html de la grille de jeu et la renvoie en string
    Args:
        rows (int): nombre de rangées de la matrice
        cols (int): nombre de colonnes de la matrice
    Returns:
        (str): code html de la grille
    """

    grid = ''

    for i in range(rows):
        row = ''
        for j in range(cols):
                index  = i * rows + j
                row += '<td id="tile'+str(index)+'" onclick="clic('+str(index)+')"></td>'
        grid += '<tr>' + row + '</tr>'

    return '<table>' + grid + '</table>'


def test_generate_html_grid():
    """Test unitaire de la fonction generate_html_grid()"""
    assert generate_html_grid(0, 0) == '<table></table>'
    assert generate_html_grid(0, 3) == '<table></table>'
    assert generate_html_grid(3, 0) == '<table><tr></tr><tr></tr><tr></tr></table>'
    assert generate_html_grid(1, 1) == '<table><tr><td id="tile0" onclick="clic(0)"></td></tr></table>'
    assert generate_html_grid(3, 3) == '<table><tr><td id="tile0" onclick="clic(0)"></td><td id="tile1" onclick="clic(1)"></td><td id="tile2" onclick="clic(2)"></td></tr><tr><td id="tile3" onclick="clic(3)"></td><td id="tile4" onclick="clic(4)"></td><td id="tile5" onclick="clic(5)"></td></tr><tr><td id="tile6" onclick="clic(6)"></td><td id="tile7" onclick="clic(7)"></td><td id="tile8" onclick="clic(8)"></td></tr></table>'


def generate_2d_array(rows, cols, initial_value):
    """Génère un array 2d définit par défaut. Fct nécessaire pour
    que chaque ligne ne soit pas simplement une référence de liste.
    Args:
        rows (int): nombre de rangées de la matrice
        cols (int): nombre de colonnes de la matrice
        initial_value (any): valeur par défaut des éléments
    Returns:
        array_2d (list[list[any]]): matrice définit par défaut
    """
    array_2d = []

    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(initial_value)
        array_2d.append(row)

    return array_2d


def test_generate_2d_array():
    """Test unitaire de la fonction generate_2d_array()"""
    assert generate_2d_array(0, 0, 0) == []
    assert generate_2d_array(0, 1, 0) == []
    assert generate_2d_array(1, 0, 0) == [[]]
    assert generate_2d_array(1, 1, 987) == [[987]]
    assert generate_2d_array(3, 3, '*') == [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]


def generate_grid(rows, cols):
    """Génère la grille de jeu avec les pièces et leurs indices autours.
    Args:
        rows (int): nombre de rangées de la grille
        cols (int): nombre de colonnes de la grille
    Returns:
        grid (list[list[any]]): matrice de la grille
    """
    grid = generate_2d_array(rows, cols, 0)

    min_amount_coins = int(rows * cols * 0.15)
    max_amount_coins = int(rows * cols * 0.20)

    # Définit le nombre de pièces à ramasser
    global coins_amount
    coins_amount = randint(min_amount_coins, max_amount_coins)
    coins_to_add = coins_amount

    while coins_to_add > 0:
        row = randint(0, rows - 1)
        col = randint(0, cols - 1)
        if grid[row][col] == 0:
            grid[row][col] = "*"
            grid = update_neighboring_tiles(grid, row, col)
            coins_to_add -= 1

    return grid


def test_generate_grid():
    """Test unitaire de la fonction generate_grid()"""
    assert generate_grid(0, 0) == []
    assert generate_grid(0, 1) == []
    assert generate_grid(1, 0) == [[]]
    assert generate_grid(1, 1) == [[0]]
    for _ in range(10):
        generate_grid(10, 10)
        assert 15 <= coins_amount <= 20


def get_list_of_neighboring_tiles(x, y):
    """Renvoie une liste des coordonnées des cases voisines.
    Args:
        x (int): coordonnée horizontale (colonne)
        y (int): coordonnée verticale (rangée)
    Returns:
        (list[tuple]): coordonnées (x, y)
    """
    return [
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y),   (x, y),   (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1)
    ]


def test_get_list_of_neighboring_tiles():
    """Test unitaire de la fonction get_list_of_neighboring_tiles()"""
    assert get_list_of_neighboring_tiles(1, 1) == [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
    assert get_list_of_neighboring_tiles(0, 0) == [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    assert get_list_of_neighboring_tiles(15, 15) == [(14, 14), (15, 14), (16, 14), (14, 15), (15, 15), (16, 15), (14, 16), (15, 16), (16, 16)]
    assert get_list_of_neighboring_tiles(-9, -9) == [(-10, -10), (-9, -10), (-8, -10), (-10, -9), (-9, -9), (-8, -9), (-10, -8), (-9, -8), (-8, -8)]
    assert get_list_of_neighboring_tiles(100, 100) == [(99, 99), (100, 99), (101, 99), (99, 100), (100, 100), (101, 100), (99, 101), (100, 101), (101, 101)]


def update_neighboring_tiles(grid, x, y):
    """Actualise les indices des cases voisines
    Args:
        grid (list[list]): grille 2d du jeu
        x (int): coordonnée horizontale (colonne)
        y (int): coordonnée verticale (rangée)
    Returns:
        grid (list[list]): grille avec les nouveaux indices
    
    """
    for neighboring_tile in get_list_of_neighboring_tiles(x, y):
        _x, _y = neighboring_tile[0], neighboring_tile[1]
        
        if not (0 <= _x < COLS) or not (0 <= _y < ROWS):
            continue
        if grid[_x][_y] == '*':
            continue

        grid[_x][_y] += 1
    
    return grid


def test_update_neighboring_tiles():
    """Test unitaire de la fonction update_neighboring_tiles()"""
    assert update_neighboring_tiles([['*',0,0],[0,0,0],[0,0,0]], 0, 0) == [['*', 1, 0], [1, 1, 0], [0, 0, 0]]
    assert update_neighboring_tiles([[0,0,0],[0,'*',0],[0,0,0]], 1, 1) == [[1, 1, 1], [1, '*', 1], [1, 1, 1]]
    assert update_neighboring_tiles([['*','*',1],[2,'*',1],[0,0,0]], 1, 1) == [['*', '*', 2], [3, '*', 2], [1, 1, 1]]
    assert update_neighboring_tiles([[0,0,1,'*',1],[2,2,2,1,1],['*','*',1,0,0],[3,'*',1,0,0],['*',1,0,0,0]], 3, 1) == [[0, 0, 1, '*', 1], [2, 2, 2, 1, 1], ['*', '*', 2, 0, 0], [4, '*', 2, 0, 0], ['*', 2, 1, 0, 0]]


def update_html_grid():
    """Actualise la grille de jeu affichée à partir de la position des pièces et de leurs indices"""
    for row in range(ROWS):
        for col in range(COLS):
            index = row * ROWS + col
            if grid[row][col] == '*':
                tile_element(index).innerHTML = '<img src="symboles/coste.svg" hidden="hidden">'
            elif grid[row][col] == 0:
                tile_element(index).innerHTML = ''
            else:
                tile_element(index).innerHTML = str(grid[row][col])


def tile_element(index):
    """Returne l'élément html de case n° index"""
    return document.querySelector('#tile' + str(index))


def clic(index):
    """Procédure lorsque l'utilisateur clique sur la case n° index"""
    x = index % COLS
    y = index // COLS
    
    # Le jouer a touché une pièce
    if grid[y][x] == "*":
        hit(index)

    # Le joueur a faire une erreur
    if grid[y][x] == 0:
        miss()

def hit(index):
    """Procédure lorsque le joueur a cliqué sur une pièce"""

    # Ajuste l'affichage du nombre de pièce à trouver
    global coins_left
    coins_left -= 1
    coins_left_element.innerHTML = 'Nombre des sous: ' + str(coins_left)

    # Affiche la pièce
    tile_element(index).innerHTML = '<img src="symboles/coste.svg" width="20" height="20">'

    # Regarde la condition de victoire
    if coins_left < 1:
        message_element.innerHTML = 'Vous avez gagné!'
        time.sleep(10)
        init()


def miss():
    """Procédure lorsque le joueur a cliqué sur une mauvaise case"""

    # Ajuste l'affiche du nombre d'erreurs
    global errors
    errors += 1
    error_element.innerHTML = 'Erreurs: ' + str(errors)

    # Regarde la condition de défaite
    if errors > 2:
        message_element.innerHTML = 'Vous avez perdu!'
        time.sleep(10)
        init()
