import pygame

from gui.control_panel.control_panel import ControlPanel
from gui.gui_constants import GuiConstants


class Gui:
    def __init__(self):
        self.control_panel = ControlPanel()
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((GuiConstants.SCREEN_WIDTH, GuiConstants.SCREEN_HEIGHT))
        pygame.display.update()
        pygame.display.set_caption("Complex Geometry Solver")

    def process_click(self, x, y):
        pass

    def redraw_screen(self, buttons, drawing_state):
        self.screen.fill((255, 255, 255))
        for button in buttons:
            button.draw(self.screen)
        drawing_state.redraw_everything(self.screen)
