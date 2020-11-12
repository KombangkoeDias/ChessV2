import pygame
from ChessBoard import Board
from DrawButtons import drawBackButton
pygame.init() # initiate the pygame library

# screen width and height
Width = 1000
Height = 600

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Chess Game')
clock = pygame.time.Clock()

def start_game():

    gamePlay: bool = True
    print("Starting the game now!")

    ChessBoard = Board(screen)


    while gamePlay:

        ChessBoard.detectClick()
        ChessBoard.drawBoardAndPieces()
        drawBackButton(screen,Width,Height,ChessBoard)
        pygame.display.update()  # update the screen every cycle for hover effects on button.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

start_game()