import pygame
import math


class Point:
    def __init__(self, x, y, namer):
        self.x = x
        self.y = y
        self.namer = namer
        self.name = namer.get_name()

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 5)

        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render(self.name, False, (0, 0, 0))
        screen.blit(text_surface, (self.x, self.y))

    def get_coords(self):
        return self.x, self.y

    def dist_to(self, x, y):
        return math.sqrt((x - self.x)**2 + (y - self.y) ** 2)

    def to_string(self):
        return self.name