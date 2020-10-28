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