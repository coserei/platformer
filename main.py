
"""main.py"""

import sys
import pygame
from config import PLAYER_SCALE, MAP_SCALE, WIDTH, HEIGHT, FRAMERATE, FONT
from player import Player

class Game:

    """the main class which the game runs upon"""

    def __init__(self):

        """initalization function for the Game class"""

        self.player_scale = PLAYER_SCALE
        self.map_scale = MAP_SCALE
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.fps = 0
        self.fps_text = 0

    def update(self):

        """function for updating game logic"""

        self.framerate_counter()
        self.render()

    def render(self):

        """function that handles the rendering of game objects"""

        self.display.fill((0,0,0))
        self.display.blit(self.fps_text, (10,10))

        player_list.update()
        player_list.draw(self.display)

    def framerate_counter(self):

        """handles the framerate counter object"""

        self.fps = str(round(self.clock.get_fps()))
        self.fps_text = FONT.render("FPS: " + self.fps, 1, (255, 255, 255))

    def main(self):

        """function which forms the main loop for all functions within the Game class"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        self.update()

        pygame.display.flip()
        self.clock.tick(FRAMERATE)


GAME = Game()
PLAYER = Player()

player_list = pygame.sprite.Group()
player_list.add(PLAYER)

while True:
    GAME.main()
