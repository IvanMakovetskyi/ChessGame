# Interface for the game
import pygame
from chessgame.constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK
class Interface:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Chess Game")
        pygame.display.set_icon(pygame.image.load("chessgame/ui/resources/icon.png"))
        self.buttons = []
        self.hoverTile = None
        

    #TODO: Implement draw logic
    def draw(self):
        self.screen.fill(WHITE)
        pygame.display.flip()
