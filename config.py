
"""config.py"""

import pygame

pygame.init()

# Screen variables

SCREEN = pygame.display.get_desktop_sizes()
WIDTH = SCREEN[0][0]
HEIGHT = SCREEN[0][1]
FRAMERATE = 60

# Player variables

PLAYER_X = WIDTH // 2
PLAYER_Y = HEIGHT * 0.8
PLAYER_SCALE = 0.5
PLAYER_SPEED = 1

# Map variables

MAP_SCALE = 1

# Font

FONT = pygame.font.Font('font.ttf', 30)
