from computational.descriptions.point_description import PointDescription


class PointFromTwoLinesIntersectionDescription(PointDescription):
    code_line_template = "let {} = point_two_line_intersection({}, {})"

    def __init__(self, name, dependencies):
        if len(dependencies) != 2:
            raise Exception("Incorrect number of dependencies for point")
        line1, line2 = dependencies
        if not line1.is_line() or not line2.is_line():
            raise Exception("Point from two liens arguments must be lines")
        code_line = PointFromTwoLinesIntersectionDescription.code_line_template.format(name, line1.name, line2.name)
        super().__init__(name, code_line, dependencies)
