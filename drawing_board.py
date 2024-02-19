import pygame
import sys
import string

from gui.control_panel.button import Button
from gui.drawing_plane.point_namer import PointNamer
from gui.gui import Gui
from gui.gui_constants import GuiConstants
from gui.drawing_plane.drawing_state import DrawingState


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
    drawing_state.redraw_everything(screen)


def main():
    gui = Gui()

    point_namer = PointNamer()
    drawing_state = DrawingState(point_namer)

    buttons = [Button("Point", (10, 10), (70, 40), button_function=lambda: set_mode_to_point(drawing_state)),
               Button("Line", (80, 10), (150, 40), button_function=lambda: set_mode_to_line(drawing_state)),
               Button("Circle", (160, 10), (230, 40), button_function=lambda: set_mode_to_circle(drawing_state))]

    gui.redraw_screen(buttons, drawing_state)
    running = True
    while running:
        for event in pygame.event.get():
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
                        gui.redraw_screen(buttons, drawing_state)
                        # only redrawing everything when there is event
        pygame.display.update()

    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
