import numpy as np
import random
import time
import sys
import os
import pygame
pygame.init()

#intro_sound = pygame.mixer.Sound("amoba_theme_2.wav")
#amoba_bckgrnd_music = pygame.mixer.Sound("amoba_theme_2.wav")
picking_sound = pygame.mixer.Sound("picking.wav")
error_sound = pygame.mixer.Sound("error.wav")
win_sound = pygame.mixer.Sound("win.wav")

B1 = '\033[1m' + '\033[33m'
B2 = '\033[1m' + '\033[34m'
B0 = '\033[0m' + '\033[0m'
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red

def showtable():
    print(" ")
    print(" ", table[0][0], G +" | " + W , table[0][1], G +" | " + W ,  table[0][2],"\n")
    print(G + " ====|=====|==== " + W)
    print("")
    print(" ", table[1][0], G +" | " + W , table[1][1], G +" | " + W ,  table[1][2],"\n")
    print(G + " ====|=====|==== " + W)
    print("")
    print(" ", table[2][0], G +" | " + W , table[2][1], G +" | " + W ,  table[2][2],"\n")
    print("")

def check_rows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def check_diagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0

def check_win(board):
    #transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = check_rows(newBoard)
        if result:
            return result
    return check_diagonals(board)

def table_full(table):
    new_table=[]
    for row in range(3):
        for oszlop in range(3):
            new_table.append(table[row][oszlop])
    return len(set(new_table)) == 2

def picking_x(multiplayer = 0):
    showtable()
    while True:
        try:
            n = int(input(O + "Player X turn: " + W))
            picking_sound.play()
        except ValueError:
            picking_sound.stop()
            error_sound.play()
            print(R + "Choose a number between 1 - 9!" + W)
            continue
        if n >9 or n < 0:
            picking_sound.stop()
            error_sound.play()
            print(R + "Choose number between 1 - 9!" + W)
        else:
            if n>0 and n<=3:
                if table[0][n-1] == "X" or table[0][n-1] == "O":
                    picking_sound.stop()
                    error_sound.play()
                    print(R+ "That spot is already taken: " + W)
                else:
                    table[0][n-1]="X"
                    break
            if n>=4 and n<=6:
                if table[1][n-4] == "X" or table[1][n-4] == "O":
                    picking_sound.stop()
                    error_sound.play()
                    print(R+ "That spot is already taken: " + W)
                else:
                    table[1][n-4]="X"
                    break
            if n>=7 and n<=9:
                if table[2][n-7] == "X" or table[2][n-7] == "O":
                    picking_sound.stop()
                    error_sound.play()
                    print(R+ "That spot is already taken: " + W)
                else:
                    table[2][n-7] = "X"
                    break
            if n == 0:
                exit()
    if multiplayer == 1:
        with open("file.txt","w") as text_file:
            text_file.write(str(n))
    print("\n")
def picking_o():
    showtable()
    while True:
        try:
            n = int(input(B + "Player o turn: " + W))
            picking_sound.play()
        except ValueError:
            picking_sound.stop()
            error_sound.play()
            print(R + "Choose a number between 1 - 9!" + W)
            continue
        if n >9 or n < 0:
            picking_sound.stop()
            error_sound.play()
            print(R + "Choose number between 1 - 9!" + W)
        else:
            if n>0 and n<=3:
                if table[0][n-1] == "X" or table[0][n-1] == "O":
                    picking_sound.stop()
                    error_sound.play()
                    print(R+ "That spot is already taken: " + W)
                else:
                    table[0][n-1]="O"
                    break
            if n>=4 and n<=6:
                if table[1][n-4] == "X" or table[1][n-4] == "O":
                    picking_sound.stop()
                    error_sound.play()
                    print(R+ "That spot is already taken: " + W)
                else:
                    table[1][n-4]="O"
                    break
            if n>=7 and n<=9:
                if table[2][n-7] == "X" or table[2][n-7] == "O":
                    picking_sound.stop()
                    error_sound.play()
                    print(R+ "That spot is already taken: " + W)
                else:
                    table[2][n-7] = "O"
                    break
            if n == 0:
                exit()
    print("\n")

def picking_o_m():
    fileName = 'file.txt'
    originalTime = os.path.getmtime(fileName)
    potty = 0
    while True:
        if(os.path.getmtime(fileName) > originalTime):
            with open(fileName, 'r') as f:
                n = int(f.read())
                break
            originalTime = os.path.getmtime(fileName)
        b = " Waiting for the answer" + "." * potty
        print(b,end = "\r")
        time.sleep(4)
        if potty < 3:
            potty +=1
        else:
            potty = 0
    if n>0 and n<=3:
        table[0][n-1]="O"
    if n>=4 and n<=6:
        table[1][n-4]="O"
    if n>=7 and n<=9:
        table[2][n-7] = "O"
    print("                                              ")
    print("Enemy chose:" + str(n))
    print("\n")

def picking_ai(board):
    showtable()
    while True:
        row = random.randrange(0,3)
        collum = random.randrange(0,3)
        if board[row][collum] !="X" and board[row][collum] != "O":
            picking_sound.play()
            break
    for x in range (0,4):
        b = "Thinking" + "." * x
        print (b, end="\r")
        time.sleep(0.4)
    board[row][collum]= "O"
    print("                       ")
    print("\n")
    
xpoint=0
ypoint=0
bot_true = 0
local = 0
multiplayer = 0
while True:
    pygame.mixer.music.load("amoba_theme_2.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
    with open("file.txt", "w") as text_file:
        text_file.write (" ")
    with open("player.txt", "w") as text_file:
        text_file.write (" ")
    table= [[1,2,3], [4,5,6], [7,8,9]]
    game_status = check_win(table)
    player = 0
    onlineplay = 0
    bot_true=0
    answer = ""
    game_start = input ("Press " + G + "Y" + W + " to start, or press " + R +"0" + W + " anytime to exit :")
    if game_start == "0":
        exit()
    while bot_true == 0 and local == 0 and multiplayer == 0:
        answer = input("Do you want to play againts a bot or local or multiplayer" +
                    G + "B" + W + "/" + R + "L" + W + "/" + B + "M" + W)
        if answer == ("B"):
            bot_true = 1
        elif answer == ("L"):
            local = 1
        elif answer == ("M"):
            multiplayer = 1
        elif answer == str(0):
            exit()
        else:
            print("Wrong answer!")
    while game_status == 0:
        if multiplayer == 1:
            while player != 1 and player != 2:
                player = input("choose 1 or 2")
                if player == str(1):
                    with open("player.txt", "r") as f:
                        content = f.read()
                    if content == "z":
                        print("The other player have already chosen!")
                        print("Now the player number is selected for you!")
                        player = 2
                    with open("player.txt", "w") as text_file:
                        text_file.write ("z")
                elif player == str(2):
                    with open("player.txt", "r") as f:
                        content = f.read()
                    if content == "i":
                        print("The other player have already chosen!")
                        print("Now the player number is selected for you!")
                        player = 1
                    with open("player.txt", "w") as text_file:
                        text_file.write ("i")
                else:
                    print("Wrong answer!")
                player = int(player)
            if player == 1:
                picking_x(1)
                showtable()
                if check_win(table) == "X":#ez kell ide?
                    win_sound.play()
                    showtable()
                    game_status = 1
                    xpoint+=1
                    break
                if table_full(table) == True:
                    error_sound.play()
                    showtable()
                    break
                picking_o_m()
                if check_win(table) =="O":#ez kell ide?
                    win_sound.play()
                    showtable()
                    game_status = 1
                    ypoint+=1
                    break
                if table_full(table) == True:
                    error_sound.play()
                    showtable()
                    break
            if player == 2:
                picking_o_m()
                showtable()
                with open ("file.txt","r") as f:
                    choice = str(f.read())
                print("Enemy chose: " + choice)
                if check_win(table) == "O":#ez kell ide?
                    win_sound.play()
                    showtable()
                    game_status = 1
                    xpoint+=1
                    break
                if table_full(table) == True:
                    error_sound.play()
                    showtable()
                    break
                picking_x(1)
                if check_win(table) =="X":#ez kell ide?
                    win_sound.play()
                    showtable()
                    game_status = 1
                    ypoint+=1
                    break
                if table_full(table) == True:
                    error_sound.play()
                    showtable()
                    break
        if multiplayer == 0:
            picking_x()
            if check_win(table) == "X":
                win_sound.play()
                showtable()
                game_status = 1
                xpoint+=1
                break
            if table_full(table) == True:
                error_sound.play()
                showtable()
                break
            if bot_true==1:
                picking_ai(table)
                picking_sound.play()
            else:
                picking_o()
            if check_win(table) =="O":
                win_sound.play()
                showtable()
                game_status = 1
                ypoint+=1
                break
            if table_full(table) == True:
                error_sound.play()
                showtable()
                break
    showtable()
    pygame.mixer.music.fadeout(7000)
    pygame.mixer.music.stop()
    print(O+"X player points: " +W + str(xpoint))
    print(B+"O player points: " +W + str(ypoint))
    print("Next round: ")
    
