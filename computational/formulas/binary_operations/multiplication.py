from computational.formulas.formulas import BinaryOperation


class Multiplication(BinaryOperation):
    OPERATION_STRING = "*"

    def __init__(self, expression1, expression2):
        super().__init__(expression1, expression2)

    def to_latex_string(self):
        return "(" + self.expression1.to_latex_string() + " \\cdot " + self.expression2.to_latex_string() + ")"
