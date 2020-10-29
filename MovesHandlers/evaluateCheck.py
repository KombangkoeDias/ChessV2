from side import side
from type import type
from EvaluateMovesEngine import EvaluateMovesEngine


class EvaluateCheck: # it will check the walks or eats and filter them so that it won't trigger check to its side.
    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.evaluateMoveEngine = EvaluateMovesEngine(self.chessboard,self) # create a new evaluateMoveEngine object so that it won't affect the board's moveEngine
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
    def filterWalks(self,walkSquares,firstSquare):
        return self.filter(walkSquares,firstSquare)
    def filterEats(self,eatSquares,firstSquare):
        return self.filter(eatSquares,firstSquare)
    def filter(self,Squares,firstSquare):
        """ filter the moves so that it won't trigger check to its own side which is forbidden by the rule"""
        resultlist = list() # the result list
        for i in range(len(Squares)):
            currentSide = firstSquare.Piece.side
            firstPiece = firstSquare.Piece
            secondPiece = Squares[i].Piece

            # move without animation
            self.chessboard.walkOrEatWithoutAnimation(firstSquare,Squares[i])

            # we will choose and not choose to add into resultlist
            if(self.checkCheck(currentSide)): # if the move makes its own side checked then not include it
                print("remove", self.chessboard.findIJSquare(Squares[i]))
            else: # if not it will be add into resultlist.
                resultlist.append(Squares[i])
            # then move back
            firstSquare.addPieces(firstPiece)
            Squares[i].addPieces(secondPiece)
        return resultlist

    def detect_CheckMate(self):
        """ detect if the each side has been checked mate. return side object"""
        # TODO Create CheckMate detecting function
        pass
