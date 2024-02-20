import pygame

from gui.control_panel.control_panel import ControlPanel
from gui.drawing_plane.drawing_state import DrawingState
from gui.gui_constants import GuiConstants


class Gui:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((GuiConstants.SCREEN_WIDTH, GuiConstants.SCREEN_HEIGHT))
        pygame.display.set_caption("Complex Geometry Solver")

        self.drawing_state = DrawingState()

        # pygame.display.update()
        self.control_panel = ControlPanel(self.drawing_state)

        self.redraw_screen()

    def process_click(self, x, y):
        if self.control_panel.is_clicked(x, y):
            self.control_panel.process_click(x, y)
        else:
            self.drawing_state.process_click(x, y)
        self.redraw_screen()

    def redraw_screen(self):
        self.screen.fill((255, 255, 255))
        self.control_panel.draw(self.screen)
        self.drawing_state.redraw_everything(self.screen)
