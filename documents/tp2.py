# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

def init():
    main = document.querySelector("#main")
    main.innerHTML = """
      <button onclick="init()">Nouvelle partie</button>
      <div id="jeu" class="centered">
      <table>
          <tr>
            <td id="case0"></td>
            <td id="case1"></td>
            <td id="case2"></td>         
          </tr>
          <tr>
            <td id="case6"></td>
            <td id="case7"></td>
            <td id="case8"></td>
          </tr>
        </table>
      </div>""" 

      