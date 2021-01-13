from Core import QuartoGame
from UI import QuartoUI
import time
import pygame

#few standard messages
AIPLAYING   = 'The AI is playing'
AICHOOSING  = 'The AI is choosing the next piece'
AICHOICE    = 'AI chose the piece circled in red'
PPLAYING    = ' please select the piece position'
PCHOOOSING  = ' please select a piece to be played'
PCHOICE     = ' chose the piece circled in red'
PPieceChoice = ' placed the piece'
def run():
    game_over = False
    #Initialize the AI, UI and game
    game = QuartoGame.QuartoGame()
    AI = QuartoGame.QuartoAI()
    UI = QuartoUI.QuartoUI()


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
        if game.currentPiece == None and not game_over:
            #AI decide the piece
            if  'Player' not in currentPlayer:
                UI.update(game.pieces, game.board, AICHOOSING)
                piece = AI.chooseNextPiece(game.board)
                #get rectangle corresponding to the piece
                rect  = list(UI.rectDict.keys())[list(UI.rectDict.values()).index(piece)]

                if piece !=None:
                    UI.update(game.pieces,game.board,AICHOICE,rect)
                    game.updatePieceToPlay(piece)
                    # After the piece is chosen, we need to switch player
                    game.switchPlayer()
            #Player decide the piece
            elif 'Player' in currentPlayer:
                UI.update(game.pieces,game.board, game.currentPlayer + PCHOOOSING)
                # Check for a user move
                click = False
                for event in pygame.event.get():
                    if event.type == 5:
                        click = True
                        pos = event.pos

                if click and not game_over:
                    #get position clicked
                    #TODO CHECK IF POSITION IS VALID
                    piece,rect = getClickedPosition(UI.rectDict,pos)
                    if piece !=None:
                        UI.update(game.pieces,game.board,game.currentPlayer + PCHOICE,rect)
                        game.updatePieceToPlay(piece)
                        # After the piece is chosen, we need to switch player
                        game.switchPlayer()
                        pygame.event.clear()

        elif game.currentPiece != None and not game_over:
        # CURRENT PLAYER NEEDS TO CHOOSE WHERE TO PUT THE PIECE
            # Check for AI move
            if 'Player' not in currentPlayer and not game_over:
                    UI.update(game.pieces,game.board, AIPLAYING, rect)
                    action = AI.chooseAction(game.board)
                    game.updateBoard(action)

            elif 'Player' in currentPlayer:
                UI.update(game.pieces, game.board, game.currentPlayer + PPLAYING, rect)
                #check for player move
                click = False
                for event in pygame.event.get():
                    if event.type == 5:
                        click = True
                        pos = event.pos

                if click and not game_over:

                    case,bRect = getClickedPosition(UI.boardDict,pos)
                    action = {case:game.currentPiece}
                    #update board based on the player action
                    game.updateBoard(action)
                    #remove the current piece from current piece
                    game.updatePieceToPlay(None)
                    #clear the event list
                    pygame.event.clear()

                    UI.update(game.pieces, game.board, game.currentPlayer + PPieceChoice)

        game_over,reason = game.terminal()

        if game_over:

            message = 'The winner is ' + game.currentPlayer
            UI.update(game.pieces, game.board, message)
            time.sleep(3)

            message = generateEndingMessage(game.currentPlayer,reason)
            UI.update(game.pieces, game.board, message)
            time.sleep(3)


def generateEndingMessage(player, reason):

    if reason[1] == 1:
        ach = 'row'
    elif reason[1] == 2:
        ach = 'column'
    elif reason[1] == 3:
        ach = 'diagonal'

    if reason[2] == 0:
        type = 'size'
    elif reason[2] == 1:
        type = 'color'
    elif reason[2] == 2:
        type = 'shape'
    elif reason[2] == 2:
        type = 'fullness'

    message = player + ' made a ' + ach + ' of four pieces of the same ' + type

    return message




####### HELPER FUNCTIONS #######
def getClickedPosition(rectList,mouse):

    isValidPos = None
    for key, elem in rectList.items():
        rect = pygame.Rect(key)
        isValidPos = rect.collidepoint(mouse)
        if isValidPos:
            return elem,rect
    return None,None
