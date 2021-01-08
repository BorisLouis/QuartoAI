from Core import QuartoGame
from UI import QuartoUI
import time
import pygame

#few standard messages
AIPLAYING   = 'The AI is playing'
AICHOOSING  = 'The AI is choosing the next piece'
AICHOICE    = 'AI chose the piece circled in red'
PPLAYING    = 'Please select the position where you want to place the piece'
PCHOOOSING  = 'Please select the next piece that needs to be played'
PCHOICE     = 'Player chose the piece circled in red'

def run():
    game_over = False
    #Initialize the AI, UI and game
    AI = QuartoGame.QuartoAI()
    UI = QuartoUI.QuartoUI()
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
        if game.currentPiece == None:
            if currentPlayer != 'player'and not game_over:
                UI.update(game.pieces, game.board, AICHOOSING)
                piece = AI.chooseNextPiece(game.board)
                #get rectangle corresponding to the piece
                rect  = list(UI.rectDict.keys())[list(UI.rectDict.values()).index(piece)]

                if piece !=None:
                    UI.update(game.pieces,game.board,AICHOICE,rect)
                    game.updatePieceToPlay(piece)
                    # After the piece is chosen, we need to switch player
                    game.switchPlayer()

            else:
                UI.update(game.pieces,game.board, PCHOOOSING)
                # Check for a user move
                click = False
                for event in pygame.event.get():
                    if event.type == 5:
                        click = True
                        pos = event.pos

                if click and currentPlayer == 'player' and not game_over:
                    #get position clicked
                    piece,rect = getClickedPosition(UI.rectDict,pos)
                    if piece !=None:
                        UI.update(game.pieces,game.board,PCHOICE,rect)
                        game.updatePieceToPlay(piece)
                        # After the piece is chosen, we need to switch player
                     #   game.switchPlayer()
                        pygame.event.clear()

        else:
        # CURRENT PLAYER NEEDS TO CHOOSE WHERE TO PUT THE PIECE
            # Check for AI move
            if currentPlayer != 'player' and not game_over:
                    UI.update(game.pieces,game.board, AIPLAYING, rect)
                    action = AI.chooseAction(game.board)
                    game.updateBoard(action)

            else:
                UI.update(game.pieces, game.board, PPLAYING, rect)
                #check for player move
                click = False
                for event in pygame.event.get():
                    if event.type == 5:
                        click = True
                        pos = event.pos

                if click and currentPlayer == 'player' and not game_over:

                    case,bRect = getClickedPosition(UI.boardDict,pos)
                    action = {case:game.currentPiece}
                    #update board based on the player action
                    game.updateBoard(action)
                    #remove the current piece from current piece
                    game.updatePieceToPlay(None)
                    #clear the event list
                    pygame.event.clear()
                    #switch player
                    #game.switchPlayer()


####### HELPER FUNCTIONS #######
def getClickedPosition(rectList,mouse):

    isValidPos = None
    for key, elem in rectList.items():
        rect = pygame.Rect(key)
        isValidPos = rect.collidepoint(mouse)
        if isValidPos:
            return elem,rect
    return None,None
