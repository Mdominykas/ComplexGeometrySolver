from computational.descriptions.base_description import BaseDescription


class PointDescription(BaseDescription):
    code_line_template = "let {} = free_point()"

    def __init__(self, name: object, dependencies: object = []) -> object:
        if len(dependencies) != 0:
            raise Exception("Too many dependencies for point")
        code_line = PointDescription.code_line_template.format(name)
        super().__init__(name, code_line, dependencies)