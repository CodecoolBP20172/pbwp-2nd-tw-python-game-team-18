import random
import time
import sys
drawcounter = 0
gameend = 0 # ha egyre változik akkor vége a meccsnek.
xpoint = 0 # Pontszámok
ypoint = 0
B1 = '\033[1m' + '\033[33m'
B2 = '\033[1m' + '\033[34m'
B0 = '\033[0m' + '\033[0m'
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red

def check():# Minden lépés után itt ellenörzi hogy nem e nyert valaki.
    global gameend
#----------------------Ez az X játékost ellenörzi------------------------------
    if board[1] == "x" and board[2] == "x" and board[3] == "x":
        board[1] = B1 + "X" + B0
        board[2] = B1 + "X" + B0
        board[3] = B1 + "X" + B0
        print(O + "X won! " + W)
        gameend = gameend+1
    if board[7] == "x" and board[8] == "x" and board[9] == "x":
        board[7] = B1 + "X" + B0
        board[8] = B1 + "X" + B0
        board[9] = B1 + "X" + B0
        print(O + "X won!" + W)
        gameend = gameend+1
    if board[4] == "x" and board[5] == "x" and board[6] == "x":
        board[4] = B1 + "X" + B0
        board[5] = B1 + "X" + B0
        board[6] = B1 + "X" + B0
        print(O + "X won!" + W)
        gameend = gameend+1
    if board[3] == "x" and board[6] == "x" and board[9] == "x":
        board[3] = B1 + "X" + B0
        board[6] = B1 + "X" + B0
        board[9] = B1 + "X" + B0
        print(O + "X won!" + W)
        gameend = gameend+1
    if board[3] == "x" and board[5] == "x" and board[7] == "x":
        board[3] = B1 + "X" + B0
        board[5] = B1 + "X" + B0
        board[7] = B1 + "X" + B0
        print(O + "X won!" + W)
        gameend = gameend+1
    if board[2] == "x" and board[5] == "x" and board[8] == "x":
        board[2] = B1 + "X" + B0
        board[5] = B1 + "X" + B0
        board[8] = B1 + "X" + B0
        print(O + "X won!" + W)
        gameend = gameend+1
    if board[1] == "x" and board[4] == "x" and board[7] == "x":
        board[1] = B1 + "X" + B0
        board[4] = B1 + "X" + B0
        board[7] = B1 + "X" + B0
        print(O + "X won!" + W)
        gameend = gameend+1
    if board[1] == "x" and board[5] == "x" and board[9] == "x":
        board[1] = B1 + "X" + B0
        board[5] = B1 + "X" + B0
        board[9] = B1 + "X" + B0
        print(O + "X won!" + W)
        gameend = gameend+1
#----------------------Ez az O játékost ellenörzi------------------------------
    if board[1] == "o" and board[2] == "o" and board[3] == "o":
        board[1] = B2 + "O" + B0
        board[2] = B2 + "O" + B0
        board[3] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend+1
    if board[7] == "o" and board[8] == "o" and board[9] == "o":
        board[7] = B2 + "O" + B0
        board[8] = B2 + "O" + B0
        board[9] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend+1
    if board[4] == "o" and board[5] == "o" and board[6] == "o":
        board[4] = B2 + "O" + B0
        board[5] = B2 + "O" + B0
        board[6] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend+1
    if board[3] == "o" and board[6] == "o" and board[9] == "o":
        board[3] = B2 + "O" + B0
        board[6] = B2 + "O" + B0
        board[9] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend+1
    if board[3] == "o" and board[5] == "o" and board[7] == "o":
        board[3] = B2 + "O" + B0
        board[5] = B2 + "O" + B0
        board[7] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend+1
    if board[2] == "o" and board[5] == "o" and board[8] == "o":
        board[2] = B2 + "O" + B0
        board[5] = B2 + "O" + B0
        board[8] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend+1
    if board[1] == "o" and board[4] == "o" and board[7] == "o":
        board[1] = B2 + "O" + B0
        board[4] = B2 + "O" + B0
        board[7] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend+1
    if board[1] == "o" and board[5] == "o" and board[9] == "o":
        board[1] = B2 + "O" + B0
        board[5] = B2 + "O" + B0
        board[9] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend+1
    if drawcounter == 9 and gameend == 0:
        print("!DRAW!")
        gameend = gameend+1
#-----------------------A tábla felrajzolása-----------------------------------
def showtable():
    print(" ")
    print(" ", board[1], G +" | " + W , board[2], G +" | " + W ,  board[3],"\n")
    print(G + " ====|=====|==== " + W)
    print("")
    print(" ", board[4], G +" | " + W , board[5], G +" | " + W ,  board[6],"\n")
    print(G + " ====|=====|==== " + W)
    print("")
    print(" ", board[7], G +" | " + W , board[8], G +" | " + W ,  board[9],"\n")
    print("")
#-------------------------Igy rak X-et az 1. játékos---------------------------
def pickingX():
    global drawcounter
    drawcounter = drawcounter + 1
    showtable()
    while True:        # addig ismétli a kérdést, amig teljesül a feltétel
        try:
            n = int(input(O + "Player x turn: " + W))
        except ValueError:
            print(R + "Please give a number!" + W)
            continue
        while n >= 10 or n < 0:
            print(R + "Choose number between 1 - 9!" + W)
            break
        else:
            if board[n] !="x" and board[n] != "o":    # ellenőrzi hogy szám vagy betü-e az adott board
                if n == 0:
                    exit()
                break
            else:
                print(R+ "That square is already used!" + W)
    board[n]="x"
    print("\n")

           # X-re változik a board
#-------------------------Igy rak O-t a 2. játékos-----------------------------
def pickingO():
    global drawcounter
    drawcounter = drawcounter + 1
    showtable()
    while True:        # addig ismétli a kérdést amig teljesül a feltétel
        try:
            n = int(input(B + "Player O turn: " + W))
        except ValueError:
            print(R + "Please give a number!" + W)
            continue
        while n >= 10 or n < 0:
            print(R + "Choose number between 1 - 9!" + W)
            break
        else:
            if board[n] !="x" and board[n] != "o":   # itt ellenőrzi hogy szám vagy betű e az adott board
                if n == 0:
                    exit()
                break
            else:
                print(R+ "That square is already used!" + W)
    board[n]="o"          # O-ra változik a board
def pickingAI():          # igy rak O-t a bot.
    global drawcounter
    drawcounter = drawcounter + 1
    showtable()
    while True:
        n = random.randrange(1,9)      
        if board[n] !="x" and board[n] != "o":
            break
    for x in range (0,4):
        b = "Thinking" + "." * x
        print (b, end="\r")
        time.sleep(0.4)
    print("The bot's turn: " + str(n)) # kiírja mit választott a bot
    board[n]= "o"
    print("\n")

#-------------------------Itt indul a program----------------------------------
print("")
print(G + " ______   __     ______   " + O + "    ______   ______     ______   " + B + "    ______   ______     ______ " + B0)
print(G + "/\__  _\ /\ \   /\  ___\  " + O + "   /\__  _\ /\  __ \   /\  ___\  " + B + "   /\__  _\ /\  __ \   /\  ___\ " + B0)
print(G + "\/_/\ \/ \ \ \  \ \ \____ " + O + "   \/_/\ \/ \ \  __ \  \ \ \____ " + B + "   \/_/\ \/ \ \ \/\ \  \ \  __\ " + B0)
print(G + "   \ \_\  \ \_\  \ \_____\ " + O + "     \ \_\  \ \_\ \_\  \ \_____\ " + B + "     \ \_\  \ \_____\  \ \_____\ " + B0)
print(G + "    \/_/   \/_/   \/_____/" + O + "       \/_/   \/_/\/_/   \/_____/" + B + "       \/_/   \/_____/   \/_____/" + B0)
print("")
print("")
while True:      # addig megy amig be nem zárjuk a programot
    gameend = 0
    drawcounter = 0
    board = [0,1,2,3,4,5,6,7,8,9,10]
    n = 0
    bottrue = 0
    gamestart = input("Press " + G + "Y" + W +  " to start, or press " + R +"0" + W + " anytime to exit :")
    if gamestart == "0":
       exit()
    bot = input("Do you want to play againts a bot?" + G + "Y" + W + "/" + R +"N" + W+" ")
    if bot==("y"):
        bottrue = 1
    while(True):             # addig megy a mecs ameddig valaki nem nyer és breakel.
        while gameend == 0:  # addig megy a meccs, amig nincs vége(nem nyer valaki)
            pickingX()       # X rak
            check()          # ellenoriz
            if gameend == 1: # jatek vege
                if drawcounter == 9:
                    showtable()
                    break
                else:
                    showtable()
                    xpoint = xpoint + 1  # +1 pont a X-nek, mert az X körében lett vége
                    break                # kitör a loopbol
            if bottrue == 1:
                pickingAI()
            else:
                pickingO()           # Y rak
            check()                  # ellenoriz
            if gameend == 1:         # valaki nyert
                if drawcounter == 9:
                    showtable()
                    break
                else:
                    showtable()
                    ypoint = ypoint + 1  # +1 pont az Y-nak mert az Y körében lett vége
                    break                # kitör a loopbol

        else:
            print(O +"x points: "+str(xpoint))
            print(B +"y points: "+str(ypoint))
            print(W +"next round: ")
            break
