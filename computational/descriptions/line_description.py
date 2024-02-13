from computational.descriptions.base_description import BaseDescription


class LineDescription(BaseDescription):
    code_line_template = "let {} = 2_point_line({}, {})"

    def __init__(self, name, dependencies):
        if len(dependencies) != 2:
            raise Exception("Too few values for line")
        point1, point2 = dependencies
        if point1 == point2:
            raise Exception("Line is created from single point")
        code_line = LineDescription.code_line_template.format(name, point1.name, point2.name)
        super().__init__(name, code_line, dependencies)

