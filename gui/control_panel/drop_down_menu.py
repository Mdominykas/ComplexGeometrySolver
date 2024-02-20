from enum import Enum

from gui.control_panel.base_control_element import BaseControlElement


class DropDownDirection(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class DropDownMenu(BaseControlElement):
    def __init__(self, top_left_corner, element_width, element_height, drop_down_direction):
        self.menu_elements = []
        self.drop_down_direction = drop_down_direction
        self.element_width = element_width
        self.element_height = element_height
        assert isinstance(drop_down_direction, DropDownDirection), "drop_down_direction mus be DropDown Direction"
        super().__init__(top_left_corner, self.calculate_width(), self.calculate_height())

    def calculate_width(self):
        if self.drop_down_direction == DropDownDirection.VERTICAL:
            self.width = self.element_width
        else:
            self.width = self.element_width * (1 + len(self.menu_elements))
        return self.width

    def calculate_height(self):
        if self.drop_down_direction == DropDownDirection.HORIZONTAL:
            self.height = self.element_height
        else:
            self.height = self.element_height * (1 + len(self.menu_elements))
        return self.height

    def get_new_element_position(self):
        (x_tl, y_tl) = self.get_top_left_corner()
        if self.drop_down_direction == DropDownDirection.HORIZONTAL:
            return x_tl + self.element_width * len(self.menu_elements), y_tl
        else:
            return x_tl, y_tl + self.element_height * len(self.menu_elements)

    def add_element(self, element):
        assert isinstance(element, BaseControlElement), "Can only add instances of BaseControlElement to drop down menu"
        element.set_new_position(self.get_new_element_position())
        self.menu_elements.append(element)
        self.calculate_width()
        self.calculate_height()

    def set_new_position(self, top_left_corner):
        self.top_left_corner = top_left_corner
        (x0, y0) = self.top_left_corner
        (dx, dy) = (1, 0) if self.drop_down_direction == DropDownDirection.HORIZONTAL else (0, 1)
        for (i, element) in enumerate(self.menu_elements):
            element.set_new_position((x0 + i * dx * self.element_width, y0 + i * dy * self.element_height))

    def is_clicked(self, x, y):
        if not self.is_visible():
            return False
        for element in self.menu_elements:
            if element.is_clicked(x, y):
                return True
        return False

    def process_click(self, x, y):
        if not self.is_visible():
            return
        for element in self.menu_elements:
            element.process_click(x, y)

    def draw(self, screen):
        if self.is_visible():
            for element in self.menu_elements:
                element.draw(screen)
