
"""sprites.py"""

import pygame
from config import PLAYER_X, PLAYER_Y, PLAYER_SPEED, PLAYER_SCALE

class Player(pygame.sprite.Sprite):

    """this class handles the player logic"""

    def __init__(self):

        """initalisation function for the Player class"""

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([10 * PLAYER_SCALE, 10 * PLAYER_SCALE])
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = PLAYER_X
        self.rect.y = PLAYER_Y
        self.jumping = False
        self.delta_x = 0
        self.delta_y = 0
        self.movement_y = 0
        self.movement_x = 0
        self.mouse_pos = 0

        pygame.draw.rect(self.image,
                         (200, 200, 200),
                         pygame.Rect(0, 0, 16 * PLAYER_SCALE, 32 * PLAYER_SCALE))

    def movement(self):

        """controls movement logic"""

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_SPACE]:
            self.jumping = True
            self.mouse_pos = pygame.mouse.get_pos()

    def jump(self):

        """within this function a formula will be expressed for the jump mechanics"""

        if self.jumping:

            self.delta_x = self.rect.x - self.mouse_pos[0]
            self.delta_y = self.rect.y - self.mouse_pos[1]

            self.movement_y = ((self.delta_x / self.delta_y) * self.delta_x) / 200000
            self.movement_x = self.rect.x - self.delta_x

            self.rect.y += self.movement_y
            self.rect.x += self.movement_x

    def update(self):

        """updates the player logic"""

        self.movement()
        self.jump()
