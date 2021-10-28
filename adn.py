# Loop code

from cell import *

class uwu:
    def __init__(self): # Required method
        pass
    def execute(self, args): # Required method
        f = open("uneditable", "w")
        text = args[0]
        f.write(text)
        f.close()
    def __str__(self): # Required method
        return "uwu"

content = """--sql
Notas:
1.0
7,0
3,0
4,5
"""

# Just once code

if __name__ == "__main__":

    adress = "adn"
    n = 10
    function = uwu
    args = [content]



    main = Cell(adress, adress, 0, n, function, args)
    main.reproduction()
    execute(main.newname)