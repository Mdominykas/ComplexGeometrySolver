import pygame
import pygame_gui
import sys
import string

from Button import Button
from Circle import Circle
from Constants import Constants
from DrawingState import DrawingState
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


def set_mode_to_point(drawing_state):
    drawing_state.mode = DrawingState.POINT_MODE


def set_mode_to_line(drawing_state):
    drawing_state.mode = DrawingState.LINE_MODE


def set_mode_to_circle(drawing_state):
    drawing_state.mode = DrawingState.CIRCLE_MODE


def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    screen.fill((255, 255, 255))  # White
    pygame.display.update()
    pygame.display.set_caption("Complex Geometry Solver")

    drawing_state = DrawingState()

    buttons = [Button("Point", (10, 10), (70, 40), button_function=lambda: set_mode_to_point(drawing_state)),
               Button("Line", (80, 10), (150, 40), button_function=lambda: set_mode_to_line(drawing_state)),
               Button("Circle", (160, 10), (230, 40), button_function=lambda: set_mode_to_circle(drawing_state))]

    point_namer = PointNamer()
    points = []
    clock = pygame.time.Clock()
    running = True
    while running:
        for button in buttons:
            button.draw(screen)
        for event in pygame.event.get():
            # print("event = ", event)
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = pygame.mouse.get_pos()
                    was_button_click = False
                    for button in buttons:
                        if button.is_clicked(x, y):
                            print("Button was clicked")
                            button.perform_actions()
                            was_button_click = True

                    if not was_button_click:
                        points.append(Point(x, y, point_namer))
                        redraw_everything(screen, points)
        pygame.display.update()

    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
