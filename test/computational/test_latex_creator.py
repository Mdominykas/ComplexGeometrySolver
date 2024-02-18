import os
import unittest

from computational.formulas.binary_operations.addition import Addition
from computational.formulas.formulas import Equation, Variable, Constant
from computational.formulas.unary_operations.conjugation import Conjugation
from computational.latex_creator import LatexCreator


class TestLatexCreator(unittest.TestCase):
    def test_latex_production(self):
        latex_creator = LatexCreator()
        latex_creator.add_expression(Equation(Conjugation(Variable("x")), Addition(Constant(3), Constant(5))))
        file_name = os.path.abspath(os.getcwd()) + "/temp/test_latex_production"
        latex_creator.compile_to_pdf(file_name)
        self.assertTrue(os.path.exists(file_name + ".pdf"))


if __name__ == '__main__':
    unittest.main()
