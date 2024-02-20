import pygame

from gui.control_panel.base_control_element import BaseControlElement


class Button(BaseControlElement):
    def __init__(self, name, top_left_corner, width, height, text='', color=(0, 0, 0), button_function=lambda: 7):
        self.name = name
        super().__init__(top_left_corner, width, height, button_function)
        self.text = text
        self.color = color

    def draw(self, screen):
        (x_tl, y_tl) = self.get_top_left_corner()
        pygame.draw.rect(screen, self.color, pygame.Rect(x_tl, y_tl, self.width, self.height), width=1)

        my_font = pygame.font.SysFont('Comic Sans MS', 30)

        text_surface = my_font.render(self.name, False, (0, 0, 0))
        from_border = 5
        screen.blit(text_surface, (x_tl + from_border, y_tl + self.height / 4))

        pygame.display.flip()

    def perform_actions(self):
        self.on_click_function()
