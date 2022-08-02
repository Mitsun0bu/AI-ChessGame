# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    chessMain.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: llethuil <lucas.lethuillier@gmail.com>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/08/02 13:01:23 by llethuil          #+#    #+#              #
#    Updated: 2022/08/02 17:35:11 by llethuil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import  pygame      as      p
import  chessEngine

SCREEN_WDTH = SCREEN_HGT = 1024
BOARD_WDTH = BOARD_HGT = 512
DIMENSION = 8
SQ_SIZE = BOARD_WDTH // DIMENSION
MAX_FPS = 15
BOARD_IMG = p.image.load("images/boards/board512.png")
PIECES_IMG = {}

def loadPiecesImg():
    '''
    This function initializes a global dictionnary of pieces images. It will be called once in the main.
    ''' 
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        # PIECES_IMG[piece] = p.transform.scale(p.image.load("images/pieces/" + piece + ".png"), (SQ_SIZE/1.5, SQ_SIZE/1.5))
        PIECES_IMG[piece] = p.image.load("images/pieces/" + piece + ".png")


def main():
    '''
    This function is the main. It will handle user inputs and update the graphics."
    ''' 
    p.init()
    screen = p.display.set_mode([SCREEN_WDTH, SCREEN_HGT])
    clock = p.time.Clock()
    state = chessEngine.GameState()
    loadPiecesImg()
    running = True
    sqSelected = () # No square selected, keep track of the last click of the user (tuple : (row, col))
    playerClicks = [] # Keep track of player clicks (two tuples : [(row_1, col_1), (row_2, col_2)])
    while running :
        screen.fill("black")
        screen.blit(BOARD_IMG, (SCREEN_WDTH/4, SCREEN_HGT/4))
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # mouse handler  
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x, y) location of the mouse
                col = location[0]//SQ_SIZE - 4
                row = location[1]//SQ_SIZE - 4
                if sqSelected == (row, col): # check if user clicked the same square twice
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # append for both 1st and @nd clicks
                if len(playerClicks) == 2: # after 2nd click
                    move = chessEngine.Move(playerClicks[0], playerClicks[1], state.board)
                    print(move.getChessNotation())
                    state.makeMove(move)
                    sqSelected = () # reset user click
                    playerClicks = []
            #key handler
            if e.type == p.KEYDOWN:
                if e.key == p.K_z: # undo move when 'z' is pressed
                    state.undoMove()

        drawPieces(screen, state.board)     
        clock.tick(MAX_FPS)
        p.display.flip()


def drawPieces(screen, board):
    '''
        This function draw the pieces on the board using the current GameState.board."
    ''' 
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(PIECES_IMG[piece], (c*SQ_SIZE + SCREEN_WDTH/4 + SQ_SIZE/4, r*SQ_SIZE + SCREEN_HGT/4 - SQ_SIZE/2))

if __name__ == "__main__":
    main()