import pygame
from Color import lightSquare,darkSquare,green
from type import type
from side import side
from Square import Square
from ChessPiece import ChessPieces
from EvaluateMovesEngine import EvaluateMovesEngine
from Moves import Moves

class Board:
    def __init__(self,screen):
        """ initialize the ChessBoard """
        self.Squarelist = None # Squarelist will hold the list of rows of Squares.
        self.clicklist = list() # clicklist will hold the chosen Square and Destination Square.
        self.screen = screen # the screen passed from UI.py
        self.InitializeBoard() # call to set up the board
        self.evaluateMovesEngine = EvaluateMovesEngine(self)
        self.possibleWalks = list()
        self.possibleEats = list()
        self.moves = list()

    def InitializeBoard(self):
        """ return the initialized board as SquareList"""
        self.Squarelist = list() # make it a list
        for i in range(8):
            mylist = list()
            self.Squarelist.append(mylist)  # create rows
        for i in range(8):
            for j in range(8):
                if ((i + j) % 2 == 0): # we need to do this to add color to be like chess board.
                    newSquare = Square(220 + 70 * j, 30 + 70 * i, 70, 70, lightSquare)  # the location of each of the square.
                    piecelocation = (newSquare.x + 10, newSquare.y + 10)  # the location of each piece.
                    # add empty to every square first.
                    newSquare.addPieces(ChessPieces('Assets\Pieces\empty.png', piecelocation, type.Empty, None, side.noside))
                    # then change it if it's the case.
                    if (i == 1):
                        newSquare.addPieces(
                            ChessPieces('Assets/Pieces/blackPawn.png', piecelocation, type.PawnB, j, side.blackside))
                    if (i == 0):
                        if (j == 0):
                            newSquare.addPieces(
                                ChessPieces('Assets/Pieces/blackRook.png', piecelocation, type.RookB, 0, side.blackside))
                        if (j == 2):
                            newSquare.addPieces(
                                ChessPieces('Assets/Pieces/blackBishop.png', piecelocation, type.BishopB, 0, side.blackside))
                        if (j == 4):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces/blackKing.png', piecelocation, type.KingB, 0, side.blackside))
                        if (j == 6):
                            newSquare.addPieces(
                                ChessPieces('Assets/Pieces/blackKnight.png', piecelocation, type.KnightB, 1, side.blackside))
                    if (i == 6):
                        newSquare.addPieces(
                            ChessPieces('Assets\Pieces\whitePawn.png', piecelocation, type.PawnW, j, side.whiteside))
                    if (i == 7):
                        if (j == 1):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteKnight.png', piecelocation, type.KnightW, 0, side.whiteside))
                        if (j == 3):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteQueen.png', piecelocation, type.QueenW, 0, side.whiteside))
                        if (j == 5):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteBishop.png', piecelocation, type.BishopW, 1, side.whiteside))
                        if (j == 7):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteRook.png', piecelocation, type.RookW, 1, side.whiteside))
                    self.Squarelist[i].append(newSquare)
                else:
                    # the same just another half.
                    newSquare = Square(220 + 70 * j, 30 + 70 * i, 70, 70, darkSquare)
                    piecelocation = (newSquare.x + 10, newSquare.y + 10)
                    newSquare.addPieces(ChessPieces('Assets\Pieces\empty.png', piecelocation, type.Empty, None, side.noside))
                    if (i == 1):
                        newSquare.addPieces(
                            ChessPieces('Assets/Pieces/blackPawn.png', piecelocation, type.PawnB, j, side.blackside))
                    if (i == 0):
                        if (j == 1):
                            newSquare.addPieces(
                                ChessPieces('Assets/Pieces/blackKnight.png', piecelocation, type.KnightB, 0, side.blackside))
                        if (j == 3):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces/blackQueen.png', piecelocation, type.QueenB, 0, side.blackside))
                        if (j == 5):
                            newSquare.addPieces(
                                ChessPieces('Assets/Pieces/blackBishop.png', piecelocation, type.BishopB, 1, side.blackside))
                        if (j == 7):
                            newSquare.addPieces(
                                ChessPieces('Assets/Pieces/blackRook.png', piecelocation, type.RookB, 1, side.blackside))
                    if (i == 6):
                        newSquare.addPieces(
                            ChessPieces('Assets\Pieces\whitePawn.png', piecelocation, type.PawnW, j, side.whiteside))
                    if (i == 7):
                        if (j == 0):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteRook.png', piecelocation, type.RookW, 0, side.whiteside))
                        if (j == 2):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteBishop.png', piecelocation, type.BishopW, 0, side.whiteside))
                        if (j == 4):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteKing.png', piecelocation, type.KingW, 0, side.whiteside))
                        if (j == 6):
                            newSquare.addPieces(
                                ChessPieces('Assets\Pieces\whiteKnight.png', piecelocation, type.KnightW, 1, side.whiteside))
                    self.Squarelist[i].append(newSquare)

    def drawBoardAndPieces(self):
        """ draw board and piece when things changes, ( draw squares according to the Squares in Square list, and draw piece
        according to the piece location and image file in Square list)
        """
        for i in range(8):
            for j in range(8):
                if (len(self.clicklist) > 0 and (i,j) == self.findIJSquare(self.clicklist[0])):
                    self.getSquare(i, j).drawSquare(self.screen,True)
                else:
                    self.getSquare(i,j).drawSquare(self.screen,False)
                if (self.getSquare(i,j).Piece.type != type.Empty):
                    self.getSquare(i,j).Piece.drawPieces(self.screen,self.getSquare(i,j))
        for walkSquare in self.possibleWalks:
            pygame.draw.circle(self.screen, green, (walkSquare.x + 35, walkSquare.y + 35), 7)
    def getSquare(self,i,j):
        """ return squares at position (i,j) """
        return self.Squarelist[i][j]

    def detectClick(self):
        """ detect the click in all the squares on the board and append the clicked square to the click list """
        for i in range(8):
            for j in range(8):
                if (self.getSquare(i,j).getclick()):
                    if (len(self.clicklist) == 0 and self.getSquare(i,j).Piece.type != type.Empty):
                        self.clicklist.append(self.getSquare(i, j))
                        self.possibleWalks = self.evaluateMovesEngine.getPossibleWalks(self.getSquare(i,j))

                    if (len(self.clicklist) == 1):
                        if (self.getSquare(i,j).Piece.side != self.clicklist[0].Piece.side):
                            if (self.evaluateMovesEngine.evaluateMove(self.clicklist[0], self.getSquare(i,j))):
                                self.clicklist.append(self.getSquare(i,j))
                                # clear these two lists(walklist,eatlist) before move for aesthetic effect
                                self.possibleWalks.clear()  # after a move we clear the walklist
                                self.possibleEats.clear()  # same
                                self.walkOrEat()
                                self.clicklist.clear()


                        else:
                            self.clicklist.clear()
                            self.clicklist.append(self.getSquare(i,j))
                            self.possibleWalks.clear() # change chosen square we clear the walklist as well
                            self.possibleWalks = self.evaluateMovesEngine.getPossibleWalks(self.getSquare(i, j)) # and recalculate

    def walkOrEat(self):
        square1 = self.clicklist[0]
        square2 = self.clicklist[1]
        piece1 = square1.Piece
        piece2 = square2.Piece
        location1 = piece1.getlocation()
        location2 = piece2.getlocation()
        if (square1.Piece.type != square2.Piece.type and square1.Piece.type != type.Empty and square2.Piece.type != type.Empty):
            print(square1.Piece.type.value, "eat", square2.Piece.type.value, "at", self.toNotation(self.findIJSquare(square2)))
        else:
            print(square1.Piece.type.value, "to", self.toNotation(self.findIJSquare(square2)))
        move = Moves(square1, piece1, square2, piece2)
        self.moves.append(move) # add the move to moves list

        self.doAnimation(location1,location2,square1,square2,piece1) # doAnimation function gradually updates location of piece1

        (i,j) = self.findIJSquare(square1)
        self.getSquare(i,j).addPieces(ChessPieces('Assets\Pieces\empty.png', location1, type.Empty, None, side.noside))
        (i,j) = self.findIJSquare(square2)
        self.getSquare(i,j).addPieces(piece1)

    def findIJSquare(self,aSquare):
        for i in range(8):
            for j in range(8):
                if(self.getSquare(i,j) == aSquare):
                    return (i,j)
        return False

    def doAnimation(self,firstlocation,secondlocation,square1,square2,myPiece):
        firstx = firstlocation[0]
        firsty = firstlocation[1]
        secondx = secondlocation[0]
        secondy = secondlocation[1]
        (firsti,firstj) = self.findIJSquare(square1)
        (secondi,secondj) = self.findIJSquare(square2)
        differencex = (secondj - firstj) * 70
        differencey = (secondi - firsti) * 70



        for i in range(70):
            movementx = differencex / 70 * i
            movementy = differencey / 70 * i
            pygame.time.delay(1)
            myPiece.addlocation((firstx + movementx, firsty + movementy))
            self.drawBoardAndPieces()
            if i == 30:
                moveSound = pygame.mixer.Sound('Assets/Sounds/moveSound.wav')
                moveSound.play()
            self.screen.blit(myPiece.image, (firstx + movementx, firsty + movementy))
            pygame.display.update()

    def toNotation(self,pos):
        alphabetlist = ['A','B','C','D','E','F','G','H']
        return alphabetlist[pos[1]]+str(abs(pos[0]-8))

    def reverseMoves(self):
        if(len(self.moves) > 0):
            # clear these three lists whenever going back
            self.clicklist.clear()
            self.possibleWalks.clear()
            self.possibleEats.clear()

            lastMove = self.moves[-1]
            square1 = lastMove.firstSquare
            square2 = lastMove.secondSquare
            piece1 = lastMove.firstPiece
            piece2 = lastMove.secondPiece
            square1 = square1[0] # somehow the real square is in lastMove.firstSquare[0] and lastMove.firstSquare is a tuple of one element
            square2 = square2[0] # and the same for these two but not for piece 2 ??? how strange is that
            piece1 = piece1[0]
            location1 = square1.piecelocation
            location2 = square2.piecelocation

            self.doAnimation(location2,location1,square2,square1,piece1)

            square1.addPieces(piece1)
            square2.addPieces(piece2)
            self.moves.pop(-1)
