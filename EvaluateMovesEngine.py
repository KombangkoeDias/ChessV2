from type import type

from MovesHandlers.PawnMovesHandler import PawnMovesHandler
from MovesHandlers.KnightMovesHandler import KnightMovesHandler
from MovesHandlers.BishopMovesHandler import BishopMovesHandler
from MovesHandlers.RookMovesHandler import RookMovesHandler
from MovesHandlers.QueenMovesHandler import QueenMovesHandler
from MovesHandlers.KingMovesHandler import KingMovesHandler

class EvaluateMovesEngine:
    def __init__(self, chessboard):
        self.chessboard = chessboard
        self.PawnMovesHandler = PawnMovesHandler(chessboard)
        self.KnightMovesHandler = KnightMovesHandler(chessboard)
        self.BishopMovesHandler = BishopMovesHandler(chessboard)
        self.RookMovesHandler = RookMovesHandler(chessboard)
        self.QueenMovesHandler = QueenMovesHandler(chessboard)
        self.KingMovesHandler = KingMovesHandler(chessboard)
        print("The Evaluate-moves engine is created")
    def evaluateMove(self,firstSquare,secondSquare):
        if (firstSquare.Piece.type == type.PawnW or firstSquare.Piece.type == type.PawnB):
            return self.PawnMovesHandler.evaluateMove(firstSquare,secondSquare)
        elif (firstSquare.Piece.type == type.KnightW or firstSquare.Piece.type == type.KnightB):
            return self.KnightMovesHandler.evaluateMove(firstSquare,secondSquare)
        elif (firstSquare.Piece.type == type.BishopW or firstSquare.Piece.type == type.BishopB):
            return self.BishopMovesHandler.evaluateMove(firstSquare,secondSquare)
        elif (firstSquare.Piece.type == type.RookW or firstSquare.Piece.type == type.RookB):
            return self.RookMovesHandler.evaluateMove(firstSquare,secondSquare)
        elif (firstSquare.Piece.type == type.QueenW or firstSquare.Piece.type == type.QueenB):
            return self.QueenMovesHandler.evaluateMove(firstSquare,secondSquare)
        elif (firstSquare.Piece.type == type.KingW or firstSquare.Piece.type == type.KingB):
            return self.KingMovesHandler.evaluateMove(firstSquare,secondSquare)
    def getPossibleWalks(self,firstSquare):
        if (firstSquare.Piece.type == type.PawnW or firstSquare.Piece.type == type.PawnB):
            return self.PawnMovesHandler.findAllPossibleWalks(firstSquare)
        elif (firstSquare.Piece.type == type.KnightW or firstSquare.Piece.type == type.KnightB):
            return self.KnightMovesHandler.findAllPossibleWalks(firstSquare)
        elif (firstSquare.Piece.type == type.BishopW or firstSquare.Piece.type == type.BishopB):
            return self.BishopMovesHandler.findAllPossibleWalks(firstSquare)
        elif (firstSquare.Piece.type == type.RookW or firstSquare.Piece.type == type.RookB):
            return self.RookMovesHandler.findAllPossibleWalks(firstSquare)
        elif (firstSquare.Piece.type == type.QueenW or firstSquare.Piece.type == type.QueenB):
            return self.QueenMovesHandler.findAllPossibleWalks(firstSquare)
        elif (firstSquare.Piece.type == type.KingW or firstSquare.Piece.type == type.KingB):
            return self.KingMovesHandler.findAllPossibleWalks(firstSquare)