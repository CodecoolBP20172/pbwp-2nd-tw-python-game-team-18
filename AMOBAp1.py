import random
import time
import sys
import os
import time
drawcounter = 0
gameend = 0  # ha egyre változik akkor vége a meccsnek.
xpoint = 0  # Pontszámok
ypoint = 0
B1 = '\033[1m' + '\033[33m'
B2 = '\033[1m' + '\033[34m'
B0 = '\033[0m' + '\033[0m'
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red


def check():  # Minden lépés után itt ellenörzi hogy nem e nyert valaki.
    global gameend
#----------------------Ez az X játékost ellenörzi------------------------------
    if board[1] == "x" and board[2] == "x" and board[3] == "x":
        board[1] = B1 + "X" + B0
        board[2] = B1 + "X" + B0
        board[3] = B1 + "X" + B0
        print(O + "X won! " + W)
        gameend = gameend + 1
    if board[7] == "x" and board[8] == "x" and board[9] == "x":
        board[7] = B1 + "X" + B0
        board[8] = B1 + "X" + B0
        board[9] = B1 + "X" + B0
        print(O + "X won!" + W)
        gameend = gameend + 1
    if board[4] == "x" and board[5] == "x" and board[6] == "x":
        board[4] = B1 + "X" + B0
        board[5] = B1 + "X" + B0
        board[6] = B1 + "X" + B0
        print(O + "X won!" + W)
        gameend = gameend + 1
    if board[3] == "x" and board[6] == "x" and board[9] == "x":
        board[3] = B1 + "X" + B0
        board[6] = B1 + "X" + B0
        board[9] = B1 + "X" + B0
        print(O + "X won!" + W)
        gameend = gameend + 1
    if board[3] == "x" and board[5] == "x" and board[7] == "x":
        board[3] = B1 + "X" + B0
        board[5] = B1 + "X" + B0
        board[7] = B1 + "X" + B0
        print(O + "X won!" + W)
        gameend = gameend + 1
    if board[2] == "x" and board[5] == "x" and board[8] == "x":
        board[2] = B1 + "X" + B0
        board[5] = B1 + "X" + B0
        board[8] = B1 + "X" + B0
        print(O + "X won!" + W)
        gameend = gameend + 1
    if board[1] == "x" and board[4] == "x" and board[7] == "x":
        board[1] = B1 + "X" + B0
        board[4] = B1 + "X" + B0
        board[7] = B1 + "X" + B0
        print(O + "X won!" + W)
        gameend = gameend + 1
    if board[1] == "x" and board[5] == "x" and board[9] == "x":
        board[1] = B1 + "X" + B0
        board[5] = B1 + "X" + B0
        board[9] = B1 + "X" + B0
        print(O + "X won!" + W)
        gameend = gameend + 1
#----------------------Ez az O játékost ellenörzi------------------------------
    if board[1] == "o" and board[2] == "o" and board[3] == "o":
        board[1] = B2 + "O" + B0
        board[2] = B2 + "O" + B0
        board[3] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend + 1
    if board[7] == "o" and board[8] == "o" and board[9] == "o":
        board[7] = B2 + "O" + B0
        board[8] = B2 + "O" + B0
        board[9] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend + 1
    if board[4] == "o" and board[5] == "o" and board[6] == "o":
        board[4] = B2 + "O" + B0
        board[5] = B2 + "O" + B0
        board[6] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend + 1
    if board[3] == "o" and board[6] == "o" and board[9] == "o":
        board[3] = B2 + "O" + B0
        board[6] = B2 + "O" + B0
        board[9] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend + 1
    if board[3] == "o" and board[5] == "o" and board[7] == "o":
        board[3] = B2 + "O" + B0
        board[5] = B2 + "O" + B0
        board[7] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend + 1
    if board[2] == "o" and board[5] == "o" and board[8] == "o":
        board[2] = B2 + "O" + B0
        board[5] = B2 + "O" + B0
        board[8] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend + 1
    if board[1] == "o" and board[4] == "o" and board[7] == "o":
        board[1] = B2 + "O" + B0
        board[4] = B2 + "O" + B0
        board[7] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend + 1
    if board[1] == "o" and board[5] == "o" and board[9] == "o":
        board[1] = B2 + "O" + B0
        board[5] = B2 + "O" + B0
        board[9] = B2 + "O" + B0
        print(B + "Y won!" + W)
        gameend = gameend + 1
    if drawcounter == 9 and gameend == 0:
        print("!DRAW!")
        gameend = gameend + 1
#-----------------------A tábla felrajzolása-----------------------------------


def showtable():
    print(" ")
    print(
        " ",
        board[1],
        G + " | " + W,
        board[2],
        G + " | " + W,
        board[3],
        "\n")
    print(G + " ====|=====|==== " + W)
    print("")
    print(
        " ",
        board[4],
        G + " | " + W,
        board[5],
        G + " | " + W,
        board[6],
        "\n")
    print(G + " ====|=====|==== " + W)
    print("")
    print(
        " ",
        board[7],
        G + " | " + W,
        board[8],
        G + " | " + W,
        board[9],
        "\n")
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
            # ellenőrzi hogy szám vagy betü-e az adott board
            if board[n] != "x" and board[n] != "o":
                if n == 0:
                    exit()
                break
            else:
                print(R + "That square is already used!" + W)
    board[n] = "x"
    print("\n")

def pickingXM():
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
            # ellenőrzi hogy szám vagy betü-e az adott board
            if board[n] != "x" and board[n] != "o":
                if n == 0:
                    exit()
                break
            else:
                print(R + "That square is already used!" + W)
    with open("file.txt", "w") as text_file:
        text_file.write (str(n))
    board[n] = "x"
    print("\n")
    showtable()

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
            # itt ellenőrzi hogy szám vagy betű e az adott board
            if board[n] != "x" and board[n] != "o":
                if n == 0:
                    exit()
                break
            else:
                print(R + "That square is already used!" + W)
    board[n] = "o"          # O-ra változik a board

def pickingOM():
    global drawcounter
    drawcounter = drawcounter + 1
    fileName = 'file.txt'
    originalTime = os.path.getmtime(fileName)
    potty = 0
    while True:        # addig ismétli a kérdést amig teljesül a feltétel
        if(os.path.getmtime(fileName) > originalTime):
            with open(fileName, 'r') as f:
                n = int(f.read())
                break
            originalTime = os.path.getmtime(fileName)
        b = " Waiting for the answer" + "." * potty + "   "
        print(b,end = "\r")
        time.sleep(3.5)
        if potty < 3:
            potty +=1
        else:
            potty = 0
    board[n] = "o"
    #time.sleep(0.1)          # O-ra változik a board
    print("                                                       ")
    print("Y choose = " + str(n))
def pickingAI():          # igy rak O-t a bot.
    global drawcounter
    drawcounter = drawcounter + 1
    showtable()
    while True:
        # addig ismétli a kérdést, amig teljesül a feltétel
        n = random.randrange(1, 9)
        if board[n] != "x" and board[n] != "o":
            break
    print("The bot's turn: " + str(n))  # kiírja mit választott a bot
    board[n] = "o"
    print("\n")


#-------------------------Itt indul a program----------------------------------
print("")
print(
    G +
    " ______   __     ______   " +
    O +
    "    ______   ______     ______   " +
    B +
    "    ______   ______     ______ " +
    B0)
print(
    G +
    "/\__  _\ /\ \   /\  ___\  " +
    O +
    "   /\__  _\ /\  __ \   /\  ___\  " +
    B +
    "   /\__  _\ /\  __ \   /\  ___\ " +
    B0)
print(
    G +
    "\/_/\ \/ \ \ \  \ \ \____ " +
    O +
    "   \/_/\ \/ \ \  __ \  \ \ \____ " +
    B +
    "   \/_/\ \/ \ \ \/\ \  \ \  __\ " +
    B0)
print(
    G +
    "   \ \_\  \ \_\  \ \_____\ " +
    O +
    "     \ \_\  \ \_\ \_\  \ \_____\ " +
    B +
    "     \ \_\  \ \_____\  \ \_____\ " +
    B0)
print(
    G +
    "    \/_/   \/_/   \/_____/" +
    O +
    "       \/_/   \/_/\/_/   \/_____/" +
    B +
    "       \/_/   \/_____/   \/_____/" +
    B0)
print("")
print("")
while True:      # addig megy amig be nem zárjuk a programot
    with open("file.txt", "w") as text_file:
        text_file.write (" ")
    multiplayer = 0
    local = 0
    gameend = 0
    drawcounter = 0
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 0
    bottrue = 0
    player = 0
    answer = ""
    gamestart = input(
        "Press " +
        G +
        "Y" +
        W +
        " to start, or press " +
        R +
        "0" +
        W +
        " anytime to exit :")
    if gamestart == "0":
        exit()
    while bottrue == 0 and local == 0 and multiplayer == 0:
        answer = input("Do you want to play againts a bot or local or multiplayer" +
                    G + "B" + W + "/" + R + "L" + W + "/" + B + "M" + W)
        if answer == ("B"):
            bottrue = 1
        elif answer == ("L"):
            local = 1
        elif answer == ("M"):
            multiplayer = 1
        else:
            print("Wrong answer!")
    player = input("choose 1 or 2")
    if player == str(1):
        with open("file.txt", "r") as f:
            content = f.read()
        if content == "z":
            print("the other player have already chosen!")
            player = 2
        with open("file.txt", "w") as text_file:
            text_file.write ("z")
    elif player == str(2):
        with open("file.txt", "r") as f:
            content = f.read()
        if content == "i":
            print("the other player have already chosen!")
            player = 1
        with open("file.txt", "w") as text_file:
            text_file.write ("i")
    else:
        print("PLS")
    player = int(player)
    # addig megy a mecs ameddig valaki nem nyer és breakel.
    while(True):
        if multiplayer == 1:
            if player == 1:
                # addig megy a meccs, amig nincs vége(nem nyer valaki)
                while gameend == 0:
                    pickingXM()       # X rak
                    check()          # ellenoriz
                    if gameend == 1:  # jatek vege
                        if drawcounter == 9:
                            showtable()
                            break
                        else:
                            showtable()
                            #xpoint = xpoint + 1  # +1 pont a X-nek, mert az X körében lett vége
                            break                # kitör a loopbol
                    else:
                        pickingOM()           # Y rak
                    check()                  # ellenoriz
                    if gameend == 1:         # valaki nyert
                        if drawcounter == 9:
                            showtable()
                            break
                        else:
                            showtable()
                            #ypoint = ypoint + 1  # +1 pont az Y-nak mert az Y körében lett vége
                            break                # kitör a loopbol
            if player == 2:
                 # addig megy a meccs, amig nincs vége(nem nyer valaki)
                while gameend == 0:
                    pickingOM()       # X rak
                    check()          # ellenoriz
                    if gameend == 1:  # jatek vege
                        if drawcounter == 9:
                            showtable()
                            break
                        else:
                            showtable()
                            #xpoint = xpoint + 1  # +1 pont a X-nek, mert az X körében lett vége
                            break                # kitör a loopbol
                    else:
                        pickingXM()           # Y rak
                    check()                  # ellenoriz
                    if gameend == 1:         # valaki nyert
                        if drawcounter == 9:
                            showtable()
                            break
                        else:
                            showtable()
                            #ypoint = ypoint + 1  # +1 pont az Y-nak mert az Y körében lett vége
                            break                # kitör a loopbol

        else:
            while gameend == 0:
                pickingX()       # X rak
                check()          # ellenoriz
                if gameend == 1:  # jatek vege
                    if drawcounter == 9:
                        showtable()
                        break
                    else:
                        showtable()
                        #xpoint = xpoint + 1  # +1 pont a X-nek, mert az X körében lett vége
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
                        #ypoint = ypoint + 1  # +1 pont az Y-nak mert az Y körében lett vége
                        break                # kitör a loopbol

        #print(O + "x points: " + str(xpoint))
        #print(B + "y points: " + str(ypoint))
        print(W + "next round: ")
        break
