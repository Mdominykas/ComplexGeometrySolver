# !!!!! I can change name to some sort of implementation of that thing (e.g. operation must implement how to print in
# latex, how to collapse, how to invert etc.
class Variable:
    def __init__(self, name):
        self.name = name


class Constant:
    def __init__(self, value):
        self.value = value


class BinaryOperation:
    def __init__(self, name, expression1, expression2):
        self.name = name
        self.expression1 = expression1
        self.expression2 = expression2


class UnaryOperation:
    def __init__(self, name, expression):
        self.name = name
        self.expression1 = expression


class Equation:
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

class Expression:
    @staticmethod
    def from_variable(name):
        return Variable(name)

    @staticmethod
    def from_binary_operation(name, expression1, expression2):
        return BinaryOperation(name, expression1, expression2)

    @staticmethod
    def from_unary_operation(name, expression):
        return UnaryOperation(name, expression)

    @staticmethod
    def from_constant(value):
        return Constant(value)

    @staticmethod
    def from_equation(expression1, expression2):
        return Equation(expression1, expression2)