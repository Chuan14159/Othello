# Changchuan Shen 83371717. Lab assignment 5. Lab sec 14. Module Logic.

from math import *

NONE = 0
BLACK = 1
WHITE = -1

class Gamestate:

    
    def __init__(self, row, col, turn):
        '''returns a new gamestate with nothing placed on it.'''
        self._col = row
        self._row = col
        self._turn = turn
        
    def gamestart(self, color):
        '''generate the gamestate with the diagonal four original places with the color at the top-left.'''
        self.state = [[0 for i in range(self._col)] for i in range(self._row)]
        self.state[floor((self._row-1)/2)][floor((self._col-1)/2)] = color
        self.state[ceil((self._row-1)/2)][ceil((self._col-1)/2)] = color
        self.state[ceil((self._row-1)/2)][floor((self._col-1)/2)] = 0 - color
        self.state[floor((self._row-1)/2)][ceil((self._col-1)/2)] = 0 - color
        return self.state


    def _flip(self, color, row, column):
        '''returns the list of flip locations.'''
        self._fliplist = []
        for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            self._x = row
            self._y = column
            self._x += xdirection
            self._y += ydirection
            if self._isonboard(self._x, self._y):
                if self.state[self._x][self._y] == 0 - color:
                    while self.state[self._x][self._y] == 0 - color:  
                        self._x += xdirection  
                        self._y += ydirection  
                        if not self._isonboard(self._x, self._y):  
                            break
                    if not self._isonboard(self._x, self._y):
                        continue
                    if self.state[self._x][self._y] == color:
                        while True:
                            self._x -= xdirection
                            self._y -= ydirection
                            if self._x == row and self._y == column:
                                break
                            self._fliplist.append([self._x, self._y])
        return self._fliplist

                
    def _isonboard(self, row, column):
        '''return whether it is on the game board'''
        return row >= 0 and row <= self._row-1 and column >= 0 and column <= self._col-1

        
    def move(self, color, row, column, fliplist):
        ''' drop the color and renew the game state if it is valid.'''
        self.state[row][column] = color
        for location in fliplist:
            self.state[location[0]][location[1]] = color
        return self.state


    def printstate(self):
        '''get the scores and return them as a string.'''
        return "BLACK: {} WHITE: {}".format(self.count()[0], self.count()[1])

    def printturn(self):
        '''get the players turn'''
        return "TURN: {}".format({1:'BLACK', -1:'WHITE'}[self._turn])

    def isnotvalid(self, color, row, column):
        '''return True if the move is not valid.'''
        if not self._isonboard(row, column):
            return True
        return self.state[row][column] or self._flip(color, row, column) == []
    
    def hasvalidmove(self, color):
        '''return ture if the player has no valid move.'''
        for row in range(self._row):
            for column in range(self._col):
                if not self.isnotvalid(color, row, column):
                    return True
        return False

    def gameover(self):
        '''gameover while no player has valid move'''
        return not self.hasvalidmove(BLACK) and not self.hasvalidmove(WHITE)

    def count(self):
        self._black = 0
        self._white = 0
        for row in range(self._row):
            for column in range(self._col):
                if self.state[row][column] == BLACK:
                    self._black += 1
                if self.state[row][column] == WHITE:
                    self._white += 1
        return [self._black, self._white]

    def changeturn(self):
        '''change the turn of black and white'''
        self._turn *= -1
        return self._turn

