from computational.formulas.formulas import BinaryOperation


class Multiplication(BinaryOperation):
    OPERATION_STRING = "*"

    def __init__(self, expression1, expression2):
        super().__init__(expression1, expression2)