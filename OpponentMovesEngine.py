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

bestScore = None
bestMove = None

class OpponentMovesEngine:
    def __init__(self,chessboard):
        self.chessboard = chessboard

        self.PlayerSide = self.chessboard.currentSide
        if (self.PlayerSide == side.whiteside):
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
        bestScore = None
        bestMove = None
        start = time.time()
        #self.chessboard.printBoard()
        Node(self.chessboard,0,self.OpponentSide,self.OpponentSide)
        end = time.time()
        print("time used:",end - start)
        print(bestScore)
        print("best move is from",self.chessboard.findIJSquare(bestMove.getFirstSquare())
              ,"to",self.chessboard.findIJSquare(bestMove.getSecondSquare()))
        return bestMove
    def findBestMovesUsingMachineLearning(self):
        """
        This function finds best moves by running machine learning
        """
        #TODO implement machine learning network to determine best move
        pass



class Node:
    def __init__(self,chessboard,depth,OpponentSide,playSide,topRootMove=None):
        self.maxDepthSearch = 2
        self.whiteSumValue = 0
        self.blackSumValue = 0
        self.chessboard = chessboard
        self.depth = depth
        self.topRootMove = topRootMove
        self.evaluateCheckEngine = EvaluateCheck(self.chessboard)
        self.evaluateMovesEngine = EvaluateMovesEngine(self.chessboard, self.evaluateCheckEngine)
        self.playSide = playSide
        self.OpponentSide = OpponentSide
        self.determineMoves()
    def EvaluateScore(self):
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
        return self.whiteSumValue - self.blackSumValue
    def determineMoves(self):
        global bestScore
        global bestMove
        if (self.depth == self.maxDepthSearch):
            if(self.OpponentSide == side.blackside):
                if(bestScore == None):
                    bestScore = self.EvaluateScore()
                    bestMove = self.topRootMove
                elif(self.EvaluateScore() < bestScore):
                    bestScore = self.EvaluateScore()
                    bestMove = self.topRootMove
            else:

                if(bestScore == None):
                    bestScore = self.EvaluateScore()
                elif(self.EvaluateScore() > bestScore):
                    bestScore = self.EvaluateScore()
        else:
            OpponentPieceSquares = self.determinePlaySidePieceSquares()
            for square in OpponentPieceSquares:
                walkSquares = self.evaluateMovesEngine.getFilteredPossibleWalks(square)
                eatSquares = self.evaluateMovesEngine.getFilteredPossibleEats(square)

                for walksquare in walkSquares:
                    enpassant = False
                    firstRow, firstCol = self.chessboard.findIJSquare(square)
                    secondRow, secondCol = self.chessboard.findIJSquare(walksquare)
                    castling = (square.Piece.type == type.KingW or square.Piece.type == type.KingB) \
                               and abs(secondCol - firstCol) == 2
                    tryMove = Moves(square, square.Piece, walksquare, walksquare.Piece,enpassant,castling,False)
                    if(self.depth == 0):
                        self.topRootMove = tryMove
                    self.chessboard.walkOrEatWithoutAnimation(square,walksquare,enpassant=False)
                    if(self.playSide == side.whiteside):
                        Node(self.chessboard,self.depth+1,self.OpponentSide,side.blackside,topRootMove=self.topRootMove)
                    else:
                        Node(self.chessboard,self.depth+1,self.OpponentSide,side.whiteside,topRootMove=self.topRootMove)
                    self.chessboard.reverseMoves(test=True,lastmove=tryMove)

                for eatsquare in eatSquares:
                    enpassant = eatsquare.Piece.type == type.Empty
                    firstRow, firstCol = self.chessboard.findIJSquare(square)
                    secondRow, secondCol = self.chessboard.findIJSquare(eatsquare)
                    castling = (square.Piece.type == type.KingW or square.Piece.type == type.KingB) \
                               and abs(secondCol - firstCol) == 2
                    tryMove = Moves(square,square.Piece,eatsquare,eatsquare.Piece,enpassant,castling,False)
                    if (self.depth == 0):
                        self.topRootMove = tryMove
                    self.chessboard.walkOrEatWithoutAnimation(square,eatsquare,enpassant=enpassant)
                    if (self.playSide == side.whiteside):
                        Node(self.chessboard, self.depth + 1,self.OpponentSide, side.blackside,topRootMove=self.topRootMove)
                    else:
                        Node(self.chessboard, self.depth + 1,self.OpponentSide, side.whiteside,topRootMove=self.topRootMove)
                    self.chessboard.reverseMoves(test=True,lastmove=tryMove)

    def determinePlaySidePieceSquares(self):
        OpponentPieceSquares = list()
        for i in range(8):
            for j in range(8):
                currSquare = self.chessboard.getSquare(i,j)
                if (currSquare.Piece.type != type.Empty and currSquare.Piece.side == self.playSide):
                    OpponentPieceSquares.append(currSquare)
        return OpponentPieceSquares
