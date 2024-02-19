import pygame

from gui.gui_constants import Constants


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __find_infinite_line(self):
        a, b = self.point1.get_coords(), self.point2.get_coords()
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        return ((a[0] + Constants.SCREEN_WIDTH * dx, a[1] + Constants.SCREEN_WIDTH * dy),
                (a[0] - Constants.SCREEN_HEIGHT * dx, a[1] - Constants.SCREEN_HEIGHT * dy))

    def draw(self, screen):
        # pygame.draw.line(screen, (0, 0, 0), self.point1.get_coords(), self.point2.get_coords())
        coords1, coord2 = self.__find_infinite_line()
        pygame.draw.line(screen, (0, 0, 0), coords1, coord2)
