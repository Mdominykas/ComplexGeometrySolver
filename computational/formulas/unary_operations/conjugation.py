from computational.formulas.formulas import UnaryOperation


class Conjugation(UnaryOperation):
    OPERATION_STRING = "conj"

    def __init__(self, expression):
        super().__init__(expression)
