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

        self.pieces = [[(0,0,0,0),(0,0,1,0)],
                       [(1,0,0,0),(1,0,1,0)],
                       [(0,0,0,1),(0,0,1,1)],
                       [(1,0,0,1),(1,0,1,1)],
                       [(0,1,0,0),(0,1,1,0)],
                       [(1,1,0,0),(1,1,1,0)],
                       [(0,1,0,1),(0,1,1,1)],
                       [(1,1,0,1),(1,1,1,1)],]

        self.currentPiece = None

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
        assert(piece == None or len(piece)==4 and isinstance(piece,tuple))
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
        assert isinstance(action,dict), 'action is expected to be a dictionary with the case and the piece'
        assert len(action)==1, 'action is expected to contain only a single action'
        board = self.board
        pos = list(action.keys())
        piece = action[pos[0]]

        board[pos[0][0]][pos[0][1]] = piece
        self.board = board


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
