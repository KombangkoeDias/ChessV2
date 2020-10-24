import pygame
from ChessPiece import ChessPieces
from type import type
from side import side
from Color import yellow,orange
class Square:
    def __init__(self,x,y,w,h,ic):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = ic
        self.chosen = False
        self.click = False
        self.Piece = ChessPieces('Assets\Pieces\empty.png', (0,0),type.Empty,None,side.noside)
    def choose(self):
        mouse = pygame.mouse.get_pos()
        if (self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y):
            self.chosen = True
            return True
        else:
            self.chosen = False
            return False
    def gethover(self):
        mouse = pygame.mouse.get_pos()
        if (self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y):
            return True
        return False
    def getclick(self):
        mouse = pygame.mouse.get_pos()
        if (self.x + self.w > mouse[0] > self.x and self.y + self.h > mouse[1] > self.y):
            if (pygame.mouse.get_pressed()[0] == 1):
                return True
            else:
                return False
    def addPieces(self,Piece):
        self.Piece = Piece

    def drawSquare(self,screen,select):
        if (select):
            pygame.draw.rect(screen,orange , (self.x, self.y, self.w, self.h))
        elif (self.gethover()):
            pygame.draw.rect(screen,yellow , (self.x, self.y, self.w, self.h))
        else:
            pygame.draw.rect(screen, self.color, (self.x,self.y,self.w,self.h))