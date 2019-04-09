#python3

from piece import Bishop
from piece import King
from piece import Rook
from piece import Pawn
from piece import Queen
from piece import Knight
import time
import pygame

class board:
    rect = (113, 113, 525, 525)
    startX = rect[0]
    startY = rect[1]
    
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        
        self.turn = "w"
        self.winner = None
        self.last = None
        
        #player time
        self.time1 = 900
        self.time2 = 900
        
        """Places all the pieces on 2D Array Board & generate the board"""
        self.board = [[0 for x in range(8)] for _ in range(rows)]
        
        self.board[0][0] = Rook(0, 0, "b")
        self.board[0][1] = Knight(0, 1, "b")
        self.board[0][2] = Bishop(0, 2, "b")
        self.board[0][3] = Queen(0, 3, "b")
        self.board[0][4] = King(0, 4, "b")
        self.board[0][5] = Bishop(0, 5, "b")
        self.board[0][6] = Knight(0, 6, "b")
        self.board[0][7] = Rook(0, 7, "b")
            
        self.board[7][0] = Rook(7, 0, "w")
        self.board[7][1] = Knight(7, 1, "w")
        self.board[7][2] = Bishop(7, 2, "w")
        self.board[7][3] = Queen(7, 3, "w")
        self.board[7][4] = King(7, 4, "w")
        self.board[7][5] = Bishop(7, 5, "w")
        self.board[7][6] = Knight(7, 6, "w")
        self.board[7][7] = Rook(7, 7, "w")
            
        #faster way of setting pawns
        for colum in range(0,8):
            self.board[1][colum] = Pawn(1,colum,"b")
            self.board[6][colum] = Pawn(6,colum,"w")  
     
        #keep track of pieces move
        self.moveStack = []
        
        self.turn = "w"

        self.time1 = 900
        self.time2 = 900

        self.storedTime1 = 0
        self.storedTime2 = 0

        self.winner = None

        self.startTime = time.time()

        
    def set_piece(self, row, col, new_piece):
        """ This function sets piece on (row, col) cell on board. 
        :param: row, the row coordinate of the piece. 
        :param: col, the col coordinate of the piece. 
        :return: None """
        self.board[row][col] = new_piece
        

    def draw(self, win, color):
        """Draws all the images on the board"""
        
        if self.last and color == self.turn:
            y, x = self.last[0]
            y1, x1 = self.last[1]

            xx = (4 - x) +round(self.startX + (x * self.rect[2] / 8))
            yy = 3 + round(self.startY + (y * self.rect[3] / 8))
            xx1 = (4 - x) + round(self.startX + (x1 * self.rect[2] / 8))
            yy1 = 3+ round(self.startY + (y1 * self.rect[3] / 8))

        s = None
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0: 
                    self.board[i][j].draw(win, color) #drawing each piece by calling piece.draw
                    if self.board[i][j].isSelected:
                        s = (i, j)
                        
    def select(self, col, row, color):
        changed = False
        prev = (-1, -1)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].selected:
                        prev = (i, j)

        # if piece
        if self.board[row][col] == 0:
            moves = self.board[prev[0]][prev[1]].move_list
            if (col, row) in moves:
                changed = self.move(prev, (row, col), color)

        else:
            if self.board[prev[0]][prev[1]].color != self.board[row][col].color:
                moves = self.board[prev[0]][prev[1]].move_list
                if (col, row) in moves:
                    changed = self.move(prev, (row, col), color)

                if self.board[row][col].color == color: #theres a bug here:AttributeError: 'int' object has no attribute 'color'
                    self.board[row][col].selected = True

            else:
                self.reset_selected()
                if self.board[row][col].color == color:
                    self.board[row][col].selected = True

        if changed:
            if self.turn == "w":
                self.turn = "b"
                self.reset_selected()
            else:
                self.turn = "w"
                self.reset_selected()

    def move(self, start, end, color):
        checkedBefore = self.is_checked(color)
        changed = True
        nBoard = self.board[:]
        if nBoard[start[0]][start[1]].pawn:
            nBoard[start[0]][start[1]].first = False

        nBoard[start[0]][start[1]].change_pos((end[0], end[1]))
        nBoard[end[0]][end[1]] = nBoard[start[0]][start[1]]
        nBoard[start[0]][start[1]] = 0
        self.board = nBoard

        if self.is_checked(color) or (checkedBefore and self.is_checked(color)):
            print("king is checked")
            changed = False
            nBoard = self.board[:]
            if nBoard[end[0]][end[1]].pawn:
                nBoard[end[0]][end[1]].first = True

            nBoard[end[0]][end[1]].change_pos((start[0], start[1]))
            nBoard[start[0]][start[1]] = nBoard[end[0]][end[1]]
            nBoard[end[0]][end[1]] = 0
            self.board = nBoard
        else:
            self.reset_selected()

        self.update_moves()
        if changed:
            self.last = [start, end]
            if self.turn == "w":
                self.storedTime1 += (time.time() - self.startTime)
            else:
                self.storedTime2 += (time.time() - self.startTime)
            self.startTime = time.time()

        return changed
        
    def reset_selected(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False    
        
    def update_moves(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].update_valid_moves(self.board)
                    
    def get_danger_moves(self, color):
        danger_moves = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].color != color:
                        for move in self.board[i][j].move_list:
                            danger_moves.append(move)

        return danger_moves

    def is_checked(self, color):
        self.update_moves()
        danger_moves = self.get_danger_moves(color)
        king_pos = (-1, -1)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    if self.board[i][j].king and self.board[i][j].color == color:
                        king_pos = (j, i)

        if king_pos in danger_moves:
            return True

        return False

                    
                    
#    def update_valid_moves(self, board): 
#        self.moveStack = self.valid_moves(board)