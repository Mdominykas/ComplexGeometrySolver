from computational.descriptions.point_description import PointDescription


class LineTwoPointsDescription(PointDescription):
    code_line_template = "let {} = 2_point_line({}, {})"

    def __init__(self, name, dependencies):
        if len(dependencies) != 2:
            raise Exception("Too few values for line")
        point1, point2 = dependencies
        if point1 == point2:
            raise Exception("Line is created from single point")
        if not point1.is_point() or not point2.is_point():
            raise Exception("2 point line must be created from two points")
        code_line = LineTwoPointsDescription.code_line_template.format(name, point1.name, point2.name)
        super().__init__(name, code_line, dependencies)

