import pygame
import pygame_gui
import sys
import string

from Circle import Circle
from Constants import Constants
from Line import Line
from Point import Point


class PointNamer:
    def __init__(self):
        self.single_letter = list(map(str, list(string.ascii_uppercase)))
        print(self.single_letter)
        self.two_letter = [a + b for a in self.single_letter for b in self.single_letter]
        print(self.two_letter)

    def get_name(self):
        if len(self.single_letter) > 0:
            return self.single_letter.pop(0)
        assert (len(self.two_letter) > 0)
        return self.two_letter.pop(0)


def redraw_everything(screen, points):
    for point in points:
        point.draw(screen)

    for point in points:
        for point2 in points:
            line = Line(point, point2)
            line.draw(screen)

    for point1 in points:
        for point2 in points:
            for point3 in points:
                if point1 != point2 and point1 != point3 and point2 != point3:
                    circle = Circle(point1, point2, point3)
                    circle.draw(screen)

    pygame.display.update()


def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    screen.fill((255, 255, 255))  # White
    pygame.display.update()
    pygame.display.set_caption("Complex Geometry Solver")

    manager = pygame_gui.UIManager((800, 600))
    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text='Say Hello',
                                                manager=manager)
    point_namer = PointNamer()
    points = []
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = pygame.mouse.get_pos()
                    points.append(Point(x, y, point_namer))
                    # Only redrawing when necessary
                    redraw_everything(screen, points)

    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
