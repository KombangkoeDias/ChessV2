
class Moves:
    def __init__(self,firstSquare, firstPiece, secondSquare, secondPiece, enPassant,castling):
        self.firstSquare = firstSquare
        self.firstPiece = firstPiece
        self.secondSquare = secondSquare
        self.secondPiece = secondPiece
        self.enPassant = enPassant
        self.castling = castling
        # somehow the real square is in lastMove.firstSquare[0] and lastMove.firstSquare is a tuple of one element
        # and the same for these two but not for piece 2 ??? how strange is that
    def getFirstSquare(self):
        return self.firstSquare
    def getSecondSquare(self):
        return self.secondSquare
    def getFirstPiece(self):
        return self.firstPiece
    def getSecondPiece(self):
        return self.secondPiece
    def getCastling(self):
        return self.castling