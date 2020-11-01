"""
Quarto AI player
"""
from Core import QuartoGame
from UI import QuartoUI

UI = QuartoUI.QuartoUI()

i = 1
while True:
    UI.update()
    i = i+1
    if i == 1e4:
        break
