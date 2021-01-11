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
        board = self.board

        isNone = True
        for row in board:
            for col in row:
                if col != None:
                    isNone = False
                    break
        if isNone:
            return False,(None,None)
        else:
            #need to check rows, column and diagonals
            sumCol = []
            sumRow = []
            sumDiag = []
            sumDiag.append((0,0,0,0))
            sumDiag.append((0,0,0,0))

            for i in range(0,len(board)):
                sumRow.append((0,0,0,0))

                for j in range(0,len(board[0])):
                    if i == 0:
                        sumCol.append((0,0,0,0))
                    if board[i][j] != None:
                        #check row
                        if j>0:
                            tupComp = compareTuple(board[i][j-1],board[i][j])
                            sumRow[i] = tuple(map(sum, zip(sumRow[i], tupComp)))

                        if i>0:
                            tupComp = compareTuple(board[i-1][j],board[i][j])
                            sumCol[j] = tuple(map(sum, zip(sumCol[j], tupComp)))

                        #main diagonal
                        if i == j and i>0:
                            tupComp = compareTuple(board[i-1][j-1],board[i][j])
                            sumDiag[0] = tuple(map(sum, zip(sumDiag[0],tupComp)))

                        if j <len(board)-1 and (i == len(board[0])-j or j == len(board[0])-i):
                            tupComp = compareTuple(board[i-1][j+1],board[i][j])
                            sumDiag[1] = tuple(map(sum, zip(sumDiag[1], tupComp)))

            #check row
            for i in range(0,len(board)):
                for j in range(0,len(board[0])):
                    if sumRow[i][j] == len(board[0])-1:
                        #1 means row
                        return True,(i,1,j)
                    if sumCol[i][j] == len(board[0])-1:
                        #2 mean col
                        return True,(i,2,j)
                    if i <2:
                        #3 mean diag
                        if sumDiag[i][j] == len(board[0])-1:
                            return True,(i,3,j)

            return False,(None,None)

def compareTuple(tuple1,tuple2):
    boolTup = []
    if tuple1 == None or tuple2 == None:
        return (0,0,0,0)

    for i in range(0,len(tuple1)):
        if tuple1[i] == tuple2[i]:
            boolTup.append(1)
        else:
            boolTup.append(0)

    return tuple(boolTup)





class QuartoAI:
    def __init__(self, alpha=0.5, epsilon=0.1):
        self.q = dict()
        self.alpha = alpha
        self.epsilon = epsilon

    def chooseAction(self, board):
        raise NotImplementedError

    def chooseNextPiece(self, board):
        raise NotImplementedError
