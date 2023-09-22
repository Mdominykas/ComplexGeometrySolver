import pygame
import sys
import string


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


class Point:
    def __init__(self, x, y, namer):
        self.x = x
        self.y = y
        self.namer = namer
        self.name = namer.get_name()

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 5)

        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render(self.name, False, (0, 0, 0))
        screen.blit(text_surface, (self.x, self.y))

    def get_coords(self):
        return self.x, self.y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __find_infinite_line(self, infinity_constant=10000):
        a, b = self.point1.get_coords(), self.point2.get_coords()
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        return ((a[0] + infinity_constant * dx, a[1] + infinity_constant * dy),
                (a[0] - infinity_constant * dx, a[1] - infinity_constant * dy))

    def draw(self, screen):
        # pygame.draw.line(screen, (0, 0, 0), self.point1.get_coords(), self.point2.get_coords())
        coords1, coord2 = self.__find_infinite_line()
        pygame.draw.line(screen, (0, 0, 0), coords1, coord2)


def redraw_everything(screen, points):
    for point in points:
        point.draw(screen)

    for point in points:
        for point2 in points:
            line = Line(point, point2)
            line.draw(screen)
    # Update the display
    pygame.display.flip()


def main():
    pygame.init()
    pygame.font.init()

    # Constants
    screen_width, screen_height = 800, 600

    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255, 255, 255))  # White
    pygame.display.update()
    pygame.display.set_caption("Complex Geometry Solver")

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
