from type import type

class PawnMovesHandler:
    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.possibleWalks = list()
        self.possibleEats = list()
    def evaluateMove(self,firstSquare,secondSquare):
        self.findAllPossibleWalks(firstSquare)
        self.findAllPossibleEats(firstSquare)
        if(secondSquare in self.possibleWalks or secondSquare in self.possibleEats):
            return True
        else:
            return False
    def findAllPossibleWalks(self,firstSquare):
        (row, col) = self.chessboard.findIJSquare(firstSquare)
        if (firstSquare.Piece.type == type.PawnW):
            one_step_square = self.chessboard.getSquare(row-1,col)
            two_step_square = self.chessboard.getSquare(row-2,col)
            if (row == 6):
                if (one_step_square.Piece.type == type.Empty):
                    self.possibleWalks.append(one_step_square)
                    if (two_step_square.Piece.type == type.Empty):
                        self.possibleWalks.append(two_step_square)
            else:
                if (one_step_square.Piece.type == type.Empty):
                    self.possibleWalks.append(one_step_square)
        if (firstSquare.Piece.type == type.PawnB):
            one_step_square = self.chessboard.getSquare(row + 1, col)
            two_step_square = self.chessboard.getSquare(row + 2, col)
            if (row == 1):
                if (one_step_square.Piece.type == type.Empty):
                    self.possibleWalks.append(one_step_square)
                    if (two_step_square.Piece.type == type.Empty):
                        self.possibleWalks.append(two_step_square)
            else:
                if (one_step_square.Piece.type == type.Empty):
                    self.possibleWalks.append(one_step_square)
        return self.possibleWalks
    def findAllPossibleEats(self,firstSquare):
        (firsti, firstj) = self.chessboard.findIJSquare(firstSquare)

