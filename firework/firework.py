import pygame
import numpy as np

from rocket import Rocket


class Firework():
    #
    #
    #  -------- Init -----------
    #
    def __init__(self, config: dict):
        super().__init__()

        # save config
        self.config = config

        # save rocket container
        self.rockets: list = []

        # initiate pygame
        pygame.init()

        # add screen title
        pygame.display.set_caption(self.config.get('title'))

        # initiate & save screen
        self.screen = pygame.display.set_mode(self.config.get('screenSize'))

        # initiate & configure background
        self.background = pygame.Surface(self.config.get('screenSize'))
        self.background.set_alpha(64)
        self.background.fill((0, 0, 0))

        # initiate & save game clock
        self.clock = pygame.time.Clock()

        # start firework
        self.run()

    #
    #
    # -------- Game Loop -----------
    #
    def run(self):
        while True:

            # --- Main event loop
            for event in pygame.event.get():

                # --- handle window close
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # --- Remove not visible rockets
            for rocket in self.rockets:
                if (not rocket.inBound()):
                    self.rockets.remove(rocket)

            # --- Add new rocket over time
            if (len(self.rockets) < self.config.get('count')):
                self.rockets.append(Rocket(**self.config.get('rocket')))

            self.updateScreen()

    #
    #
    # -------- updateScreen -----------
    #
    def updateScreen(self):

        # --- Screen-clearing
        self.screen.blit(self.background, (0, 0))

        # --- Draw rockets
        for rocket in self.rockets:
            rocket.applyForce(np.array(self.config.get('force')))
            rocket.update()
            rocket.draw()

        # --- Update the screen
        pygame.display.flip()

        # --- Update clock with game fps
        self.clock.tick(self.config.get('fps'))
