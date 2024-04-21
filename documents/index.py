
import math
import random

def init():
    global msg
    msg = document.querySelector('#msg')
    msg.innerHTML = 'bonjour'

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