from side import side
from type import type
from EvaluateMovesEngine import EvaluateMovesEngine


class EvaluateCheck: # it will check the walks or eats and filter them so that it won't trigger check to its side.
    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.evaluateMoveEngine = EvaluateMovesEngine(self.chessboard,self)
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
        poplist = list()
        for i in range(len(Squares)):
            currentSide = firstSquare.Piece.side
            firstPiece = firstSquare.Piece
            secondPiece = Squares[i].Piece

            # move without animation
            self.chessboard.walkOrEatWithoutAnimation(firstSquare,Squares[i])

            # we use poplist to note which one we will choose and not choose to add into resultlist
            if(self.checkCheck(currentSide)): # if the move makes its own side checked then pop it (1)
                print("remove", self.chessboard.findIJSquare(Squares[i]))
                poplist.append(1)
            else: # if not marked it 0 to be add into resultlist.
                poplist.append(0)

            # then move back
            firstSquare.addPieces(firstPiece)
            Squares[i].addPieces(secondPiece)

        resultlist = list() # the result list
        for i in range(len(poplist)):
            if(poplist[i] == 0): # if it's not pop (0) then add it to result list.
                resultlist.append(Squares[i])
        return resultlist
    def detect_CheckMate(self):
        """ detect if the each side has been checked mate. return side object"""
        pass
