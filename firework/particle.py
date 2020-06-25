import pygame
import numpy as np


# default particle class (rect):
class Particle(pygame.Rect):

    #
    #
    #  -------- Init -----------
    #
    def __init__(
            self,
            position: list = [0, 0],
            size: int = 0,
            velocity: list = [0.0, 0.0],
            color=pygame.Color('WHITE'),
    ):

        super().__init__(position, [size, size])

        # get corresponding screen object
        self.screen = pygame.display.get_surface()
        self.bound = pygame.Rect((0, 0), self.screen.get_size())

        # physics representation: velocity, acceleration
        self.vel = np.array(velocity)
        self.acc = np.array([0.0, 0.0])

        # save color
        self.color = color

    #  -------- inBound -----------
    #
    def inBound(self) -> bool:

        # Rect.contains(Rect)
        # https://www.pygame.org/docs/ref/rect.html#pygame.Rect.contains
        if (self.bound.contains(self)):
            return True

        return False

    #  -------- collision -----------
    #
    def collision(self, particle) -> bool:

        # Rect.colliderect(Rect)
        # https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect
        if (self.colliderect(particle)):
            return True

        return False

    #  -------- draw -----------
    #
    def applyForce(self, force) -> None:
        self.acc += force

    #  -------- draw -----------
    #
    def update(self) -> None:
        self.vel += self.acc
        self.center += self.vel
        self.acc.dot(0)

    #  -------- draw -----------
    #
    def draw(self) -> None:

        # https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
        pygame.draw.circle(self.screen, self.color, self.center, self.width)
