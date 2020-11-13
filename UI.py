import pygame
from ChessBoard import Board
from DrawButtons import drawBackButton
from Background import BackgroundPhoto
pygame.init() # initiate the pygame library

# screen width and height
Width = 1000
Height = 600

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Chess Game')
clock = pygame.time.Clock()

def start_game():
    GameplayBackground = BackgroundPhoto('Assets\Background\Horses.jpg', [0, 0])
    gamePlay: bool = True
    print("Starting the game now!")

    ChessBoard = Board(screen)


    while gamePlay:
        screen.blit(GameplayBackground.image, GameplayBackground.rect)
        ChessBoard.detectClick()
        ChessBoard.drawBoardAndPieces()
        drawBackButton(screen,Width,Height,ChessBoard)
        ChessBoard.promotionHandler.findPromotionSquare()
        pygame.display.update()  # update the screen every cycle for hover effects on button.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

start_game()