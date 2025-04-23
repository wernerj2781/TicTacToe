__author__ = 'Jeff Werner'

'''
A working example of a Tic Tac Toe game. Not the most elegant implementation, but it works. 
And so far the "AI" works too (which is really just randomly selecting
'''

from tkinter import * #Tk, Canvas, Frame, BOTH
import random
import json
import AI_Level_One
import time
import GameData


global aiToken

global gameData, space_info
WinnerExists = False
#gameData will be sent to AI so it can determine what to do (when I get that part in the works)
gameData = {"WinnerExists": False, "AIWin": False, "AIFirst": False, "AIChoices": [], "OpponentChoices": [] }
space_info = ["-","-","-","-","-","-","-","-","-"]
global winning_combos
winning_combos = [
    [ 0, 1, 2 ], [ 3, 4, 5 ],
    [ 6, 7, 8 ], [ 0, 3, 6 ],
    [ 1, 4, 7 ], [ 2, 5, 8 ],
    [ 0, 4, 8 ], [ 2, 4, 6 ]
]

global turn, order
turn = 'X'
order = "Human"

global ai
ai = AI_Level_One.AI_Level_One("Clarence")
GameDataSet = GameData.AnalysisData(gameData, False, False, False, [], [])



class GameSpace(Frame):

    def __init__(self, master, id, xPos, yPos):
        super(GameSpace, self).__init__(master)
        self.id = id
        self.grid()
        self.create_widget(xPos, yPos)

    def create_widget(self,xPos, yPos):
        self.bttn = Button(self)
        self.bttn['text'] = " "
        self.bttn['command'] = self.select_spot
        self.bttn['height'] = 5
        self.bttn['width'] = 10
        self.bttn.place(x=100, y=100)
        self.bttn.grid()

    def select_spot(self):
        global turn
        #global space_info
        if self.bttn['text'] != 'X' and self.bttn['text'] != 'O':
            self.bttn['text'] = turn
            space_info[self.id-1] = turn
            gameEnd = check_for_winnning(turn)
            if gameEnd:
                print("1. Game over. Player " + turn + " wins.")
                sendGameData()
                #insert section of sending metrics
            turn = toggle_turn(turn)
            ai_on = True #just a temporary variable
            #check for winning here
            if gameEnd == False:
                aiTurn()

    def get_slot_input(self):
        return self.bttn['text']

    def get_slot_id(self):
        return self.Id

def clearBoard():
    global space_info
    space_info = ["-","-","-","-","-","-","-","-","-"]
    createBoard()
    print("clear")

#which do I go with? this one, or determineInput?
def toggle_turn(turn):
    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'
    return turn

def determineInput():
    global counter
    if counter % 2 == 0:
        counter = counter + 1
        return "O"
    else:
        counter = counter + 1
        return "X"

def determineFirstTurn():
    global turn
    if setFirst.get() == 1:
        turn = 'X'
    if setFirst.get() == 2:
        turn = 'O'

def determineTurnOrder():
    global order
    if turnOrder.get() == 1:
        order = "Human"
    if turnOrder.get() == 2:
        order = "AI"

#still testing things out with this function
def sendGameData():
    global gameData
    info = GameDataSet.WinnerExists
    infotest = GameDataSet.GameData["WinnerExists"]
    #create json object

def createBoard():
    global TopLeft, TopCenter, TopRight, MiddleLeft, MiddleCenter, MiddleRight, BotLeft, BotCenter, BotRight
    TopLeft = GameSpace(root,1,10,10)
    TopLeft.place(x=10,y=10)
    TopCenter = GameSpace(root,2,100,10)
    TopCenter.place(x=100, y=10)
    TopRight = GameSpace(root,3,190,10)
    TopRight.place(x=190, y=10)
    MiddleLeft = GameSpace(root,4,10,100)
    MiddleLeft.place(x=10, y=100)
    MiddleCenter = GameSpace(root,5,100,100)
    MiddleCenter.place(x=100, y=100)
    MiddleRight = GameSpace(root,6,190,100)
    MiddleRight.place(x=190, y=100)
    BotLeft = GameSpace(root,7,10,190)
    BotLeft.place(x=10, y=190)
    BotCenter = GameSpace(root,8,100,190)
    BotCenter.place(x=100, y=190)
    BotRight = GameSpace(root,9,190,190)
    BotRight.place(x=190, y=190)

def check_for_winnning(player_turn):
    global gameData
    gameEnd = False;
    for win in winning_combos:
        gameEnd = check_match_three(win, player_turn, space_info)
        if gameEnd == True:
            gameData["WinnerExists"] = True
            return gameEnd
    return gameEnd


def check_match_three(input, player_turn, space_info):
    if str(space_info[(input[0])]) == str(player_turn) and str(space_info[(input[0])]) == str(space_info[(input[1])]) and str(space_info[(input[0])]) == str(space_info[(input[2])]):
        print("Player " + str(player_turn) + " wins!")
        return True
    return False

def startGame():
    print("starting game")
    if order == "AI":
        aiTurn()
    elif order == "Human":
        print("Humans first")

def aiTurn():
    spot = ai.select_space(space_info)
    select_space(spot,spot)


def select_space(space_number, location):
    global turn
    gameEnd = check_for_winnning(turn)
    if gameEnd:
        print("2. Game over. Player " + turn + " wins.")
        sendGameData()
        #send metrics here
    if gameEnd == False:
        if space_number == 0:
            if TopLeft.bttn['text'] == " ":
                token = turn # just testing to see if I can just make it turn instead of this
                TopLeft.bttn['text'] = token
                space_info[space_number] = token
                turn = toggle_turn(turn)
            else:
                print("Something went wrong.")

        elif space_number == 1:
            if TopCenter.bttn['text'] == " ":
                token = turn # just testing to see if I can just make it turn instead of this
                TopCenter.bttn['text'] = token
                space_info[space_number] = token
                turn = toggle_turn(turn)
            else:
                print("Something went wrong.")
                #recalibrate(location)
                #aiTest()#do it again
        elif space_number == 2:
            if TopRight.bttn['text'] == " ":
                token = turn # just testing to see if I can just make it turn instead of this
                TopRight.bttn['text'] = token
                space_info[space_number] = token
                turn = toggle_turn(turn)
            else:
                print("Something went wrong")
        elif space_number == 3:
            if MiddleLeft.bttn['text'] == " ":
                token = turn # just testing to see if I can just make it turn instead of this
                MiddleLeft.bttn['text'] = token
                space_info[space_number] = token
                turn = toggle_turn(turn)
            else:
                print("Something went wrong")
        elif space_number == 4:
            if MiddleCenter.bttn['text'] == " ":
                token = turn # just testing to see if I can just make it turn instead of this
                MiddleCenter.bttn['text'] = token
                space_info[space_number] = token
                turn = toggle_turn(turn)
            else:
                print("Something went wrong")
        elif space_number == 5:
            if MiddleRight.bttn['text'] == " ":
                token = turn # just testing to see if I can just make it turn instead of this
                MiddleRight.bttn['text'] = token
                space_info[space_number] = token
                turn = toggle_turn(turn)
            else:
                print("Something went wrong")
        elif space_number == 6:
            if BotLeft.bttn['text'] == " ":
                token = turn # just testing to see if I can just make it turn instead of this
                BotLeft.bttn['text'] = token
                space_info[space_number] = token
                turn = toggle_turn(turn)
            else:
                print("Something went wrong")
        elif space_number == 7:
            if BotCenter.bttn['text'] == " ":
                token = turn # just testing to see if I can just make it turn instead of this
                BotCenter.bttn['text'] = token
                space_info[space_number] = token
                turn = toggle_turn(turn)
            else:
                print("Something went wrong")
        elif space_number == 8:
            if BotRight.bttn['text'] == " ":
                token = turn # just testing to see if I can just make it turn instead of this
                BotRight.bttn['text'] = token
                space_info[space_number] = token
                turn = toggle_turn(turn)
            else:
                print("Something went wrong")

root = Tk()
root.title("Tic Tac Toe")
root.geometry("400x400")




createBoard()

setFirst = IntVar()
turnOrder = IntVar()

radioX = Radiobutton(root, text="X first", variable=setFirst, value=1, command=determineFirstTurn)
radioX.place(x=100, y=330)
radioO = Radiobutton(root, text="O first", variable=setFirst, value=2, command=determineFirstTurn)
radioO.place(x=200, y=330)
radioX.select()

radioHumanFirst = Radiobutton(root, text="Human first", variable=turnOrder, value=1, command=determineTurnOrder)
radioHumanFirst.place(x=100, y=360)
radioAiFirst = Radiobutton(root, text="Ai first", variable=turnOrder, value=2, command=determineTurnOrder)
radioAiFirst.place(x=200, y=360)
radioHumanFirst.select()


gameStart = Button(root, compound=BOTTOM, text="Start game", command=startGame)
gameStart.place(x=300, y=300)
clear = Button(root, compound=BOTTOM, text="Clear", command=clearBoard)
clear.place(x=100,y=300)



root.mainloop()


#order of events

#0: Who's input is it anyways? Determine if human or "AI" is first
#1a: If human first, await for input (just have button press be the trigger
#2b: If AI first, do the AI portion and have it change the button location's text (no actual button press required)
#3 determine if there is a winner, if there is, the game ends and a reset is required for more play
