from type import type
from side import side

class PawnMovesHandler:
    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.possibleWalks = list()
        self.possibleEats = list()
    def findAllPossibleWalks(self,firstSquare):
        self.possibleWalks.clear()  # clear the list first
        (row, col) = self.chessboard.findIJSquare(firstSquare)
        if (firstSquare.Piece.type == type.PawnW): # for white
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

        if (firstSquare.Piece.type == type.PawnB): # for black
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
        self.possibleEats.clear()  # clear the list first
        (row, col) = self.chessboard.findIJSquare(firstSquare)
        if (firstSquare.Piece.type == type.PawnW): # for white
            if (self.chessboard.checkIJInSquare(row-1,col-1)): # check if it's in the square before creating
                left_eat_square = self.chessboard.getSquare(row-1,col-1)
                if (left_eat_square.Piece.side == side.blackside): # and if that square's piece is opponent's add it to eat list
                    self.possibleEats.append(left_eat_square)
            if (self.chessboard.checkIJInSquare(row-1,col+1)): # check if it's in the square before creating
                right_eat_square = self.chessboard.getSquare(row - 1, col + 1)
                if (right_eat_square.Piece.side == side.blackside): # and if that square's piece is opponent's add it to eat list
                    self.possibleEats.append(right_eat_square)
        if firstSquare.Piece.type == type.PawnB: # for black
            if (self.chessboard.checkIJInSquare(row+1,col-1)): # check if it's in the square before creating
                left_eat_square = self.chessboard.getSquare(row + 1, col - 1)
                if (left_eat_square.Piece.side == side.whiteside): # and if that square's piece is opponent's add it to eat list
                    self.possibleEats.append(left_eat_square)
            if (self.chessboard.checkIJInSquare(row+1,col+1)): # check if it's in the square before creating
                right_eat_square = self.chessboard.getSquare(row + 1, col + 1)
                if (right_eat_square.Piece.side == side.whiteside): # and if that square's piece is opponent's add it to eat list
                    self.possibleEats.append(right_eat_square)
        self.findEnPassant(firstSquare) # add more to possibleEats for En Passant
        return self.possibleEats
    def findEnPassant(self,firstSquare):
        # TODO creates En Passant function
        if (firstSquare.Piece.side == side.whiteside):
            if (self.chessboard.findIJSquare(firstSquare)[0] == 3):
                print("last move", self.chessboard.findIJSquare(self.chessboard.moves[-1].getFirstSquare()),"to",
                      self.chessboard.findIJSquare(self.chessboard.moves[-1].getSecondSquare()))
        else:
            if (self.chessboard.findIJSquare(firstSquare)[0] == 4):
                print("last move",self.chessboard.findIJSquare(self.chessboard.moves[-1].getFirstSquare()),"to",
                      self.chessboard.findIJSquare(self.chessboard.moves[-1].getSecondSquare()))
        pass



