import pygame
import numpy as np

from particle import Particle


class Rocket(Particle):

    #
    #
    #  -------- Init -----------
    #
    def __init__(
            self,
            size: int = 0,
            velocity: list = [[-0, 0], [-0, 0]],
            splitterNum: int = 0,
            splitterSize: int = 0,
            splitterVelocity: int = 0,
            splitterForce: list = [0.0, 0.0],
            splitterBrightness: list = [0, 255],
    ):

        screenSize: list = pygame.display.get_surface().get_size()

        super().__init__(
            position=[
                np.random.random_integers(0, high=screenSize[0]),
                np.random.random_integers(screenSize[1] - size * 16,
                                          high=screenSize[1] - size),
            ],
            size=size,
            velocity=[
                float(
                    np.random.random_integers(velocity[0][0],
                                              high=velocity[0][1])),
                float(
                    np.random.random_integers(velocity[1][0],
                                              high=velocity[1][1]))
            ],
        )

        self.splitterNum: int = splitterNum
        self.splitterSize: int = splitterSize
        self.splitterVelocity: int = splitterVelocity
        self.splitterForce: list = splitterForce
        self.splitterBrightness: int = splitterBrightness

        self.exploded: bool = False
        self.splitters: list = []

    #  -------- update -----------
    #
    def update(self) -> None:
        super().update()

        if (self.exploded):
            for s in self.splitters:
                s.applyForce(np.array(self.splitterForce))
                s.update()
                s.draw()

        if (self.vel[1] > -0.5 and not self.exploded):
            self.exploded = True
            self.explode()

    #  -------- explode -----------
    #
    def explode(self) -> None:

        color = pygame.Color(
            int(
                np.random.random_integers(self.splitterBrightness[0],
                                          high=self.splitterBrightness[1])),
            int(
                np.random.random_integers(self.splitterBrightness[0],
                                          high=self.splitterBrightness[1])),
            int(
                np.random.random_integers(self.splitterBrightness[0],
                                          high=self.splitterBrightness[1])),
        )

        for i in range(0, self.splitterNum):

            self.splitters.append(
                Particle(
                    position=self.center,
                    size=self.splitterSize,
                    velocity=[
                        float(
                            np.random.uniform(-1, 1) * self.splitterVelocity),
                        float(
                            np.random.uniform(-1, 1) * self.splitterVelocity)
                    ],
                    color=color,
                ))

    #  -------- draw -----------
    #
    def draw(self) -> None:
        if (not self.exploded):
            super().draw()
