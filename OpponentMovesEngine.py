from side import side
from type import type
from MovesHandlers.evaluateCheck import EvaluateCheck
from EvaluateMovesEngine import EvaluateMovesEngine
from Moves import Moves
import time

Score = {type.PawnW: 1, type.PawnB: 1,
         type.KnightW: 3, type.KnightB: 3,
         type.BishopW: 3, type.BishopB: 3,
         type.RookW: 5, type.RookB: 5,
         type.QueenW: 8, type.QueenB: 8,
         type.KingW: 1000,type.KingB: 1000}

bestScore = None  # the variable for bestMove's best score
bestMove = None  # the return variable for the best move possible

class OpponentMovesEngine:
    def __init__(self,chessboard):
        self.chessboard = chessboard

        self.PlayerSide = self.chessboard.currentSide # the side player choose
        if (self.PlayerSide == side.whiteside):  # so the opponent side will be opposite
            self.OpponentSide = side.blackside
        else:
            self.OpponentSide = side.whiteside
    def findBestMovesUsingAlPhaBetaPruning(self):
        """
        This function finds best moves by searching the all possible state space search
        with the well-known pruning technic - alpha, beta pruning -
        """
        #TODO implement alpha beta pruning algorithm for search space
        global bestScore
        global bestMove
        # we clear the global variables every time we run this function so it calculates from scratch
        bestScore = None
        bestMove = None
        # for timing purpose
        start = time.time()
        #self.chessboard.printBoard()
        Node(self.chessboard,0,self.OpponentSide,self.OpponentSide)  # call the first Node to build Node tree
        end = time.time()
        print("time used:",end - start)  # time used
        print(bestScore)  # best score achieved
        # for debugging purpose
        print("best move is from",self.chessboard.findIJSquare(bestMove.getFirstSquare())
              ,"to",self.chessboard.findIJSquare(bestMove.getSecondSquare()))
        return bestMove  # return the best move (as a Moves object)
    def findBestMovesUsingMachineLearning(self):
        """
        This function finds best moves by running machine learning
        """
        #TODO implement machine learning network to determine best move
        pass



class Node:
    def __init__(self,chessboard,depth,OpponentSide,playSide,topRootMove=None):
        self.maxDepthSearch = 2  # the max height of the tree
        self.whiteSumValue = 0  # for calculating score purpose
        self.blackSumValue = 0  # for calculating score purpose
        self.chessboard = chessboard
        self.depth = depth  # current depth of the Node
        self.topRootMove = topRootMove  # depth0 (root) node's move of the current Node
        self.evaluateCheckEngine = EvaluateCheck(self.chessboard)
        self.evaluateMovesEngine = EvaluateMovesEngine(self.chessboard, self.evaluateCheckEngine)
        self.playSide = playSide  # the side that is playing (change with depth)
        self.OpponentSide = OpponentSide  # the side opponent is (the opposite side of player side)(permanent no change)
        self.determineMoves()  # after creating the node we run determineMoves which will create leaf nodes of this node

    def EvaluateScore(self):
        """Evaluate Score of the node (will be called if the node's depth reaches the max depth search)"""
        self.whiteSumValue = 0
        self.blackSumValue = 0
        for i in range(8):
            for j in range(8):
                currSquare = self.chessboard.getSquare(i, j)
                if (currSquare.Piece.type != type.Empty):
                    if (currSquare.Piece.side == side.whiteside):
                        self.whiteSumValue += Score[currSquare.Piece.type]
                    else:
                        self.blackSumValue += Score[currSquare.Piece.type]
        # calculate score by sum all white pieces' score and subtracts the sum of all black pieces' score
        return self.whiteSumValue - self.blackSumValue

    def determineMoves(self):
        """Create leaf nodes associated with the node by being the possible next moves of the node itself."""
        global bestScore
        global bestMove
        # if the max depth is reached we just calculate score and compare it with the global variables as well as
        # update them
        if (self.depth == self.maxDepthSearch):
            if(self.OpponentSide == side.blackside):  # for black side we'll prefer low score
                if(bestScore == None):
                    bestScore = self.EvaluateScore()
                    bestMove = self.topRootMove
                elif(self.EvaluateScore() < bestScore):
                    bestScore = self.EvaluateScore()
                    bestMove = self.topRootMove
            else:  # for white side we'll prefer high score
                if(bestScore == None):
                    bestScore = self.EvaluateScore()
                elif(self.EvaluateScore() > bestScore):
                    bestScore = self.EvaluateScore()
        # if the max depth is not reached we'll find all possible moves considering the current play side
        else:
            # determine all pieces' square contains play side's piece.
            OpponentPieceSquares = self.determinePlaySidePieceSquares()
            for square in OpponentPieceSquares:  # for every square contain play side's piece we find all moves
                walkSquares = self.evaluateMovesEngine.getFilteredPossibleWalks(square)
                eatSquares = self.evaluateMovesEngine.getFilteredPossibleEats(square)

                # for each move we'll create a child node which will have different play side
                for walksquare in walkSquares:
                    # find enpassant
                    enpassant = False
                    firstRow, firstCol = self.chessboard.findIJSquare(square)
                    secondRow, secondCol = self.chessboard.findIJSquare(walksquare)

                    # find castling
                    castling = (square.Piece.type == type.KingW or square.Piece.type == type.KingB) \
                               and abs(secondCol - firstCol) == 2
                    tryMove = Moves(square, square.Piece, walksquare, walksquare.Piece,enpassant,castling,False)

                    # if the node is the root node we'll change the topRootMove variable and pass it on
                    if(self.depth == 0):
                        self.topRootMove = tryMove

                    # do walk
                    self.chessboard.walkOrEatWithoutAnimation(square,walksquare,enpassant=False)

                    # then create node according to the play side and depth equals to current depth + 1
                    if(self.playSide == side.whiteside):
                        Node(self.chessboard,self.depth+1,self.OpponentSide,side.blackside,topRootMove=self.topRootMove)
                    else:
                        Node(self.chessboard,self.depth+1,self.OpponentSide,side.whiteside,topRootMove=self.topRootMove)
                    # after we do all the Node's operation we'll move the board back
                    self.chessboard.reverseMoves(test=True,lastmove=tryMove)

                for eatsquare in eatSquares:
                    # find enpassant
                    enpassant = eatsquare.Piece.type == type.Empty
                    firstRow, firstCol = self.chessboard.findIJSquare(square)
                    secondRow, secondCol = self.chessboard.findIJSquare(eatsquare)

                    # find castling
                    castling = (square.Piece.type == type.KingW or square.Piece.type == type.KingB) \
                               and abs(secondCol - firstCol) == 2
                    tryMove = Moves(square,square.Piece,eatsquare,eatsquare.Piece,enpassant,castling,False)

                    # if the node is the root node we'll change the topRootMove variable and pass it on
                    if (self.depth == 0):
                        self.topRootMove = tryMove

                    # do walk
                    self.chessboard.walkOrEatWithoutAnimation(square,eatsquare,enpassant=enpassant)

                    # then create node according to the play side and depth equals to current depth + 1
                    if (self.playSide == side.whiteside):
                        Node(self.chessboard, self.depth + 1,self.OpponentSide, side.blackside,topRootMove=self.topRootMove)
                    else:
                        Node(self.chessboard, self.depth + 1,self.OpponentSide, side.whiteside,topRootMove=self.topRootMove)

                    # after we do all the Node's operation we'll move the board back
                    self.chessboard.reverseMoves(test=True,lastmove=tryMove)

    def determinePlaySidePieceSquares(self):
        OpponentPieceSquares = list()
        for i in range(8):
            for j in range(8):
                currSquare = self.chessboard.getSquare(i,j)
                # add only those that have side equals to the current play side.
                if (currSquare.Piece.type != type.Empty and currSquare.Piece.side == self.playSide):
                    OpponentPieceSquares.append(currSquare)
        return OpponentPieceSquares
