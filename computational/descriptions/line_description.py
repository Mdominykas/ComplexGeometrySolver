from computational.descriptions.base_description import BaseDescription


class LineDescription(BaseDescription):
    def __init__(self, name, code_line, dependencies):
        super().__init__(name, code_line, dependencies)

    def is_line(self):
        return True
