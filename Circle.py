import pygame


class Circle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def __get_points(self):
        x1, y1 = self.point1.get_coords()
        x2, y2 = self.point2.get_coords()
        x3, y3 = self.point3.get_coords()
        return x1, y1, x2, y2, x3, y3

    def __triangle_area(self):
        x1, y1, x2, y2, x3, y3 = self.__get_points()
        return abs(2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

    def draw(self, screen):
        x1, y1, x2, y2, x3, y3 = self.__get_points()

        d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        ux = ((x1 ** 2 + y1 ** 2) * (y2 - y3) + (x2 ** 2 + y2 ** 2) * (y3 - y1) + (x3 ** 2 + y3 ** 2) * (y1 - y2)) / d
        uy = ((x1 ** 2 + y1 ** 2) * (x3 - x2) + (x2 ** 2 + y2 ** 2) * (x1 - x3) + (x3 ** 2 + y3 ** 2) * (x2 - x1)) / d

        r = ((x1 - ux) ** 2 + (y1 - uy) ** 2) ** 0.5
        pygame.draw.circle(screen, (0, 0, 0), (ux, uy), r, 1)
        # return (Ux, Uy), R
