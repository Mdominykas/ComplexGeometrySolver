from gui.control_panel.base_control_element import BaseControlElement
from gui.control_panel.button import Button
from gui.control_panel.drop_down_menu import DropDownMenu, DropDownDirection
from gui.drawing_plane.drawing_state import DrawingState
from gui.gui_constants import GuiConstants


class ControlPanel:
    def __init__(self, drawing_state):
        self.main_panel = DropDownMenu(GuiConstants.PANEL_START, GuiConstants.BUTTON_WIDTH, GuiConstants.BUTTON_HEIGHT,
                                       DropDownDirection.HORIZONTAL)
        buttons = [Button("Point", (10, 10), GuiConstants.BUTTON_WIDTH, GuiConstants.BUTTON_HEIGHT, button_function=lambda: drawing_state.change_mode(DrawingState.POINT_MODE)),
                   Button("Line", (80, 10), GuiConstants.BUTTON_WIDTH, GuiConstants.BUTTON_HEIGHT, button_function=lambda: drawing_state.change_mode(DrawingState.LINE_MODE)),
                   Button("Circle", (160, 10), GuiConstants.BUTTON_WIDTH, GuiConstants.BUTTON_HEIGHT, button_function=lambda: drawing_state.change_mode(DrawingState.CIRCLE_MODE))]
        for button in buttons:
            self.main_panel.add_element(button)

        drop_down_panel = DropDownMenu((0, 0), GuiConstants.BUTTON_WIDTH, GuiConstants.BUTTON_HEIGHT, DropDownDirection.HORIZONTAL)
        useless_button1 = Button("Show properties", (260, 10), GuiConstants.BUTTON_WIDTH, GuiConstants.BUTTON_HEIGHT)
        useless_button2 = Button("Export proof", (260, 10), GuiConstants.BUTTON_WIDTH, GuiConstants.BUTTON_HEIGHT)
        drop_down_panel.add_element(useless_button1)
        drop_down_panel.add_element(useless_button2)
        self.main_panel.add_element(drop_down_panel)


    def is_clicked(self, x, y):
        return self.main_panel.is_clicked(x, y)

    def process_click(self, x, y):
        self.main_panel.process_click(x, y)

    def draw(self, screen):
        self.main_panel.draw(screen)
