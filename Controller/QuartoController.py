from Core import QuartoGame
from UI import QuartoUI
import time

def run():
    while True:
        UI = QuartoUI.QuartoUI()
        game = QuartoGame.QuartoGame()
        state = game.board
        UI.update(state)

        


        time.sleep(10)
        break