from Core import QuartoGame
from UI import QuartoUI
import time
import pygame

AIPLAYING   = 'The AI is playing'
AICHOOSING  = 'The AI is choosing the next piece'
PPLAYING    = 'Please select the position where you want to place the piece'
PCHOOOSING  = 'Please select the next piece that need to be played'

def run():
    game_over = False
    #Initialize the AI, UI and game
    AI = QuartoGame.QuartoAI()
    qUI = QuartoUI.QuartoUI()
    game = QuartoGame.QuartoGame()



    while True:
        for event in pygame.event.get():
            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()
                # quit the program.
                quit()

        currentPlayer = game.getPlayer()

        # CURRENT PLAYER NEEDS TO CHOOSE THE PIECE FOR THE NEXT PLAYER
        #display message to user
        if currentPlayer != 'player'and not game_over:
            qUI.update(game.board, AICHOOSING)
            # After the piece is chosen, we need to switch player
            game.switchPlayer()

        else:
            qUI.update(game.board, PCHOOOSING)
            # Check for a user move
            click, _, _ = pygame.mouse.get_pressed()

            if click == 1 and currentPlayer == 'player' and not game_over:
                #get position clicked
                mouse = pygame.mouse.get_pos()
                rectList = getPiecePosition(qUI.cells)

                isValidPos = getClickedPos(rectList,mouse)

                if isValidPos !=None:
                    qUI.update(game.board,'Player chose the piece circled in red',isValidPos)
                    game.updatePieceToPlay(isValidPos)
                    # After the piece is chosen, we need to switch player
                    game.switchPlayer()


        # CURRENT PLAYER NEEDS TO CHOOSE WHERE TO PUT THE PIECE
        # Check for AI move
        #if currentPlayer != 'player' and not game_over:
        #        UI.update(game.board, AIPLAYING)
        #        time.sleep(0.5)
        #        action = AI.chooseAction(game.board)
        #        game.updateBoard(action)
        #        piece  = AI.chooseNextPiece(game.board)
        #else:
#
 #           # Check for a user move
  #          click, _, _ = pygame.mouse.get_pressed()
#
 #           if click == 1 and currentPlayer == 'player' and not game_over:
  #              UI.update(game.board, PPLAYING)
   #             raise NotImplementedError
    #            mouse = pygame.mouse.get_pos()
     #           for i in range(3):
      #              for j in range(3):
       #                 if (board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse)):
        #                    board = ttt.result(board, (i, j))

def getPiecePosition(cells):
    xbl = []
    ybl = []

    for cell in cells:
        for r in cell:
            xbl.append(r.topleft[0])
            ybl.append(r.topleft[1])

    xbl = set(xbl)
    ybl = set(ybl)

    xbl.remove(max(xbl))
    bl = (max(xbl), min(ybl))
    blRect = pygame.Rect(bl[0], bl[1], 2 * r[3], 8 * r[3])

    rectList = []
    for cell in cells:
        for r in cell:
            x = r.topleft[0]
            y = r.topleft[1]

            if blRect[0] <= x <=blRect[0]+blRect[2] and blRect[1] <= y <=blRect[1]+blRect[3]:
                rectList.append(r)

    return rectList

def getBoardPosition(cells):
    xbl = []
    ybl = []

    for cell in cells:
        for r in cell:
            xbl.append(r.topleft[0])
            ybl.append(r.topleft[1])

    xbl = set(xbl)
    ybl = set(ybl)

    # we remove the two first minimum
    ybl.remove(min(ybl))
    ybl.remove(min(ybl))

    # here we take the min x  and the min y (third one)
    bl = (min(xbl), min(ybl))
    blRect = pygame.Rect(bl[0], bl[1], 4 * r[3], 4 * r[3])

    rectList = []
    for cell in cells:
        for r in cell:
            x = r.topleft[0]
            y = r.topleft[1]

            if blRect[0] <= x <= blRect[0] + blRect[2] and blRect[1] <= y <= blRect[1] + blRect[3]:
                rectList.append(r)

    return rectList

def getClickedPos(rectList,mouse):

    isValidPos = None
    for rect in rectList:
        isValidPos = rect.collidepoint(mouse)

        if isValidPos:
            return rect

    return isValidPos
