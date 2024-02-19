class BaseControlElement:
    def __init__(self, top_left_corner, width, height, on_click_function=lambda: None):
        self.visibility = True # TODO: change to False, when you can construct gui
        self.top_left_corner = top_left_corner
        assert width > 0, "Width must be positive"
        assert height > 0, "Height must be positive"
        self.width = width
        self.height = height
        self.on_click_function = on_click_function

    def set_new_position(self, top_left_corner, width, height):
        self.top_left_corner = top_left_corner
        self.width = width
        self.height = height

    def is_visible(self):
        return self.visibility

    def get_top_left_corner(self):
        return self.top_left_corner

    def get_bottom_right_corner(self):
        (x_top_left, y_top_left) = self.get_top_left_corner()
        return x_top_left + self.width, y_top_left + self.height

    def is_clicked(self, x, y):
        if not self.is_visible():
            return False
        (x_tl, y_tl) = self.get_top_left_corner()
        (x_br, y_br) = self.get_bottom_right_corner()

        return (x_tl <= x) and (x <= x_br) and (y_tl <= y) and (y <= y_br)

    def on_click(self):
        self.on_click_function()

    def open(self):
        self.visibility = True

    def close(self):
        self.visibility = False

    # def draw(self):
    #     assert False, "Draw is not implemented in base class"
