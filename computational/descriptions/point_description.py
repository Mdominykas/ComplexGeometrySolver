from computational.descriptions.base_description import BaseDescription


class PointDescription(BaseDescription):
    def __init__(self, name, code_line, dependencies, formula):
        self.formula = formula
        super().__init__(name, code_line, dependencies)

    def is_point(self):
        return True

    def get_formula(self):
        return self.formula
