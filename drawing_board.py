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


def draw_text(screen, x, y, text):
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render(text, False, (0, 0, 0))
    screen.blit(text_surface, (x, y))


def redraw_everything(screen, drawing_state: DrawingState):
    for point in drawing_state.points:
        point.draw(screen)

    for line in drawing_state.lines:
        line.draw(screen)

    for circle in drawing_state.circles:
        circle.draw(screen)

    for (i, selected_point) in enumerate(drawing_state.selected_points):
        draw_text(screen, Constants.SELECTED_POINTS_X, Constants.SELECTED_POINTS_Y + i * Constants.SELECTED_POINTS_INC, selected_point.to_string())

    pygame.display.update()


def set_mode_to_point(drawing_state):
    drawing_state.change_mode(DrawingState.POINT_MODE)


def set_mode_to_line(drawing_state):
    drawing_state.change_mode(DrawingState.LINE_MODE)


def set_mode_to_circle(drawing_state):
    drawing_state.change_mode(DrawingState.CIRCLE_MODE)


def redraw_screen(screen, buttons, drawing_state):
    screen.fill((255, 255, 255))
    for button in buttons:
        button.draw(screen)
    redraw_everything(screen, drawing_state)


def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    pygame.display.update()
    pygame.display.set_caption("Complex Geometry Solver")

    point_namer = PointNamer()
    drawing_state = DrawingState(point_namer)

    buttons = [Button("Point", (10, 10), (70, 40), button_function=lambda: set_mode_to_point(drawing_state)),
               Button("Line", (80, 10), (150, 40), button_function=lambda: set_mode_to_line(drawing_state)),
               Button("Circle", (160, 10), (230, 40), button_function=lambda: set_mode_to_circle(drawing_state))]

    redraw_screen(screen, buttons, drawing_state)
    clock = pygame.time.Clock()
    running = True
    while running:
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
                        drawing_state.process_click(x, y)
                        redraw_screen(screen, buttons, drawing_state)
                        # only redrawing everything when there is event
        pygame.display.update()

    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
