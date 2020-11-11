from type import type
from side import side

class KingMovesHandler:
    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.possibleWalks = list()
        self.possibleEats = list()
    def findAllPossibleWalks(self,firstSquare):
        self.possibleWalks.clear() # clear the results before evaluating
        (row,col) = self.chessboard.findIJSquare(firstSquare)
        surroundSquares = [(row-1,col-1),(row-1,col),(row-1,col+1),(row,col-1),(row,col),(row,col+1),(row+1,col-1),(row+1,col),(row+1,col+1)]
        for step in surroundSquares:
            if (self.chessboard.checkIJInSquare(step[0],step[1]) and self.chessboard.getSquare(step[0],step[1]).Piece.type == type.Empty):
                self.possibleWalks.append(self.chessboard.getSquare(step[0],step[1]))
        self.findCastlingMoves(firstSquare)
        return self.possibleWalks

    def findAllPossibleEats(self,firstSquare):
        self.possibleEats.clear() # clear the results before evaluating
        (row, col) = self.chessboard.findIJSquare(firstSquare)
        surroundSquares = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col),
                           (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        for step in surroundSquares:
            if (self.chessboard.checkIJInSquare(step[0], step[1]) and
                    self.chessboard.getSquare(step[0], step[1]).Piece.type != type.Empty and
                    self.chessboard.getSquare(step[0],step[1]).Piece.side != firstSquare.Piece.side):
                self.possibleEats.append(self.chessboard.getSquare(step[0], step[1]))
        return self.possibleEats

    def findCastlingMoves(self,firstSquare):
        """ This function detect for Castling moves when clicking the king(in firstSquare) """
        currSide = firstSquare.Piece.side
        whiteSideRightSquares = [self.chessboard.getSquare(7,5),self.chessboard.getSquare(7,6)]
        whiteSideLeftSquares = [self.chessboard.getSquare(7,1),self.chessboard.getSquare(7,2), self.chessboard.getSquare(7,3)]
        blackSideRightSquares = [self.chessboard.getSquare(0,1),self.chessboard.getSquare(0,2), self.chessboard.getSquare(0,3)]
        blacksideLeftSquares = [self.chessboard.getSquare(0,5), self.chessboard.getSquare(0,6)]
        if(currSide == side.whiteside and not self.chessboard.evaluateCheckEngine.checkCheck(side.whiteside)):
            if (self.chessboard.WhiteKingCastlingHandler.determineRightCastlingFromMovesAndNotCheck()):
                if (whiteSideRightSquares[0].Piece.type == type.Empty and
                        whiteSideRightSquares[1].Piece.type == type.Empty and
                        self.chessboard.WhiteKingCastlingHandler.determineCastlingFromCheck(whiteSideRightSquares)):
                    for square in whiteSideRightSquares:
                        self.possibleWalks.append(square)
                    print("white can right castling")
            if (self.chessboard.WhiteKingCastlingHandler.determineLeftCastlingFromMovesAndNotCheck()):
                if (whiteSideLeftSquares[0].Piece.type == type.Empty and
                        whiteSideLeftSquares[1].Piece.type == type.Empty and
                        whiteSideLeftSquares[2].Piece.type == type.Empty and
                        self.chessboard.WhiteKingCastlingHandler.determineCastlingFromCheck(whiteSideLeftSquares)):
                    for square in whiteSideLeftSquares[1:3]:
                        self.possibleWalks.append(square)
                    print("white can left castling")
        if(currSide == side.blackside and not self.chessboard.evaluateCheckEngine.checkCheck(side.blackside)):
            if (self.chessboard.BlackKingCastlingHandler.determineRightCastlingFromMovesAndNotCheck()):
                if (blackSideRightSquares[0].Piece.type == type.Empty and
                        blackSideRightSquares[1].Piece.type == type.Empty and
                        blackSideRightSquares[2].Piece.type == type.Empty and
                        self.chessboard.BlackKingCastlingHandler.determineCastlingFromCheck(blackSideRightSquares)):
                    for square in blackSideRightSquares[1:3]:
                        self.possibleWalks.append(square)
                    print("black can right castling")
            if (self.chessboard.BlackKingCastlingHandler.determineLeftCastlingFromMovesAndNotCheck()):
                if (blacksideLeftSquares[0].Piece.type == type.Empty and
                        blacksideLeftSquares[1].Piece.type == type.Empty and
                        self.chessboard.BlackKingCastlingHandler.determineCastlingFromCheck(blacksideLeftSquares)):
                    for square in blacksideLeftSquares:
                        self.possibleWalks.append(square)
                    print("black can left castling")

class CastlingMovesHandler:
    def __init__(self,side,chessboard):
        self.side = side
        self.chessboard = chessboard
        self.KingMove = False
        self.RookRightMove = False
        self.RookLeftMove = False

    def determineRightCastlingFromMovesAndNotCheck(self):
        return not (self.KingMove or self.RookRightMove)

    def determineLeftCastlingFromMovesAndNotCheck(self):
        return not (self.KingMove or self.RookLeftMove)

    def determineMoveEffectOnCastling(self,firstSquare):
        if (self.side == side.blackside):
            if (firstSquare.Piece.type == type.RookB and (not self.RookLeftMove or not self.RookRightMove)):
                if(self.chessboard.findIJSquare(firstSquare) == (0,0)):
                    self.RookRightMove = True
                    print("black right rook moves")
                if(self.chessboard.findIJSquare(firstSquare) == (0,7)):
                    self.RookLeftMove = True
                    print("black left rook moves")
            if (firstSquare.Piece.type == type.KingB and not self.KingMove):
                self.KingMove = True
                print("black king moves")
        if (self.side == side.whiteside):
            if(firstSquare.Piece.type == type.RookW and (not self.RookLeftMove or not self.RookRightMove)):
                if(self.chessboard.findIJSquare(firstSquare) == (7,7)):
                    self.RookRightMove = True
                    print("white right rook moves")
                if(self.chessboard.findIJSquare(firstSquare) == (7,0)):
                    self.RookLeftMove = True
                    print("white left rook moves")
            if (firstSquare.Piece.type == type.KingW and not self.KingMove):
                self.KingMove = True
                print("white king moves")
    def determineCastlingFromCheck(self,passSquares):
        for aSquare in passSquares:
            if(self.chessboard.evaluateCheckEngine.detectPassSquareEaten(self.side,aSquare)):
                return False
        return True
