import pygame


class Button:
    # top_left_corner = (x, y) where (0, 0) is the top_left_corner of the screen
    def __init__(self, name, top_left_corner, bottom_right_corner, text='', color=(0, 0, 0), button_function=lambda: 7):
        self.name = name
        assert(top_left_corner[0] <= bottom_right_corner[0])
        assert (top_left_corner[1] <= bottom_right_corner[1])
        self.top_left_corner = top_left_corner
        self.bottom_right_corner = bottom_right_corner
        self.text = text
        self.color = color
        self.button_function = button_function

    def __top_left_width_height(self):
        top = self.top_left_corner[1]
        left = self.top_left_corner[0]
        width = self.bottom_right_corner[0] - self.top_left_corner[0]
        height = self.bottom_right_corner[1] - self.top_left_corner[1]
        assert (top >= 0)
        assert (left >= 0)
        assert (width >= 0)
        assert (height >= 0)
        return top, left, width, height

    def draw(self, screen):
        top, left, width, height = self.__top_left_width_height()
        pygame.draw.rect(screen, self.color, pygame.Rect(left, top, width, height), width=1)

        my_font = pygame.font.SysFont('Comic Sans MS', 30)

        text_surface = my_font.render(self.name, False, (0, 0, 0))
        from_border = 5
        screen.blit(text_surface, (left + from_border, top + height / 4))

        pygame.display.flip()

    def is_clicked(self, x, y):
        print("x, y =", x, y)
        # print(x, self.top_left_corner, y, self.bottom_right_corner)

        return ((self.top_left_corner[0] <= x) and (x <= self.bottom_right_corner[0])
                and (self.top_left_corner[1] <= y) and (y <= self.bottom_right_corner[1]))

    def perform_actions(self):
        self.button_function()
