from side import side
from type import type
from ChessPiece import ChessPieces
from Square import Square
from Color import white,darkgreen
class PromotionHandler:
    #TODO adjust the promotion handler class
    def __init__(self,chessboard,screen):
        self.chessboard = chessboard
        self.myfirstSquare = None
        self.mysecondSquare = None
        self.mythirdSquare = None
        self.myfourthSquare = None
        self.promotionSquares = [self.myfirstSquare,self.mysecondSquare,self.mythirdSquare,self.myfourthSquare]
        self.choosePromotionSquare = None
        self.putInSquare = None
        self.screen = screen
    def determinePromotionSquares(self,side):
        if (side == side.whiteside):
            self.myfirstSquare = Square(900,20,70,70,white)
            self.mysecondSquare = Square(900,90,70,70,white)
            self.mythirdSquare = Square(900,160,70,70,white)
            self.myfourthSquare = Square(900,230,70,70,white)

            self.promotionSquares = [self.myfirstSquare, self.mysecondSquare, self.mythirdSquare, self.myfourthSquare]
        if (side == side.blackside):
            self.myfirstSquare = Square(900, 20, 70, 70, darkgreen )
            self.mysecondSquare = Square(900, 90, 70, 70, darkgreen)
            self.mythirdSquare = Square(900, 160, 70, 70, darkgreen)
            self.myfourthSquare = Square(900, 230, 70, 70, darkgreen)

            self.promotionSquares = [self.myfirstSquare, self.mysecondSquare, self.mythirdSquare, self.myfourthSquare]

    def drawChooose(self,side):
        if(side == side.whiteside):
            Queen = ChessPieces('Assets\Pieces\whiteQueen.png', (910, 30), type.QueenW, 0, side.whiteside)
            Rook = ChessPieces('Assets\Pieces\whiteRook.png', (910, 100), type.RookW, 0, side.whiteside)
            Bishop = ChessPieces('Assets\Pieces\whiteBishop.png', (910, 170), type.BishopW, 0, side.whiteside)
            Knight = ChessPieces('Assets\Pieces\whiteKnight.png', (910, 240), type.KnightW, 0, side.whiteside)
        if(side == side.blackside):
            Queen = ChessPieces('Assets\Pieces/blackQueen.png', (910, 30), type.QueenB, 0, side.blackside)
            Rook = ChessPieces('Assets\Pieces/blackRook.png', (910, 100), type.RookB, 0, side.blackside)
            Bishop = ChessPieces('Assets\Pieces/blackBishop.png', (910, 170), type.BishopB, 0, side.blackside)
            Knight = ChessPieces('Assets\Pieces/blackKnight.png', (910, 240), type.KnightB, 0, side.blackside)

        self.myfirstSquare.addPieces(Queen)
        self.mysecondSquare.addPieces(Rook)
        self.mythirdSquare.addPieces(Bishop)
        self.myfourthSquare.addPieces(Knight)
        self.myfirstSquare.drawSquare(self.screen, select=False, eat=False, check=False)
        self.mysecondSquare.drawSquare(self.screen, select=False, eat=False, check=False)
        self.mythirdSquare.drawSquare(self.screen, select=False, eat=False, check=False)
        self.myfourthSquare.drawSquare(self.screen, select=False, eat=False, check=False)
        self.screen.blit(Knight.image, Knight.rect)
        self.screen.blit(Bishop.image, Bishop.rect)
        self.screen.blit(Rook.image, Rook.rect)
        self.screen.blit(Queen.image, Queen.rect)

    def detectClick(self):
        for square in self.promotionSquares:
            if(square.getclick()):
                self.choosePromotionSquare = square

    def findPromotionSquare(self):
        promotion = False
        i = 0
        for j in range(8):
            if (self.chessboard.getSquare(i, j).Piece.type == type.PawnW):
                self.chessboard.promotion = side.whiteside
                self.chessboard.boardActive = False
                self.putInSquare = self.chessboard.getSquare(i,j)
                promotion = True
                print("promotion white")
                break

        i = 7
        for j in range(8):
            if (self.chessboard.getSquare(i, j).Piece.type == type.PawnB):
                self.chessboard.promotion = side.blackside
                self.chessboard.boardActive = False
                self.putInSquare = self.chessboard.getSquare(i, j)
                promotion = True
                print("promotion black")
                break
        if (not promotion):
            self.chessboard.promotion = False
            self.putInSquare = None


