"""
Quarto AI player
"""
import time

from Controller import QuartoController
from UI import QuartoUI

#QuartoController.run()
EMPTY = None
state = [[EMPTY, EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY, EMPTY]]


UI = QuartoUI.QuartoUI()
while True:
    UI.update(state,'POGU')
    time.sleep(20)
    break