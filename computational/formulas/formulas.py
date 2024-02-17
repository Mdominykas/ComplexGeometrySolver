# !!!!! I can change name to some sort of implementation of that thing (e.g. operation must implement how to print in
# latex, how to collapse, how to invert etc.
class Variable:
    def __init__(self, name):
        self.name = name

    def clone(self):
        return Variable(self.name)

    def is_identical(self, other):
        return isinstance(other, Variable) and self.name == other.name

    def to_string(self):
        return self.name


class Constant:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return Constant(self.value)

    def is_identical(self, other):
        return isinstance(other, Constant) and self.value == other.value

    def to_string(self):
        return str(self.value)


class BinaryOperation:
    OPERATION_STRING = "?"

    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def clone(self):
        return BinaryOperation(self.expression1, self.expression2)

    def return_parts(self):
        return self.expression1, self.expression2

    def rebuild_from_parts(self, expression1, expression2):
        t = type(self)
        return t(expression1, expression2)

    def is_identical(self, other):
        if type(self) != type(other):
            return False
        p1, p2 = other.return_parts()
        return self.expression1.is_identical(p1) and self.expression2.is_identical(p2)

    def to_string(self):
        return "(" + self.expression1.to_string() + self.OPERATION_STRING + self.expression2.to_string() + ")"


class UnaryOperation:
    OPERATION_STRING = "?"

    def __init__(self, expression):
        self.expression = expression

    def clone(self):
        return UnaryOperation(self.expression)

    def is_identical(self, other):
        if type(self) != type(other):
            return False
        return self.expression.is_identical(other.expression)

    def to_string(self):
        return self.OPERATION_STRING + "(" + self.expression.to_string() + ")"


class Equation:
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def clone(self):
        return Equation(self.expression1, self.expression2)

    def return_both_sides(self):
        return self.expression1, self.expression2

    def is_identical(self, other):
        if type(self) != type(other):
            return False
        p1, p2 = other.return_both_sides()
        return self.expression1.is_identical(p1) and self.expression2.is_identical(p2)

    def to_string(self):
        return self.expression1.to_string() + "=" + self.expression2.to_string()
