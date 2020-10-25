from Button import button
from Color import vegasgold, gold



def drawBackButton(screen,Width,Height,ChessBoard):
    button(screen, "Back", Width // 2 - 450, Height // 2 + 50, 150, 40, vegasgold, gold,ChessBoard.reverseMoves)
