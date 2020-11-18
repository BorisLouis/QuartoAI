from copy import deepcopy
EMPTY = None
class QuartoGame:
    """
    QuartoGame representation
    """
    def __init__(self):
        #Set the parameter for quarto game
        self.height = 4
        self.width  = 4

        self.board  = [[(1,1,0,0), EMPTY, EMPTY, EMPTY,],
                       [EMPTY, EMPTY, EMPTY, EMPTY,],
                       [EMPTY, EMPTY, EMPTY, EMPTY,],
                       [EMPTY, EMPTY, EMPTY, EMPTY,]]


    def getBoard(self):
        return self.board

    def player(self):
        """
           Returns player who has the next turn on a board.
        """
        raise NotImplementedError

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
