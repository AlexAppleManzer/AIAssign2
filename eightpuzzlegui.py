
import pygame


class EightPuzzleGUI:

    def __init__(self):
        pygame.init()
        size = 320, 240
        black = 0, 0, 0

        screen = pygame.display.set_mode(size)
        screen.fill(black)
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()


