import pygame
import sys

from gui.gui import Gui


def main():
    gui = Gui()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = pygame.mouse.get_pos()
                    gui.process_click(x, y)
        pygame.display.update()

    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
