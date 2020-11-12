
class DrawHandler:
    def __init__(self,chessboard):
        self.chessboard = chessboard
        self.stalemate = False
        self.deadPosition = False
        self.mutualAgree = False # will not be implemented here
        self.fiftyMoves = False
        self.threeFoldRepetition = False

    def determineStaleMate(self):
        #TODO implement stalemate detection
        pass

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