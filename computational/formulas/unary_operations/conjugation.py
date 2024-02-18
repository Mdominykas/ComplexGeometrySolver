from computational.formulas.formulas import UnaryOperation


class Conjugation(UnaryOperation):
    OPERATION_STRING = "conj"

    def __init__(self, expression):
        super().__init__(expression)

    def to_latex_string(self):
        return "\\overline{" + self.expression.to_latex_string() + "}"
