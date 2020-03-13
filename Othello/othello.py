'''
Olivia Spears
CWID: 102-40-548
Due: 11/12/2018
-------------------------------------
A program meant to implement a playable game of Othello between two humans and also
a game against and AI opponent using the mini max algorithm and alpha beta pruning.

To run, othello.py --play_num <1 or 2> --player1 <black or white> --debug <True or False> [optional] --logging <True or False> [optional]
----------------------------------------
'''
# import statements
import math
import argparse
import time
from tkinter import *
import copy
import sys

# UI dimensions
WIDTH = 600
HEIGHT = 600
MARGIN = 8
CELL = 73

# Enums for game
EMPTY = 0
VALID = 1
BLACK = 2
WHITE = 3

# Set in command line
AI = False
AIcolor = BLACK
debug = False
logging = False

# hardcoded to set depth and alpha beta pruning
desired_depth = 5
pruning = True

stateCounter = 0

# A function to log a game
def logState(state, row, col, game):
    global log
    # Just came from the AI's turn
    if state == "minimax":
        if row != -1:
            if col == 0:
                letter = "A"
            elif col == 1:
                letter = "B"
            elif col == 2:
                letter = "C"
            elif col == 3:
                letter = "D"
            elif col == 4:
                letter = "E"
            elif col == 5:
                letter = "F"
            elif col == 6:
                letter = "G"
            else:
                letter = "H"
            log += "\nAI just moved! Selected " + letter + str(row+1)
        else:
            log += "\nNo valid moves for the AI. Skipping turn"
    
    # just came from the Player's turn
    elif state == "playermove":
        if row != -1:
            if col == 0:
                letter = "A"
            elif col == 1:
                letter = "B"
            elif col == 2:
                letter = "C"
            elif col == 3:
                letter = "D"
            elif col == 4:
                letter = "E"
            elif col == 5:
                letter = "F"
            elif col == 6:
                letter = "G"
            else:
                letter = "H"
            log += "\nPlayer moved! Selected " + letter + str(row +1)
        else:
            log += "\nNo valid moves for player :( Skipped turn"
    
    # The first set up
    elif state == "initial":
        log = "Starting Game!"
        if AIcolor == BLACK:
            log += "\nAI = Black      Human = White"
        else:
            log += "\nAI = White      Human = Black"
    
    # Logs the score and draws the board
    if state != "start":
        log += "\n**********************\nScore:   Black - " + str(game.count[0]) + "   White - " + str(game.count[1]) 
        log += "\n | A | B | C | D | E | F | G | H |"
        for i in range(8):
            log += "\n" + str(i+1) + "|"
            for j in range(8):
                space = game.board[i][j]
                if space == EMPTY or space == VALID:
                    space = " "
                elif space == BLACK:
                    space = "x"
                elif space == WHITE:
                    space = "o"
                log += " " + space + " |"
                
        log +=  "\n**********************\n"
        
#argument parsing
def parse_arguments():
    global AI, AIcolor, debug, logging
    # sets up an argument parser
    arg_parser = argparse.ArgumentParser()
    # determines if you're playing against an AI or a person
    arg_parser.add_argument("--play_num",
                            help="Number of players",
                            type=int,
                            choices=[1, 2],
                            required=True)
    # sets the color of player 1 (who is the human in the case of a single player game. not really relevant for 2 player)
    arg_parser.add_argument("--player1",
                            help="The color of player 1. If 1 player, player 1 is the human",
                            type=str,
                            choices=["black", "white"],
                            required=True)
    # turns on debug mode
    arg_parser.add_argument("--debug",
                            type=bool,
                            required=False)
    # turns on logging
    arg_parser.add_argument("--logging",
                            type=bool,
                            required=False)
    # Creates a dictionary of keys = argument flag, and value = argument
    arg = vars(arg_parser.parse_args())
    if arg['play_num'] == 1:
        AI = True
        if arg['player1'] == 'black':
            AIcolor = WHITE
    if arg['debug'] == True:
        debug = True
        print("debug mode A C T I V A T E D")
    if arg['logging'] == True:
        logging = True
        print("logging game!!!")
    return arg['play_num']
#************************MiniMax********************************

def minimax(boardstate):
    global stateCounter
    # gets the list of possible moves
    move_list = boardstate.get_valid()
    if debug:
        print("\n********************\nin minimax\n********************\n")
    # no valid moves!!!!
    if len(move_list) == 0:
        row = -1
        col = -1
    else:
        # since the first layer is maximizing, the best value is initialized to -9999
        best_move = -9999
        # counter is set to 0
        stateCounter = 0
        
        # iterate through the list of moves
        for (x, y) in move_list:
            stateCounter += 1
            # copy the board so the original board doesn't change
            tempboard = copy.deepcopy(boardstate)
            # Making the move :)
            tempboard.determine_board([x, y])
            # and now its the opponents turn. Since its the opponent's turn, maximizing is set to false...
            # here the corners are emphasized so they'll end with a higher value
            if (x, y) == (0, 0) or (x, y) == (0, 7) or (x, y) == (7, 0)  or (x, y) == (7, 7) :
                value = minimax_value(tempboard, 1, False, -99999, 99999) + 30
            else:
                value = minimax_value(tempboard, 1, False, -99999, 99999)
            
            # Prints after a coordinate is finished being considered
            if debug:
                print("Move considered row " + str(x+1) + " and col " + str(y+1) + "\nMove has a heuristic of " + str(value)+"\n")
            
            # sets best value to highest value found and best coordinates to corresponding coordinates
            if (value > best_move):
                best_move = value
                bestRow = x
                bestCol = y 
                if debug:
                    print("***New best position!! Row " + str(bestRow+1) +" and Col " + str(bestCol+1) + "\n")
        if debug:    
            print("Best coordinates!! Row " + str(bestRow+1) +" and Col " + str(bestCol+1))
            print("Best value!! " + str(best_move))
            print("Nodes visited: " + str(stateCounter))
        row = bestRow
        col = bestCol
    
    return row, col
    
def minimax_value(board, depth, max, alpha, beta):
    global stateCounter
    
    # checks to see if the search is at the end
    if depth == desired_depth or board.GameOver:
        return heuristic(board)
    
    # otherwise!!! we're searching recursively!!
    else:
        tempboard = copy.deepcopy(board)
        move_list = board.get_valid()
        if len(move_list) == 0: # If no turns, pass the turn
            tempboard.determine_board([-1, -1])
            if max: # get value of next node with the right conditions of maximizing or minimizing
                return minimax_value(tempboard, 1, False, alpha, beta)
            else:
                return minimax_value(tempboard, 1, True, alpha, beta)
            
        elif max: # IF A MAXIMIZING LAYER
            best_value = -99999
            for (x, y) in move_list: 
                stateCounter += 1
                # go through the move list and make the move!
                tempboard.determine_board([x, y])
                # Emphasize corners again
                if (x, y) == (0, 0) or (x, y) == (0, 7) or (x, y) == (7, 0)  or (x, y) == (7, 7) :
                    value = minimax_value(tempboard, depth + 1, False, alpha, beta) + 30
                else:
                    value = minimax_value(tempboard, depth + 1, False, alpha, beta)
                
                # Handle setting the best value to the highest bc maximizing
                if value > best_value:
                    best_value = value
                    
                # and handle setting the alpha values
                if alpha < best_value:
                    alpha = best_value 
                
                # Check the beta and the alpha to see if we need to continue searching on this node
                if pruning:
                    if beta <= alpha:
                        break
                
            return best_value
            
        elif not max: # IF A MINIMIZING LAYER
            # everything is the same as above except handled for minimizing instead of maximizing
            best_value = 99999
            for (x, y) in move_list:
                #if debug:
                stateCounter += 1
                tempboard.determine_board([x, y])
                if (x, y) == (0, 0) or (x, y) == (0, 7) or (x, y) == (7, 0)  or (x, y) == (7, 7) :
                    value = minimax_value(tempboard, depth + 1, True, alpha, beta) - 30
                else:
                    value = minimax_value(tempboard, depth + 1, True, alpha, beta)
                if value < best_value:
                    best_value = value
                if beta > best_value:
                    beta = best_value 
                if pruning:
                    if beta <= alpha:
                        break
                
            return best_value

# the heuristic value for the nodes. Based on the number of available moves for the current player and a little bit based on the score 
def heuristic(board):
    move_list = board.get_valid()
    scores = board.count_pieces()
    if AIcolor == BLACK:
        player = scores[0]
        opp = scores[1]
    else:
        player = scores[1]
        opp = scores[0]
    score = (player - opp) / 5
    
    return ((len(move_list) * 2) + score)
        
#Othello board state handler
class board_state(object):
    def __init__(self, players):
        self.players = players
        self.turn = BLACK
        self.board = self.create_board()
        self.noMoves1 = False
        self.noMoves2 = False
        self.GameOver = False
        self.num_flipped = 0

    # The initial board
    def create_board(self):
        # Creates 2D array and everything is set to 0
        newboard = [[EMPTY for x in range(8)] for y in range(8)]

        # Sets initial locations of WHITE and BLACK
        newboard[3][3] = WHITE
        newboard[4][4] = WHITE
        newboard[3][4] = BLACK
        newboard[4][3] = BLACK

        # Adds in the initial valid moves of the game board
        newboard = self.check_valid(newboard, BLACK)

        return newboard

    # the board at the end of each turn
    def determine_board(self, location):
        # updates the turn
        if self.turn == WHITE:
            piece = WHITE
            self.turn = BLACK
        elif self.turn == BLACK:
            piece = BLACK
            self.turn = WHITE
        i = location[0]
        j = location[1]

        # Update the pieces in the board
        newboard = self.board
        # Allows for handling of passing a turn
        if i != -1:
            newboard[i][j] = piece
            newboard = self.flip(newboard, i, j, piece)
        
        # Updates the valid moves on the board
        newboard = self.check_valid(newboard, self.turn)

        # Checks for a game over
        if self.noMoves1 and self.noMoves2:
            self.GameOver = True

        return newboard
    
    # Flips pieces after a move
    def flip(self, boardstate, i, j, piece):
        #check around for a piece of the opposite color. start N
        placed = boardstate[i][j]
        opp_piece = self.turn
        toFlip = []
        self.num_flipped = 0

        #check N (methods here are duplicated below
        if(j != 0):
            check = j
            possibleFlip = [] # An array to hold pieces that might be flipped!
            while (check > 0):
                check -= 1
                # If the board space is empty then the pieces can't be flipped. break.
                if (boardstate[i][check] == EMPTY or boardstate[i][check] == VALID):
                    break
                # If the piece is of the player's color then all the pieces in the possibleFlip array can be flipped. break
                elif (boardstate[i][check] == placed):
                    if len(possibleFlip) != 0:
                        for pair in possibleFlip:
                            toFlip.append(pair)
                    break
                # If its an opponent's piece, its added to the possibleFlip array 
                elif (boardstate[i][check] == opp_piece):
                    possibleFlip.append((i, check))

        #check S
        if(j != 7):
            check = j
            possibleFlip = []
            while (check < 7):
                check += 1
                if (boardstate[i][check] == EMPTY or boardstate[i][check] == VALID):
                    break
                elif (boardstate[i][check] == placed):
                    if len(possibleFlip) != 0:
                        for pair in possibleFlip:
                            toFlip.append(pair)
                    break
                elif (boardstate[i][check] == opp_piece):
                    possibleFlip.append((i, check))

        #check W
        if(i != 0):
            check = i
            possibleFlip = []
            while (check > 0):
                check -= 1
                if (boardstate[check][j] == EMPTY or boardstate[check][j] == VALID):
                    break
                elif (boardstate[check][j] == placed):
                    if len(possibleFlip) != 0:
                        for pair in possibleFlip:
                            toFlip.append(pair)
                    break
                elif (boardstate[check][j] == opp_piece):
                    possibleFlip.append((check, j))

        #check E
        if(i != 7):
            check = i
            possibleFlip = []
            while (check < 7):
                check += 1
                if (boardstate[check][j] == EMPTY or boardstate[check][j] == VALID):
                    break
                elif (boardstate[check][j] == placed):
                    if len(possibleFlip) != 0:
                        for pair in possibleFlip:
                            toFlip.append(pair)
                    break
                elif (boardstate[check][j] == opp_piece):
                    possibleFlip.append((check, j))

        #check NW
        if (i != 0 and j != 0):
            check_i, check_j = i, j
            possibleFlip = []
            while (check_i > 0 and check_j > 0):
                check_i -= 1
                check_j -= 1
                if (boardstate[check_i][check_j] == EMPTY or boardstate[check_i][check_j] == VALID):
                    break
                elif (boardstate[check_i][check_j] == placed):
                    if len(possibleFlip) != 0:
                        for pair in possibleFlip:
                            toFlip.append(pair)
                    break
                elif (boardstate[check_i][check_j] == opp_piece):
                    possibleFlip.append((check_i, check_j))
                    
        #check NE
        if (i != 7 and j != 0):
            check_i, check_j = i, j
            possibleFlip = []
            while (check_i < 7 and check_j > 0):
                check_i += 1
                check_j -= 1
                if (boardstate[check_i][check_j] == EMPTY or boardstate[check_i][check_j] == VALID):
                    break
                elif (boardstate[check_i][check_j] == placed):
                    if len(possibleFlip) != 0:
                        for pair in possibleFlip:
                            toFlip.append(pair)
                    break
                elif (boardstate[check_i][check_j] == opp_piece):
                    possibleFlip.append((check_i, check_j))
                    
        #check SW
        if (i != 0 and j != 7):
            check_i, check_j = i, j
            possibleFlip = []
            while (check_i > 0 and check_j < 7):
                check_i -= 1
                check_j += 1
                if (boardstate[check_i][check_j] == EMPTY or boardstate[check_i][check_j] == VALID):
                    break
                elif (boardstate[check_i][check_j] == placed):
                    if len(possibleFlip) != 0:
                        for pair in possibleFlip:
                            toFlip.append(pair)
                    break
                elif (boardstate[check_i][check_j] == opp_piece):
                    possibleFlip.append((check_i, check_j))
                    
        #check SE
        if (i != 7 and j != 7):
            check_i, check_j = i, j
            possibleFlip = []
            while (check_i < 7 and check_j < 7):
                check_i += 1
                check_j += 1
                if (boardstate[check_i][check_j] == EMPTY or boardstate[check_i][check_j] == VALID):
                    break
                elif (boardstate[check_i][check_j] == placed):
                    if len(possibleFlip) != 0:
                        for pair in possibleFlip:
                            toFlip.append(pair)
                    break
                elif (boardstate[check_i][check_j] == opp_piece):
                    possibleFlip.append((check_i, check_j))

        # Everything in the toFlip array is flipped
        for (x, y) in toFlip:
            boardstate[x][y] = placed
            self.num_flipped += 1
            
        return boardstate

    # Returns the number of valid moves on the board
    def get_valid(self):
        newboard = self.check_valid(self.board, self.turn)
        valid = []
        for i in range(8):
            for j in range(8):
                if newboard[i][j] == VALID:
                    coords = (i,j)
                    valid.append(coords)
        return valid
    
    # Finds the valid moves on the board for the given turn
    def check_valid(self, boardstate, piece):
        newValid = 0
        #Clear out previously valid marks
        for n in range(8):
            for m in range(8):
                if boardstate[n][m] == VALID:
                    boardstate[n][m] = EMPTY
        #Checking for valid moves based off of the opposing player's color
        for i in range(8):
            for j in range(8):
                #no piece on this spot
                if boardstate[i][j] == EMPTY or boardstate[i][j] == VALID:
                    continue
                #own piece
                elif boardstate[i][j] == piece:
                    continue
                #set opponent's piece color.
                if piece == BLACK:
                    opp_piece = WHITE
                elif piece == WHITE:
                    opp_piece = BLACK

                #check N. if j == 0 the space is all the on the top.
                #if j == 7 its all the way on the borrom and putting a piece on the N side won't be a valid move against this piece
                if (j != 0 and j != 7):
                    check_j = j
                    #see if there's a piece of player's color to S. if so, proceed
                    if boardstate[i][j+1] == piece:
                        while (check_j > 0):
                            check_j -= 1
                            #piece already has our own color on W side
                            if (boardstate[i][check_j] == piece):
                                break
                            elif (boardstate[i][check_j] == EMPTY or boardstate[i][check_j] == VALID):
                                boardstate[i][check_j] = VALID
                                newValid += 1
                                break
                            elif (boardstate[i][check_j] == opp_piece):
                                continue

                #check S if j == 0 the space is all the way to the left and putting a piece on the E side won't be a valid move against this piece
                #if j == 7 its all the way to the right
                if (j != 0 and j != 7):
                    check_j = j
                    #see if there's a piece of player's color to N. if so, proceed
                    if boardstate[i][j-1] == piece:
                        while (check_j < 7):
                            check_j += 1
                            #piece already has our own color on S side
                            if (boardstate[i][check_j] == piece):
                                break
                            elif (boardstate[i][check_j] == EMPTY or boardstate[i][check_j] == VALID):
                                boardstate[i][check_j] = VALID
                                newValid += 1
                                break
                            elif (boardstate[i][check_j] == opp_piece):
                                continue


                #check W
                if (i != 0 and i != 7):
                    check_i = i
                    #see if there's a piece of player's color to E. if so, proceed
                    if boardstate[i+1][j] == piece:
                        while (check_i > 0):
                            check_i -= 1
                            #piece already has our own color on W side
                            if (boardstate[check_i][j] == piece):
                                break
                            elif (boardstate[check_i][j] == EMPTY or boardstate[check_i][j] == VALID):
                                boardstate[check_i][j] = VALID
                                newValid += 1
                                break
                            elif (boardstate[check_i][j] == opp_piece):
                                continue

                #check E
                if (i != 0 and i != 7):
                    check_i = i
                    #see if there's a piece of player's color to W. if so, proceed
                    if boardstate[i-1][j] == piece:
                        while (check_i < 7):
                            check_i += 1
                            #piece already has our own color on S side
                            if (boardstate[check_i][j] == piece):
                                break
                            elif (boardstate[check_i][j] == EMPTY or boardstate[check_i][j] == VALID):
                                boardstate[check_i][j] = VALID
                                newValid += 1
                                break
                            elif (boardstate[check_i][j] == opp_piece):
                                continue

                #check NW
                if (i != 0 and i != 7 and j != 0 and j != 7):
                    check_i, check_j = i, j
                    if boardstate[i+1][j+1] == piece:
                        while (check_i > 0 and check_j > 0):
                            check_i -= 1
                            check_j -= 1
                            if (boardstate[check_i][check_j] == piece):
                                break
                            elif (boardstate[check_i][check_j] == EMPTY or boardstate[check_i][check_j] == VALID):
                                boardstate[check_i][check_j] = VALID
                                newValid += 1
                                break
                            elif (boardstate[check_i][check_j] == opp_piece):
                                continue

                #check SW
                if (i != 0 and i != 7 and j != 0 and j != 7):
                    check_i, check_j = i, j
                    if boardstate[i+1][j-1] == piece:
                        while (check_i > 0 and check_j < 7):
                            check_i -= 1
                            check_j += 1
                            if (boardstate[check_i][check_j] == piece):
                                break
                            elif (boardstate[check_i][check_j] == EMPTY or boardstate[check_i][check_j] == VALID):
                                boardstate[check_i][check_j] = VALID
                                newValid += 1
                                break
                            elif (boardstate[check_i][check_j] == opp_piece):
                                continue

                #check NE
                if (i != 0 and i != 7 and j != 0 and j != 7):
                    check_i, check_j = i, j
                    if boardstate[i-1][j+1] == piece:
                        while (check_i < 7 and check_j > 0):
                            check_i += 1
                            check_j -= 1
                            if (boardstate[check_i][check_j] == piece):
                                break
                            elif (boardstate[check_i][check_j] == EMPTY or boardstate[check_i][check_j] == VALID):
                                boardstate[check_i][check_j] = VALID
                                newValid += 1
                                break
                            elif (boardstate[check_i][check_j] == opp_piece):
                                continue

                #check SE
                if (i != 0 and i != 7 and j != 0 and j != 7):
                    check_i, check_j = i, j
                    if boardstate[i-1][j-1] == piece:
                        while (check_i < 7 and check_j < 7):
                            check_i += 1
                            check_j += 1
                            if (boardstate[check_i][check_j] == piece):
                                break
                            elif (boardstate[check_i][check_j] == EMPTY or boardstate[check_i][check_j] == VALID):
                                boardstate[check_i][check_j] = VALID
                                newValid += 1
                                break
                            elif (boardstate[check_i][check_j] == opp_piece):
                                continue

        # Updates noMoves for the corresponding player
        if piece == BLACK:
            if newValid == 0:
                self.noMoves1 = True
            else:
                self.noMoves1 = False
        elif piece == WHITE:
            if newValid == 0:
                self.noMoves2 = True
            else:
                self.noMoves2 = False
        return boardstate

    # Counts and returns how many of each color are on the board 
    def count_pieces(self):
        black, white = 0, 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == BLACK:
                    black += 1
                elif self.board[i][j] == WHITE:
                    white += 1
        
        return [black, white]

# Game controller
class OthelloGame:
    def __init__(self, boardstate):
        self.boardstate = boardstate
        self.board = boardstate.board
        #first item in count is black, second item in count is white
        self.count = boardstate.count_pieces()
        if AI:
            #if the first turn (black) is also the AI's color, start the AI for the first move
            if boardstate.turn == AIcolor:
                self.AI_move()
        if logging:
            logState("initial", 0, 0, self)

    # Handles allowing the AI to move
    def AI_move(self):
        valid_moves = self.boardstate.get_valid()
        if (len(valid_moves) == 0): # No moves. Skips turn.
            self.move(-1, -1)
        else: # Otherwise, calls minimax
            row, col = minimax(self.boardstate)
            self.move(row, col)
        
    # Called when a valid position is chosen on the board. Handles updating the board and the score
    def move(self, row, col):       
        location = [row, col]
        self.board = self.boardstate.determine_board(location)
        self.count = self.boardstate.count_pieces()
        
        if logging and self.boardstate.turn == AIcolor:
            logState("playermove", row, col, self)
        elif logging and self.boardstate.turn != AIcolor:
            logState("minimax", row, col, self)

    # Checks if a given position is Valid or not
    def isValid(self, row, col):
        if self.board[row][col] == VALID:
            return True
        else:
            return False

#*************************All that jazz********************************
class OthelloUI(Frame):
    def __init__(self, parent, game):
        self.game = game
        self.parent = parent
        Frame.__init__(self, parent)
        self.white_text = StringVar()
        self.black_text = StringVar()
        self.turn_text = StringVar()

        self.__initUI()

    # the initial UI setup
    def __initUI(self):
        self.parent.title("Othello")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT, bg="forest green")
        self.canvas.pack(fill=BOTH, side=TOP)

        self.__draw_HUD()
        self.__draw_grid()
        self.__draw_state()

        self.canvas.bind("<Button-1>", self.__box_clicked)

    # the handler for the score and turn displays
    def __draw_HUD(self):
        if self.game.boardstate.turn == BLACK:
            player_turn = "Black"
        else:
            player_turn = "White"
        label = Label(self.parent, text="OTHELLO", font=(24))
        label.pack()
        
        self.white_text.set("White: " + str(game.count[1]))
        white = Label(self.parent, textvariable=self.white_text, font=(24)).pack(side=RIGHT) 
        
        self.black_text.set("Black: " + str(game.count[0]))
        black = Label(self.parent, textvariable=self.black_text, font=(24)).pack(side=LEFT)
        
        self.turn_text.set("Black's turn!")
        player_turn = Label(self.parent, textvariable=self.turn_text, font=(26)).pack()

    # an updater for the HUD text
    def __update_HUD(self):
        if self.game.boardstate.turn == BLACK:
            player_turn = "Black"
        else:
            player_turn = "White"
        self.white_text.set("White: " + str(game.count[1]))
        self.black_text.set("Black: " + str(game.count[0]))
        self.turn_text.set(player_turn + "'s turn!")
        
    # draws the grid to be used by the game
    def __draw_grid(self):
        for i in range(9):
            x0 = MARGIN + i * CELL
            y0 = MARGIN
            x1 = MARGIN + i * CELL
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill="black")

            x0 = MARGIN
            y0 = MARGIN + i * CELL
            x1 = WIDTH - MARGIN
            y1= MARGIN + i * CELL
            self.canvas.create_line(x0, y0, x1, y1, fill="black")

    # draws the pieces and valid moves based on the state of the game
    def __draw_state(self):
        self.canvas.delete("VALID")
        board = game.board
        for i in range(8):
            for j in range(8):
                space = board[i][j]
                if space != EMPTY:
                    x = MARGIN + j * CELL + CELL / 2
                    y = MARGIN + i * CELL + CELL / 2
                    if space == WHITE:
                        color = "White"
                        outline = "White"
                        r = 25
                        tag = "WHITE"
                    elif space == BLACK:
                        color = "Black"
                        outline = "Black"
                        r = 25
                        tag = "BLACK"
                    elif space == VALID:
                        if (game.boardstate.turn == WHITE):
                            outline = "White"
                        else:
                            outline = "Black"
                        color = "Yellow"
                        tag = "VALID"
                        r = 15
                    self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline=outline, width=3.0, tags=tag)                    

    # draws the no move indicator when one player is out of moves
    def __draw_nomoves(self):
        x0 = y0 = MARGIN + CELL * 2
        x1 = y1 = MARGIN + CELL * 6
        self.canvas.create_oval(x0, y0, x1, y1, fill="cyan", outline="cyan", tags="nomoves")
        x = y = MARGIN + 3.5 * CELL + CELL / 2
        self.canvas.create_text(x, y, text="No more moves for this player", font=(30), tags="nomoves")
        self.canvas.create_text(x, y+20, text="[Click anywhere to continue]", tags="nomoves")

    # draws the game over circle when the game has ended
    def __draw_gameover(self):
        global log
        if game.count[0] > game.count[1]:
            winner = "BLACK is the winner!"
        elif game.count[1] > game.count[0]:
            winner = "WHITE is the winner!"
        elif game.count[0] == game.count[1]:
            winner = "It's a tie!"
            
        if logging:
            log += "\n" + winner
            
        x0 = y0 = MARGIN + CELL * 2
        x1 = y1 = MARGIN + CELL * 6
        self.canvas.create_oval(x0, y0, x1, y1, fill="gold", outline="gold", tags="gameover")
        x = y = MARGIN + 3.5 * CELL + CELL / 2
        self.canvas.create_text(x, y, text=winner, font=(30), tags="gameover")
        self.canvas.create_text(x, y+20, text="Thanks for playing :)", tags="gameover")
    
    # handles when the screen is clicked
    def __box_clicked(self, event):
        x, y = event.x, event.y
        if(MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            # get row and column from x, y coords
            row, col = math.floor((y - MARGIN) / CELL), math.floor((x - MARGIN) / CELL)
            
            # If that spot is a pre-determined valid spot
            if (game.isValid(row,col)):
                game.move(row, col)
                self.__draw_state()
                self.__update_HUD()
            
            self.manage_views()

    # manages how views are displayed after the screen is clicked
    def manage_views(self):
        Tk.update(self)
        
        # allows the AI to move
        if AI and self.game.boardstate.turn == AIcolor:
            if len(self.canvas.find_withtag("nomoves")) == 3:
                self.canvas.delete("nomoves")
                game.move(-1, -1)
                self.__update_HUD()
                self.__draw_state()
            self.game.AI_move()
            self.__draw_state()
            self.__update_HUD()
        
        #checks if the window is currently displaying game over
        if len(self.canvas.find_withtag("gameover")) == 3:
            # clears the circle, saves the log if logging, and exits the game
            self.canvas.delete("gameover")
            if logging:
                f = open("log.txt", "w")
                f.write(log)
            sys.exit()     
            
        # calls the draw game over if the game is over
        if game.boardstate.GameOver:
            self.__draw_gameover()
            Tk.update(self)
            
        # deletes and skips turn if no more moves
        elif len(self.canvas.find_withtag("nomoves")) == 3:
            self.canvas.delete("nomoves")
            game.move(-1, -1)
            self.__draw_state()
            self.__update_HUD()
            self.manage_views()
            
        # calls the no move draw
        elif (self.game.boardstate.turn == BLACK and game.boardstate.noMoves1) or (self.game.boardstate.turn == WHITE and game.boardstate.noMoves2):
            self.__draw_nomoves()

#********************************Running*************************************
player_info = parse_arguments()
    
board = board_state(player_info)
game = OthelloGame(board)

window = Tk()
OthelloUI(window, game)

window.mainloop()
