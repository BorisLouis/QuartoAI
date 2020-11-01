"""
Quarto AI player
"""
import time

from Core import QuartoGame
from UI import QuartoUI

UI = QuartoUI.QuartoUI()

i = 1
while True:
    UI.update()
    time.sleep(100)
    break
