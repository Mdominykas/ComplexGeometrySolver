import unittest

from computational.Parser import Parser
from computational.descriptions.description_writer import DescriptionWriter
from computational.descriptions.line_two_points_description import LineTwoPointsDescription
from computational.descriptions.point_free_description import PointFreeDescription


class MyTestCase(unittest.TestCase):
    def test_division_to_lexemes(self):
        lexemes = Parser.divide_to_lexemes("a = b 123 1a,b (2)")
        self.assertEqual(lexemes, ["a", "=", "b", "123", "1a", ",", "b", "(", "2", ")"])

    def test_can_parse_when_possible(self):
        code_line = "let a = 2_point_line(b, c)"
        code_line_template = "let {} = 2_point_line({}, {})"
        self.assertTrue(Parser.can_parse(code_line_template, code_line))

    def test_cant_parse_when_too_many_lexemes(self):
        code_line = "let a = 2_point_line(b, c, d)"
        code_line_template = "let {} = 2_point_line({}, {})"
        self.assertFalse(Parser.can_parse(code_line_template, code_line))

    def test_cant_parser_when_different_text(self):
        code_line = "leta a = 2_point_line(b, c)"
        code_line_template = "let {} = 2_point_line({}, {})"
        self.assertFalse(Parser.can_parse(code_line_template, code_line))

    def test_can_parse_when_different_whitespace(self):
        code_line = "let    a=   2_point_line(  b,c)"
        print(Parser.divide_to_lexemes(code_line))
        code_line_template = "let {} = 2_point_line({}, {})"
        self.assertTrue(Parser.can_parse(code_line_template, code_line))

    def test_parsing(self):
        point1 = PointFreeDescription("a")
        point2 = PointFreeDescription("b")
        line = LineTwoPointsDescription("line", [point1, point2])

        code_lines = DescriptionWriter.get_code_lines([line])
        parser = Parser()
        constructions = [parser.parse(line) for line in code_lines]
        self.assertEqual(type(constructions[0]), PointFreeDescription)
        self.assertEqual(type(constructions[1]), PointFreeDescription)
        self.assertEqual(type(constructions[2]), LineTwoPointsDescription)


if __name__ == '__main__':
    unittest.main()
