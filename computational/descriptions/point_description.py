from computational.descriptions.base_description import BaseDescription


class PointDescription(BaseDescription):
    def __init__(self, name, code_line, dependencies):
        super().__init__(name, code_line, dependencies)

    def is_point(self):
        return True
