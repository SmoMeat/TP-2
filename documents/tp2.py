import math, random

# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

def init():
    global msg
    msg = document.querySelector('#main')
    msg.innerHTML = genereGrille()
    
    # main = document.querySelector("#main")
    # main.innerHTML = """
    #   <button onclick="init()">Nouvelle partie</button>
    #   <div id="jeu" class="centered">
    #   <table>
    #       <tr>
    #         <td id="case0"></td>
    #         <td id="case1"></td>
    #         <td id="case2"></td>         
    #       </tr>
    #       <tr>
    #         <td id="case6"></td>
    #         <td id="case7"></td>
    #         <td id="case8"></td>
    #       </tr>
    #     </table>
    #   </div>""" 

def clic():
    msg.innerHTML = '*' + msg.innerHTML + '*'


def table(contenu):
    return '<table>' + contenu + '</table>'

def td(contenu):
    return '<td>' + contenu + '</td>'

def tr(contenu):
    return '<tr>' + contenu + '</tr>'

def genereGrille():
    nombre_de_pieces = math.floor(random.random()*6) +15

    returnValue = ""

    for i in range(10):
        temp = ""
        for j in range(10):
            index = i*10 + j
            if random.random() < nombre_de_pieces/100:

                temp += td("<div><p>"+ str(index)+"</p></div>")
            else:
                temp += td("<div><p>"+"</p></div>")
            
        returnValue += tr(temp)

    return table(returnValue) + "<p>" + str(nombre_de_pieces) + "</p>"


class Board:
    def __init__(self, width=10, height=10):
        self.height = height
        self.width = width
        self.wrong_move = 0

    def generate_coins(self):
        [] * 

        

