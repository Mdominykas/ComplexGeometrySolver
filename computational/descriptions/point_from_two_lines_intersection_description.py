from computational.descriptions.point_description import PointDescription
from computational.formulas.canonization import Canonizator
from computational.formulas.formulas import Variable, Equation
from computational.formulas.unary_operations.conjugation import Conjugation


class PointFromTwoLinesIntersectionDescription(PointDescription):
    code_line_template = "let {} = point_two_line_intersection({}, {})"

    def __init__(self, name, dependencies):
        if len(dependencies) != 2:
            raise Exception("Incorrect number of dependencies for point")
        line1, line2 = dependencies
        if not line1.is_line() or not line2.is_line():
            raise Exception("Point from two liens arguments must be lines")
        code_line = PointFromTwoLinesIntersectionDescription.code_line_template.format(name, line1.name, line2.name)
        super().__init__(name, code_line, dependencies, self._build_formula(name, line1, line2))

    @staticmethod
    def _build_formula(name, line1, line2):
        x = PointDescription(name, "", [], Variable(name))
        equation1 = line1.get_equation(x)
        equation2 = line2.get_equation(x)
        canonizator = Canonizator()
        conj_x_1 = canonizator.solve_for_variable(equation1, Conjugation(Variable(name)))
        conj_x_2 = canonizator.solve_for_variable(equation2, Conjugation(Variable(name)))
        return canonizator.solve_for_variable(Equation(conj_x_1, conj_x_2), Variable(name))
