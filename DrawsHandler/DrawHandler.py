from side import side

class DrawHandler:
    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.stalemate = False
        self.deadPosition = False
        self.mutualAgree = False # will not be implemented here
        self.fiftyMoves = False
        self.threeFoldRepetition = False

    def determineStaleMate(self,side):
        if (self.chessboard.evaluateCheckEngine.checkCheck(side)):
            return False
        for i in range(8):
            for j in range(8):
                currSquare = self.chessboard.getSquare(i,j)
                if(currSquare.Piece.side == side):
                    walkList = self.chessboard.evaluateMovesEngine.getFilteredPossibleWalks(currSquare)

                    if(len(walkList) > 0):
                        return False
                    else:
                        eatList = self.chessboard.evaluateMovesEngine.getFilteredPossibleEats(currSquare)
                        if(len(eatList) > 0):
                            return False
        return True

    def determineDeadPosition(self):
        # pretty hard to determine
        #TODO implement dead position detection
        pass

    def determinefiftyMoves(self):
        #TODO implement 50-Move Rule detection
        pass

    def determineThreeFoldRepetition(self):
        #TODO implement three fold repetition
        pass