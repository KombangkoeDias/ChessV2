import copy # will use copy library to do deep copy of the chessboard and then make changes to it.
from side import side
from type import type
from EvaluateMovesEngine import EvaluateMovesEngine

class EvaluateCheck: # it will check the walks or eats and filter them so that it won't trigger check to its side.
    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.evaluateMoveEngine = EvaluateMovesEngine(self.chessboard)
    def checkCheck(self,side):
        """ return True if the side in input is being checked and False if not"""
        for i in range(8):
            for j in range(8):
                currSquare = self.chessboard.getSquare(i,j)
                if (currSquare.Piece.type != type.Empty and currSquare.Piece.side != side): # if it's not empty and it's opponent
                    # the evaluateMoveEngine handlers will clear all the results before evaluating again so no problem.
                    eatSquares = self.evaluateMoveEngine.getPossibleEats(currSquare)
                    for eat in eatSquares:
                        if (side == side.blackside and eat.Piece.type == type.KingB or
                                side == side.whiteside and eat.Piece.type == type.KingW):
                            return True
        return False
    def filterWalks(self,walkSquares):
        pass
    def filterEats(self,eatSquares):
        pass
    def filter(self,Squares):
        pass

