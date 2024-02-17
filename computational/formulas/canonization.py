from computational.formulas.binary_operations.addition import Addition
from computational.formulas.binary_operations.division import Division
from computational.formulas.binary_operations.multiplication import Multiplication
from computational.formulas.binary_operations.subtraction import Subtraction
from computational.formulas.formulas import Variable, Constant, BinaryOperation, Equation
from computational.formulas.unary_operations.conjugation import Conjugation


class Canonizator:
    def __init__(self):
        pass

    def solve_for_variable(self, equation, variable):
        equation = self.canonize_equation(equation)
        assert isinstance(equation, Equation)
        assert isinstance(equation.expression1, Division)
        expression = equation.expression1.expression1
        monomials = self.split_to_monomials(expression)
        monomials = [self.convert_multiplication_to_list(mono) for mono in monomials]
        constant_and_sorted_monomial = [self.sort_monomial_and_find_constant(mono) for mono in monomials]
        assert not self.has_double_variable(constant_and_sorted_monomial, variable), "Only solves linear equations"
        with_variable, without_variable = self.find_monomials_with_variable(constant_and_sorted_monomial, variable)
        with_variable = [self.factor_out(term, variable) for term in with_variable]
        return Division(Subtraction(Constant(0), self.construct_formula(without_variable)),
                        self.construct_formula(with_variable))

    def canonize_equation(self, equation):
        lhs, rhs = equation.return_both_sides()
        return Equation(self.canonize_expression(Subtraction(lhs, rhs)), Constant(0))

    def canonize_expression(self, expression):
        expression = self.simplify_conjugation(expression, False)
        expression = self.convert_subtraction_to_addition(expression)
        expression = self.rationalize(expression)
        return expression

    def simplify_conjugation(self, expression, have_odd_conjugations=False):
        if isinstance(expression, Variable):
            if have_odd_conjugations:
                return Conjugation(expression)
            else:
                return expression
        elif isinstance(expression, Constant):
            return expression
        elif isinstance(expression, Conjugation):
            return self.simplify_conjugation(expression.expression, not have_odd_conjugations)
        elif isinstance(expression, BinaryOperation):
            part1, part2 = expression.return_parts()
            part1, part2 = (self.simplify_conjugation(part1, have_odd_conjugations),
                            self.simplify_conjugation(part2, have_odd_conjugations))
            return expression.rebuild_from_parts(part1, part2)
        elif isinstance(expression, Equation):
            lhs, rhs = expression.return_both_sides()
            lhs, rhs = (self.simplify_conjugation(lhs, have_odd_conjugations),
                        self.simplify_conjugation(rhs, have_odd_conjugations))
            return Equation(lhs, rhs)
        else:
            assert False, "Unknown instance passed to simplify_conjugation"

    def convert_subtraction_to_addition(self, expression):
        if isinstance(expression, Variable):
            return expression
        elif isinstance(expression, Constant):
            return expression
        elif isinstance(expression, Conjugation):
            return Conjugation(self.convert_subtraction_to_addition(expression.expression))
        elif isinstance(expression, BinaryOperation):
            part1, part2 = expression.return_parts()
            part1, part2 = (self.convert_subtraction_to_addition(part1), self.convert_subtraction_to_addition(part2))
            if isinstance(expression, Subtraction):
                return Addition(part1, Multiplication(Constant(-1), part2))
            else:
                return expression.rebuild_from_parts(part1, part2)
        elif isinstance(expression, Equation):
            lhs, rhs = expression.return_both_sides()
            lhs, rhs = (self.convert_subtraction_to_addition(lhs), self.convert_subtraction_to_addition(rhs))
            return Equation(lhs, rhs)
        else:
            assert False, "Unknown instance passed to convert_subtraction_to_addition"

    def rationalize(self, expression):
        if isinstance(expression, Variable):
            return Division(expression, Constant(1))
        elif isinstance(expression, Constant):
            return Division(expression, Constant(1))
        elif isinstance(expression, Conjugation):
            inside = expression.expression
            inside = self.rationalize(inside)
            assert isinstance(inside, Division)
            top, bot = inside.return_parts()
            top, bot = self.simplify_conjugation(Conjugation(top)), self.simplify_conjugation(bot)
            return Division(top, bot)
        elif isinstance(expression, BinaryOperation):
            p1, p2 = expression.return_parts()
            p1, p2 = self.rationalize(p1), self.rationalize(p2)
            p1_top, p1_bot = p1.return_parts()
            p2_top, p2_bot = p2.return_parts()
            if isinstance(expression, Division):
                return Division(Multiplication(p1_top, p2_bot), Multiplication(p1_bot, p2_top))
            elif isinstance(expression, Multiplication):
                return Division(Multiplication(p1_top, p2_top), Multiplication(p1_bot, p2_bot))
            elif isinstance(expression, Subtraction):
                return Division(Subtraction(Multiplication(p1_top, p2_bot), Multiplication(p1_bot, p2_top)),
                                Multiplication(p1_bot, p2_bot))
            elif isinstance(expression, Addition):
                return Division(Addition(Multiplication(p1_top, p2_bot), Multiplication(p1_bot, p2_top)),
                                Multiplication(p1_bot, p2_bot))
            else:
                assert False, "unknown binary expression"
        elif isinstance(expression, Equation):
            lhs, rhs = expression.return_both_sides()
            return Equation(self.rationalize(lhs), self.rationalize(rhs))
        else:
            assert False, "Unknown instance passed to rationalize"

    # returns list of monomials
    def split_to_monomials(self, expression):
        if isinstance(expression, Variable) or isinstance(expression, Constant):
            return [expression]
        elif isinstance(expression, Conjugation):
            inside = expression.expression
            assert isinstance(inside, Variable) or isinstance(inside, Constant), \
                "Conjugation must be simplified before spliting to monomials"
            return [expression]
        elif isinstance(expression, BinaryOperation):
            p1, p2 = expression.return_parts()
            p1, p2 = self.split_to_monomials(p1), self.split_to_monomials(p2)
            if isinstance(expression, Addition):
                return p1 + p2
            elif isinstance(expression, Multiplication):
                return [Multiplication(a, b) for a in p1 for b in p2]
            else:
                assert False, "All other binary operations should have been removed"
        else:
            assert False, "split_to_monomials doesn't handle other types of expressions"

    def convert_multiplication_to_list(self, expression):
        if isinstance(expression, Variable) or isinstance(expression, Constant):
            return [expression]
        elif isinstance(expression, Conjugation):
            inside = expression.expression
            assert isinstance(inside, Variable) or isinstance(inside, Constant), \
                "Conjugation must be simplified before converting multiplication to list"
            return [expression]
        elif isinstance(expression, Multiplication):
            part1, part2 = expression.return_parts()
            return self.convert_multiplication_to_list(part1) + self.convert_multiplication_to_list(part2)
        else:
            assert False, "Invalid operation inside conversion to multiplication"

    @staticmethod
    def sort_monomial_and_find_constant(monomial):
        def var_name(x):
            if isinstance(x, Variable):
                return x.name
            elif isinstance(x, Conjugation):
                x = x.expression
                assert isinstance(x, Variable)
                return x.name
            else:
                assert False

        assert isinstance(monomial, list)
        final_constant = Constant(1)
        variables = []
        for el in monomial:
            if isinstance(el, Variable):
                variables.append(el)
            elif isinstance(el, Conjugation):
                inside = el.expression
                assert isinstance(inside, Variable), \
                    "Conjugation must be simplified before converting multiplication to list"
                variables.append(el)
            else:
                assert isinstance(el, Constant), "Only variables and constants  at sort_monomial_and_find_constant"
                final_constant = Constant(final_constant.value * el.value)
        variables = sorted(variables, key=var_name)
        return final_constant, variables

    @staticmethod
    def simplify_constant_and_monomial_list(constant_and_sorted_monomial):
        ans = []
        for (const, mono) in constant_and_sorted_monomial:
            if len(ans) == 0:
                ans.append((const, mono))
            elif len(mono) == len(ans[-1][1]):
                are_equal = True
                for (cur, prev) in zip(mono, ans[-1][1]):
                    if not cur.is_identical(prev):
                        are_equal = False
                if are_equal:
                    ans[-1] = Constant(ans[-1][0].value + const.value), ans[-1][1]
                else:
                    ans.append((const, mono))
            else:
                ans.append((const, mono))
        return ans

    # return two lists: one of monomials with constants that have variable and one that doesn't have them
    @staticmethod
    def find_monomials_with_variable(constant_and_sorted_monomial, variable):
        with_variable, without_variable = [], []
        for (const, mono) in constant_and_sorted_monomial:
            has_variable = False
            for var in mono:
                if var.is_identical(variable):
                    has_variable = True

            if has_variable:
                with_variable.append((const, mono))
            else:
                without_variable.append((const, mono))
        return with_variable, without_variable

    @staticmethod
    def has_double_variable(constant_and_monomials, variable):
        has = False
        for (const, mono) in constant_and_monomials:
            count = 0
            for var in mono:
                if var.is_identical(variable):
                    count += 1
            if count > 1:
                has = True
        return has

    @staticmethod
    def construct_formula(constants_and_monomials):
        def multiply_all(factors):
            assert len(factors) > 0, "Can not multiply empty list"
            answer = factors[0]
            for i in range(1, len(factors)):
                answer = Multiplication(answer, factors[i])
            return answer

        def add_all(terms):
            assert len(terms) > 0, "Can not add empty list"
            answer = terms[0]
            for i in range(1, len(terms)):
                answer = Addition(answer, terms[i])
            return answer

        multiplications = [multiply_all([constant] + monomial) for (constant, monomial) in constants_and_monomials]
        return add_all(multiplications)

    @staticmethod
    def factor_out(constant_and_monomial, variable):
        (const, mono) = constant_and_monomial
        cur_mono = []
        removed = False
        for el in mono:
            if el.is_identical(variable) and not removed:
                removed = True
            else:
                cur_mono.append(el)
        return const, cur_mono
