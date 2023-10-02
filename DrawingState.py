class DrawingState:
    POINT_MODE = 0
    LINE_MODE = 1
    CIRCLE_MODE = 2

    def __init__(self):
        self.mode = DrawingState.POINT_MODE
