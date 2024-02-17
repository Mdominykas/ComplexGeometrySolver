import unittest

from computational.formulas.binary_operations.addition import Addition
from computational.formulas.binary_operations.division import Division
from computational.formulas.binary_operations.multiplication import Multiplication
from computational.formulas.binary_operations.subtraction import Subtraction
from computational.formulas.canonization import Canonizator
from computational.formulas.formulas import Constant, Variable, Equation
from computational.formulas.unary_operations.conjugation import Conjugation


class CanonizatorTests(unittest.TestCase):
    def test_conjugation_simplification_addition_and_constant(self):
        canonizator = Canonizator()
        initial_expression = Conjugation(Addition(Variable("a"), Constant(3)))
        expected_expression = Addition(Conjugation(Variable("a")), Constant(3))
        self.assertTrue(canonizator.simplify_conjugation(initial_expression).is_identical(expected_expression))

    def test_conjugation_simplification_remove_double_conjugation(self):
        canonizator = Canonizator()
        initial_expression = Conjugation(Addition(Conjugation(Variable("a")), Constant(3)))
        expected_expression = Addition(Variable("a"), Constant(3))
        self.assertTrue(canonizator.simplify_conjugation(initial_expression).is_identical(expected_expression))

    def test_conjugation_simplification_equation_multiplication_subtraction(self):
        canonizator = Canonizator()
        initial_expression = Equation(Conjugation(Multiplication(Variable("a"), Constant(3))),
                                      Subtraction(Variable("b"), Constant(5)))
        expected_expression = Equation(Multiplication(Conjugation(Variable("a")), Constant(3)),
                                       Subtraction(Variable("b"), Constant(5)))
        self.assertTrue(canonizator.simplify_conjugation(initial_expression).is_identical(expected_expression))

    def test_convert_subtraction_to_addition(self):
        canonizator = Canonizator()
        initial_expression = Subtraction(Constant(3), Variable("b"))
        expected_expression = Addition(Constant(3), Multiplication(Constant(-1), Variable("b")))
        self.assertTrue(
            canonizator.convert_subtraction_to_addition(initial_expression).is_identical(expected_expression))

        initial_expression = Subtraction(Conjugation(Variable("a")), Multiplication(Constant(3), Variable("b")))
        expected_expression = Addition(Conjugation(Variable("a")),
                                       Multiplication(Constant(-1), Multiplication(Constant(3), Variable("b"))))
        self.assertTrue(
            canonizator.convert_subtraction_to_addition(initial_expression).is_identical(expected_expression))

    def test_rationalize(self):
        canonizator = Canonizator()
        initial_expression = Subtraction(Constant(3), Variable("b"))
        expected_expression = Division(
            Subtraction(Multiplication(Constant(3), Constant(1)), Multiplication(Constant(1), Variable("b"))),
            Multiplication(Constant(1), Constant(1)))
        self.assertTrue(canonizator.rationalize(initial_expression).is_identical(expected_expression))

    def test_split_to_monomials(self):
        canonizator = Canonizator()
        initial_expression = Addition(Multiplication(Addition(Constant(3), Variable("b")),
                                                     Addition(Variable("a"), Conjugation(Variable("b")))), Constant(4))
        expected_monomials = [Multiplication(Constant(3), Variable("a")),
                              Multiplication(Constant(3), Conjugation(Variable("b"))),
                              Multiplication(Variable("b"), Variable("a")),
                              Multiplication(Variable("b"), Conjugation(Variable("b"))),
                              Constant(4)]
        received_monomials = canonizator.split_to_monomials(initial_expression)
        self.assertEqual(len(expected_monomials), len(received_monomials))
        for (exp, rev) in zip(expected_monomials, received_monomials):
            self.assertTrue(exp.is_identical(rev))

    def test_convert_multiplication_to_list(self):
        canonizator = Canonizator()
        initial_expression = Multiplication(Multiplication(Variable("a"), Multiplication(Constant(5), Variable("b"))),
                                            Conjugation(Variable("c")))
        expected_list = [Variable("a"), Constant(5), Variable("b"), Conjugation(Variable("c"))]
        output_list = canonizator.convert_multiplication_to_list(initial_expression)
        self.assertEqual(len(output_list), len(expected_list))
        for (exp, out) in zip(expected_list, output_list):
            self.assertTrue(exp.is_identical(out))

    def test_sort_monomial_and_find_constant(self):
        canonizator = Canonizator()
        initial_expression = [Variable("c"), Constant(5), Variable("a"), Conjugation(Variable("b")), Constant(2)]
        expected_constant, expected_monomial = Constant(10), [Variable("a"), Conjugation(Variable("b")), Variable("c")]
        constant, monomial = canonizator.sort_monomial_and_find_constant(initial_expression)
        self.assertTrue(constant.is_identical(expected_constant))
        self.assertEqual(len(monomial), len(expected_monomial))
        for (exp, out) in zip(monomial, expected_monomial):
            self.assertTrue(exp.is_identical(out))

    def test_simplify_constant_and_monomial_list(self):
        canonizator = Canonizator()
        initial_expression = [(Constant(5), [Variable("a"), Variable("c")]),
                              (Constant(4), [Variable("a"), Variable("c")]),
                              (Constant(2), [Conjugation(Variable("a"))])]
        expected_output = [(Constant(9), [Variable("a"), Variable("c")]), (Constant(2), [Conjugation(Variable("a"))])]
        output = canonizator.simplify_constant_and_monomial_list(initial_expression)
        self.assertEqual(len(output), len(expected_output))
        for ((const1, lst1), (const2, lst2)) in zip(output, expected_output):
            self.assertTrue(const1.is_identical(const2))
            self.assertEqual(len(lst1), len(lst2))
            for (el1, el2) in zip(lst1, lst2):
                self.assertTrue(el1.is_identical(el2))

    def test_find_monomials_with_variable(self):
        canonizator = Canonizator()
        variable = Variable("a")
        monomials_with_constants = [(Constant(5), [Variable("a"), Variable("c")]),
                                    (Constant(2), [Conjugation(Variable("a"))]),
                                    (Constant(4), [Variable("d"), Variable("a")])]
        expected_with = [(Constant(5), [Variable("a"), Variable("c")]), (Constant(4), [Variable("d"), Variable("a")])]
        expected_without = [(Constant(2), [Conjugation(Variable("a"))])]
        output_with, output_without = canonizator.find_monomials_with_variable(monomials_with_constants, variable)

        def assert_equality(output, expected):
            self.assertEqual(len(output), len(expected))
            for (exp, out) in zip(expected, output):
                self.assertTrue(exp[0].is_identical(out[0]))
                for (el1, el2) in zip(exp[1], out[1]):
                    self.assertTrue(el1.is_identical(el2))

        assert_equality(output_with, expected_with)
        assert_equality(output_without, expected_without)

    def test_has_double_variable(self):
        canonizator = Canonizator()
        variable = Variable("a")

        monomials_with_constants = [(Constant(5), [Variable("b"), Variable("c")]),
                                    (Constant(2), [Conjugation(Variable("a")), Variable("a")]),
                                    (Constant(4), [Variable("d"), Variable("a")])]
        self.assertFalse(canonizator.has_double_variable(monomials_with_constants, variable))

        monomials_with_constants = [(Constant(5), [Variable("b"), Variable("c")]),
                                    (Constant(2), [Conjugation(Variable("a")), Variable("a")]),
                                    (Constant(4), [Variable("a"), Variable("a")])]
        self.assertTrue(canonizator.has_double_variable(monomials_with_constants, variable))

        monomials_with_constants = [(Constant(5), [Variable("b"), Variable("b")])]
        self.assertFalse(canonizator.has_double_variable(monomials_with_constants, variable))

    def test_solve_for_variable(self):
        canonizator = Canonizator()
        variable = Variable("a")
        equation = Equation(Addition(Variable("a"), Variable("b")), Constant(0))
        expected_solution = Division(Subtraction(Constant(0), Addition(Multiplication(Constant(1), Variable("b")),
                                                                       Constant(0))), Constant(1))
        solution = canonizator.solve_for_variable(equation, variable)
        print("solution_string = ", solution.to_string())

        self.assertTrue(expected_solution.is_identical(solution))


if __name__ == '__main__':
    unittest.main()
