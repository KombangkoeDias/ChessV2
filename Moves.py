
class Moves:
    def __init__(self,firstSquare, firstPiece, secondSquare, secondPiece, enPassant):
        self.firstSquare = firstSquare,
        self.firstPiece = firstPiece,
        self.secondSquare = secondSquare,
        self.secondPiece = secondPiece,
        self.enPassant = enPassant
        # somehow the real square is in lastMove.firstSquare[0] and lastMove.firstSquare is a tuple of one element
        # and the same for these two but not for piece 2 ??? how strange is that
    def getFirstSquare(self):
        return self.firstSquare[0]
    def getSecondSquare(self):
        return self.secondSquare[0]
    def getFirstPiece(self):
        return self.firstPiece[0]
    def getSecondPiece(self):
        return self.secondPiece[0]
