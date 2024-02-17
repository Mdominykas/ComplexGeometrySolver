from computational.descriptions.point_description import PointDescription
from computational.formulas.formulas import Variable


class PointFreeDescription(PointDescription):
    code_line_template = "let {} = free_point()"

    def __init__(self, name: object, dependencies=[]):
        if len(dependencies) != 0:
            raise Exception("Too many dependencies for point")
        code_line = PointFreeDescription.code_line_template.format(name)
        super().__init__(name, code_line, dependencies, Variable(name))
