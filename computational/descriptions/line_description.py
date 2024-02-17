from computational.descriptions.base_description import BaseDescription
from computational.formulas.binary_operations.division import Division
from computational.formulas.binary_operations.subtraction import Subtraction
from computational.formulas.formulas import Equation
from computational.formulas.unary_operations.conjugation import Conjugation


class LineDescription(BaseDescription):
    def __init__(self, name, code_line, dependencies, point_on_line, line_direction_formula):
        self.point_on_line = point_on_line
        self.line_direction_formula = line_direction_formula
        super().__init__(name, code_line, dependencies)

    def is_line(self):
        return True

    def get_equation(self, x):
        assert x.is_point(), "Line equation was being formed not from point"

        x_minus_point = Subtraction(x.get_formula(), self.point_on_line.get_formula())

        return Equation(Division(x_minus_point, Conjugation(x_minus_point)), self.line_direction_formula)
