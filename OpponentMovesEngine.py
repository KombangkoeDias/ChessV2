from side import side
from type import type
from MovesHandlers.evaluateCheck import EvaluateCheck
from EvaluateMovesEngine import EvaluateMovesEngine

Score = {type.PawnW: 1, type.PawnB: 1,
         type.KnightW: 3, type.KnightB: 3,
         type.BishopW: 3, type.BishopB: 3,
         type.RookW: 5, type.RookB: 5,
         type.QueenW: 8, type.QueenB: 8,
         type.KingW: 1000,type.KingB: 1000}

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

        for i in range(8):
            for j in range(8):
                currSquare = self.chessboard.getSquare(i,j)
                if(currSquare.Piece.side == self.OpponentSide):
                    print(currSquare.Piece.type)

    def findBestMovesUsingMachineLearning(self):
        """
        This function finds best moves by running machine learning
        """
        #TODO implement machine learning network to determine best move
        pass



class Node:
    def __init__(self,chessboard,depth):
        self.Score = self.whiteSumValue - self.blackSumValue
        self.maxDepthSearch = 30
        self.whiteSumValue = 0
        self.blackSumValue = 0
        self.chessboard = chessboard
        self.depth = depth
        self.PlayerSide = self.chessboard.currentSide
        self.evaluateCheckEngine = EvaluateCheck(self.chessboard)
        self.evaluateMovesEngine = EvaluateMovesEngine(self.chessboard, self.evaluateCheckEngine)
        if (self.PlayerSide == side.whiteside):
            self.OpponentSide = side.blackside
        else:
            self.OpponentSide = side.whiteside
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
        self.Score = self.whiteSumValue - self.blackSumValue
    def determineMoves(self):
        if (self.depth == self.maxDepthSearch):
            self.EvaluateScore()
        else:
            OpponentPieceSquares = self.determineOpponentPieceSquares()
            for square in OpponentPieceSquares:
                walkSquares = self.evaluateMovesEngine.getFilteredPossibleWalks(square)
                eatSquares = self.evaluateMovesEngine.getFilteredPossibleEats(square)
                for walksquare in walkSquares:
                    self.chessboard.walkOrEatWithoutAnimation(square,walksquare)
                    childNode = Node(self.chessboard,self.depth+1)
                    #TODO implement reversewalkOrEatWithoutAnimation in ChessBoard
                for eatsquare in eatSquares:
                    self.chessboard.walkOrEatWithoutAnimation(square,eatsquare)
                    childNode = Node(self.chessboard,self.depth+1)
                    #TODO implement reversewalkOrEatWithoutAnimation in ChessBoard (same as above)

    def determineOpponentPieceSquares(self):
        OpponentPieceSquares = list()
        for i in range(8):
            for j in range(8):
                currSquare = self.chessboard.getSquare(i,j)
                if (currSquare.Piece.side == self.OpponentSide):
                    OpponentPieceSquares.append(currSquare)
        return OpponentPieceSquares
