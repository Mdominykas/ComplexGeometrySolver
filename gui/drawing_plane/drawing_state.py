import pygame

from gui.drawing_plane.circle import Circle
from gui.drawing_plane.line import Line
from gui.drawing_plane.point import Point
from gui.gui_constants import GuiConstants


class DrawingState:
    POINT_MODE = 0
    LINE_MODE = 1
    CIRCLE_MODE = 2
    DIST_EPSILON = 50

    def __init__(self, point_namer):
        self.point_namer = point_namer
        self.points, self.lines, self.circles = [], [], []
        self.mode = DrawingState.POINT_MODE
        self.selected_points = []

    def process_click(self, x, y):
        match self.mode:
            case DrawingState.POINT_MODE:
                print("process point")
                self.process_point(x, y)
            case DrawingState.LINE_MODE:
                print("process line")
                self.process_line(x, y)
            case DrawingState.CIRCLE_MODE:
                print("process circle")
                self.process_circle(x, y)

    def change_mode(self, new_mode):
        if self.mode != new_mode:
            self.mode = new_mode
            self.selected_points = []

    def process_point(self, x, y):
        self.points.append(Point(x, y, self.point_namer))

    def select_point(self, x, y):
        for point in self.points:
            if (point not in self.selected_points) and (point.dist_to(x, y) < DrawingState.DIST_EPSILON):
                print("PASIRINKAU KAZKA")
                self.selected_points.append(point)
                break

    def process_line(self, x, y):
        self.select_point(x, y)
        if len(self.selected_points) == 2:
            self.lines.append(Line(self.selected_points[0], self.selected_points[1]))
            self.selected_points = []

    def process_circle(self, x, y):
        self.select_point(x, y)
        if len(self.selected_points) == 3:
            self.circles.append(Circle(self.selected_points[0], self.selected_points[1], self.selected_points[2]))
            self.selected_points = []

    def redraw_everything(self, screen):
        for point in self.points:
            point.draw(screen)

        for line in self.lines:
            line.draw(screen)

        for circle in self.circles:
            circle.draw(screen)

        for (i, selected_point) in enumerate(self.selected_points):
            self.draw_text(screen, GuiConstants.SELECTED_POINTS_X,
                           GuiConstants.SELECTED_POINTS_Y + i * GuiConstants.SELECTED_POINTS_INC,
                           selected_point.to_string())

        pygame.display.update()

    @staticmethod
    def draw_text(screen, x, y, text):
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render(text, False, (0, 0, 0))
        screen.blit(text_surface, (x, y))
