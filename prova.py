# fatto da Nicolò Francescon

# indice
# mosse valide (45, 238)

Gioco = 1

dax = []
ax = []
day = []
ay = []

pezziB = ["P", "N", "B", "R", "Q", "K", "*"]
pezziN = ["p", "n", "b", "r", "q", "k", "*"]
pezzib = ["P", "N", "B", "R", "Q", "K"]
pezzin = ["p", "n", "b", "r", "q", "k"]

cavallox = [+2, +2, +1, +1, -1, -1, -2, -2]
cavalloy = [+1, -1, +2, -2, +2, -2, +1, -1]

rex = [+1, +1, +1, 0, 0, -1, -1, -1]
rey = [-1, 0, +1, +1, -1, -1, 0, +1]

arrocco = [1, 1]



def valida(x1,y1, x2, y2):
    dax.append(x1)
    day.append(y1)
    ax.append(x2)
    ay.append(y2)

scacchiera = [
              ['+', '-', '-', '-', '-', '-', '-', '-', '-', '+'],
              ['|', 'R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R', '|'],
              ['|', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', '|'],
              ['|', '*', '*', '*', '*', '*', '*', '*', '*', '|'],
              ['|', '*', '*', '*', '*', '*', '*', '*', '*', '|'],
              ['|', '*', '*', '*', '*', '*', '*', '*', '*', '|'],
              ['|', '*', '*', '*', '*', '*', '*', '*', '*', '|'],
              ['|', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', '|'],
              ['|', 'r', 'n', 'b', 'k', 'q', 'b', 'n', 'r', '|'],
              ['+', '_', '_', '_', '_', '_', '_', '_', '_', '+'],
              ]
valori = {'P': +100,'B': +300, 'N': +300, 'R': +500, 'Q': +900, 'K': +10000,
          'p': -100,'b': -300, 'n': -300, 'r': -500, 'q': -900, 'k': -10000}
# Gioco definisce se bianco o nero
if Gioco:
    for y in range(1, 9):
        for x in range(1, 9):
# Pedone
            if scacchiera[y][x] == "P":
                if scacchiera[y+1][x] == "*": # avanti di 1
                    valida(x, y, x, y+1)
                if y == 2:
                    if scacchiera[y+2][x] == "*": # avanti di 2 solo se siamo in casa base
                        valida(x, y, x, y+2)
                for pezzi in pezzin:
                    if scacchiera[y+1][x+1] == pezzi: # mangio a sx
                        valida(x, y, x+1, y+1)
                    if scacchiera[y+1][x-1] == pezzi: # mangio a dx
                        valida(x, y, x-1, y+1)
# Cavallo
            if scacchiera[y][x] == "N":
                for i in range(8):
                    for pezzi in pezziN:
                        if scacchiera[y+cavalloy[i]][x+cavallox[i]] == pezzi:
                            valida(x, y, x+cavallox[i], y+cavalloy[i])
# Alfiere
            if scacchiera[y][x] == "B":
                # ++
                for i in range(1, 9-max([y, x])):
                    if scacchiera[y+i][x+i] == "*":
                        valida(x, y, x+i, y+i)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y+i][x+i] == pezzi:
                                valida(x, y, x+i, y+i)
                                break
                        break
                # +-
                for i in range(1, min([9-y, x])):
                    if scacchiera[y+i][x-i] == "*":
                        valida(x, y, x-i, y+i)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y+i][x-i] == pezzi:
                                valida(x, y, x-i, y+i)
                                break
                        break
                # -+
                for i in range(1, max([8-y, x])):
                    if scacchiera[y-i][x+i] == "*":
                        valida(x, y, x+i, y-i)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y-i][x+i] == pezzi:
                                valida(x, y, x+i, y-i)
                                break
                        break
                # --
                for i in range(1, min([y, x])):
                    if scacchiera[y-i][x-i] == "*":
                        valida(x, y, x-i, y-i)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y-i][x-i] == pezzi:
                                valida(x, y, x-i, y-i)
                                break
                        break
# Torre
            if scacchiera[y][x] == "R":
                # +y
                for i in range(1, 9-y):
                    if scacchiera[y + i][x] == "*":
                        valida(x, y, x, y + i)
                        print("cioa")
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y + i][x] == pezzi:
                                valida(x, y, x, y + i)
                                break
                        break
                # -y
                for i in range(1, y):
                    if scacchiera[y - i][x] == "*":
                        valida(x, y, x, y - i)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y - i][x] == pezzi:
                                valida(x, y, x, y - i)
                                break
                        break
                # -x
                for i in range(1, x):
                    if scacchiera[y][x-i] == "*":
                        valida(x, y, x-i, y)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y][x-i] == pezzi:
                                valida(x, y, x-i, y)
                                break
                        break
                # +x
                for i in range(1, 9 - x):
                    if scacchiera[y][x+i] == "*":
                        valida(x, y, x+i, y)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y][x+i] == pezzi:
                                valida(x, y, x+i, y)
                                break
                        break
# Regina
            if scacchiera[y][x] == "Q":
                #++
                for i in range(1, 9-max([y, x])):
                    if scacchiera[y+i][x+i] == "*":
                        valida(x, y, x+i, y+i)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y+i][x+i] == pezzi:
                                valida(x, y, x+i, y+i)
                                break
                        break
                #+-
                for i in range(1, min([9-y, x])):
                    if scacchiera[y+i][x-i] == "*":
                        valida(x, y, x-i, y+i)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y+i][x-i] == pezzi:
                                valida(x, y, x-i, y+i)
                                break
                        break
                #-+
                for i in range(1, max([8-y, x])):
                    if scacchiera[y-i][x+i] == "*":
                        valida(x, y, x+i, y-i)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y-i][x+i] == pezzi:
                                valida(x, y, x+i, y-i)
                                break
                        break
                #--
                for i in range(1, min([y, x])):
                    if scacchiera[y-i][x-i] == "*":
                        valida(x, y, x-i, y-i)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y-i][x-i] == pezzi:
                                valida(x, y, x-i, y-i)
                                break
                        break
                # +y
                for i in range(1, 9 - y):
                    if scacchiera[y + i][x] == "*":
                        valida(x, y, x, y + i)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y + i][x] == pezzi:
                                valida(x, y, x, y + i)
                                break
                        break
                # -y
                for i in range(1, y):
                    if scacchiera[y - i][x] == "*":
                        valida(x, y, x, y - i)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y - i][x] == pezzi:
                                valida(x, y, x, y - i)
                                break
                        break
                # -x
                for i in range(1, x):
                    if scacchiera[y][x - i] == "*":
                        valida(x, y, x - i, y)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y][x - i] == pezzi:
                                valida(x, y, x - i, y)
                                break
                        break
                # +x
                for i in range(1, 9 - x):
                    if scacchiera[y][x + i] == "*":
                        valida(x, y, x + i, y)
                    else:
                        for pezzi in pezzin:
                            if scacchiera[y][x + i] == pezzi:
                                valida(x, y, x + i, y)
                                break
                        break
# Re
            if scacchiera[y][x] == "K":
                for i in range(8):
                    for pezzi in pezziN:
                        if scacchiera[y + rey[i]][x + rex[i]] == pezzi:
                            valida(x, y, x + rex[i], y + rey[i])


print(day, ay)
print(dax, ax)




