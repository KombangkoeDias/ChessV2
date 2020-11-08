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
        if(len(Squares) > 0):
            for i in range(len(Squares)):
                thisSquare = Squares[i] # somehow the square got lost and needed to be put in a variable here ##fixed!!
                currentSide = firstSquare.Piece.side
                firstPiece = firstSquare.Piece
                secondPiece = Squares[i].Piece
                (row,col) = self.chessboard.findIJSquare(thisSquare)
                enpassantSquare = None
                enpassantPiece = None

                # logic to find enpassant
                enpassant = (firstSquare.Piece.type == type.PawnW or firstSquare.Piece.type == type.PawnB) and (
                    thisSquare.Piece.type == type.Empty and self.chessboard.findIJSquare(firstSquare)[1] !=
                    self.chessboard.findIJSquare(thisSquare)[1]
                )

                # if enpassant we store the enpassant piece and square in advance.
                if (enpassant):
                    if (firstPiece.type == type.PawnB):
                        enpassantSquare = self.chessboard.getSquare(row-1,col)
                    elif(firstPiece.type == type.PawnW):
                        enpassantSquare = self.chessboard.getSquare(row+1,col)
                    enpassantPiece = enpassantSquare.Piece
                # move without animation
                self.chessboard.walkOrEatWithoutAnimation(firstSquare,Squares[i],enpassant)

                # we will choose and not choose to add into resultlist
                if(self.checkCheck(currentSide)): # if the move makes its own side checked then not include it
                    print("remove", self.chessboard.findIJSquare(thisSquare), "of", firstPiece.type)
                else: # if not it will be add into resultlist.
                    resultlist.append(thisSquare)

                # then move back

                firstSquare.addPieces(firstPiece)
                thisSquare.addPieces(secondPiece)
                if(enpassant): # and after the move we add the eaten piece in the enpassant process.
                    enpassantSquare.addPiece(enpassantPiece)

        return resultlist

    def detect_CheckMate(self,side):
        """ detect if the each side has been checked mate. return side object"""

        totalMoves = 0
        if (self.checkCheck(side)):
            for i in range(8):
                for j in range(8):
                    currSquare = self.chessboard.getSquare(i,j)
                    if (currSquare.Piece.type != type.Empty and currSquare.Piece.side == side):
                        if (totalMoves > 0):
                            return False
                        totalMoves += len(self.evaluateMoveEngine.getFilteredPossibleWalks(currSquare))
                        totalMoves += len(self.evaluateMoveEngine.getFilteredPossibleEats(currSquare))
            if (totalMoves == 0 and self.checkCheck(side)):
                if (side == side.whiteside ):
                    print("white is checked mate, black wins")
                if (side == side.blackside ):
                    print("black is checked mate, white wins")
                return True
        return False
