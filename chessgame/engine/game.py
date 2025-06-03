# Game logic for chess
import pygame
from ..ui.interface import Interface

# ChessGame class to manage the game state
class ChessGame:
    def __init__(self):
        # TODO: Implement board, gameState and Interface
        #self.board = Board()
        #self.gameState = GameState()
        self.board = 0
        self.gameState = 0
        self.ui = Interface()
        self.running = True
        self.turn = "White"

    def run(self):
        while self.running:
            self.update()
            self.draw()
            self.handleEvent()
            
    def update(self):
        # TODO: Implement update logic
        pass

    def draw(self):
        # TODO: Implement drawing logic
        self.ui.draw()
        pass

    def handleEvent(self):
        # TODO: Implement event handling logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        pass

#Main function to run the game
if __name__ == "__main__":
    game = ChessGame()
    game.run()
    print("Game started")
