from computational.descriptions.base_description import BaseDescription


class CircleDescription(BaseDescription):
    code_line_template = "let {} = 3_point_circle({}, {}, {})"

    def __init__(self, name, dependencies):
        if len(dependencies) != 3:
            raise Exception("Too few values for point")
        point1, point2, point3 = dependencies
        if point1 == point2 or point2 == point3 or point1 == point3:
            raise Exception("Circle is created from not distinct points")
        code_line = CircleDescription.code_line_template.format(name, point1.name, point2.name, point3.name)
        super().__init__(name, code_line, dependencies)
