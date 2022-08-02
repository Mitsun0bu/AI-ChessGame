# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    chessEngine.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: llethuil <lucas.lethuillier@gmail.com>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/02 13:01:08 by llethuil          #+#    #+#              #
#    Updated: 2022/08/02 17:19:02 by llethuil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GameState():
    def __init__(self):
    # The board is an 8x8 2D list.
    # Each piece is represented as a 2 character string, the 1st one indicating its color
    # Empty squares are represented as "--"
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []
    

    def makeMove(self, move):
        ''' 
            This function take a Move as parameter and execute it. It won't work for castling, pawn promotion and en passant.
        '''
        self.board[move.startRow][move.startCol] = '--'
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) # log the move  so we can undo it later
        self.whiteToMove = not self.whiteToMove # swap players


    def undoMove(self):
        ''' 
            This function undo the lase move made by the player.
        '''
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove # swap players


# VIDEO PART 3 - 11 minutes


class Move():
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}        
    
    
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        # Modifications here to make this like real chess notation
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)


    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
