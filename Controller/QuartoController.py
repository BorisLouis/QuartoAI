from Core import QuartoGame
from UI import QuartoUI
import time
import pygame

def run():
    game_over = False
    AI = QuartoGame.QuartoAI()
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

        UI = QuartoUI.QuartoUI()
        game = QuartoGame.QuartoGame()
        currentPlayer = game.getPlayer()
        UI.update(game.board, currentPlayer)

        # Check for AI move
        if currentPlayer != 'player' and not game_over:
                UI.update(game.board, 'AI is playing')
                time.sleep(0.5)
                action = AI.chooseAction(game.board)
                game.updateBoard(action)
                piece  = AI.chooseNextPiece(game.board)
        else:

            # Check for a user move
            click, _, _ = pygame.mouse.get_pressed()

            if click == 1 and currentPlayer == 'player' and not game_over:
                UI.update(game.board, 'Player turn, click where you want to place the piece')
                raise NotImplementedError
                mouse = pygame.mouse.get_pos()
                for i in range(3):
                    for j in range(3):
                        if (board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse)):
                            board = ttt.result(board, (i, j))


        time.sleep(10)
        break