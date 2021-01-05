from copy import deepcopy
import random
EMPTY = None

class QuartoGame:
    """
    QuartoGame representation
    """
    def __init__(self):
        #Set the parameter for quarto game
        self.height = 4
        self.width  = 4

        self.board  = [[EMPTY, EMPTY, EMPTY, EMPTY,],
                       [EMPTY, EMPTY, EMPTY, EMPTY,],
                       [EMPTY, EMPTY, EMPTY, EMPTY,],
                       [EMPTY, EMPTY, EMPTY, EMPTY,]]

        number = 0#random.randint(0,1)

        if number == 0:
            self.player = 'player'
        else:
            self.player = 'AI'

    def getBoard(self):
        return self.board

    def getPlayer(self):
        """
           Returns player who has the next turn on a board.
        """
        return self.player

    def switchPlayer(self):
        if self.player == 'AI':
            self.player = 'player'
        else:
            self.player = 'AI'
    def updatePieceToPlay(self,piece):
        self.currentPiece = piece


    def actions(self):
        """
           Returns set of all possible actions (i, j) available on the board.
        """
        raise NotImplementedError

    def updateBoard(self,action):
        """
        Update the board following the action chosen
        """
        raise NotImplementedError

    def winner(self):
        """
        Returns the winner of the game if any
        """
        raise NotImplementedError

    def terminal(self):
        """
        Returns True if game is over, false otherwise
        """
        raise NotImplementedError


class QuartoAI:
    def __init__(self, alpha=0.5, epsilon=0.1):
        self.q = dict()
        self.alpha = alpha
        self.epsilon = epsilon

    def chooseAction(self, board):
        raise NotImplementedError

    def chooseNextPiece(self, board):
        raise NotImplementedError
