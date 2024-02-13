import unittest

from computational.descriptions.circle_description import CircleDescription
from computational.descriptions.completed_descriptions import CompletedDescriptions
from computational.descriptions.line_description import LineDescription
from computational.descriptions.point_description import PointDescription


class BaseDescriptionTests(unittest.TestCase):
    def test_produce_code(self):
        point1 = PointDescription("a")
        point2 = PointDescription("b")
        line = LineDescription("l1", [point1, point2])
        point3 = PointDescription("c")
        circle = CircleDescription("circ", [point1, point2, point3])
        point_code, line_code, circle_code = [], [], []
        point1_line = "let a = free_point()"
        point2_line = "let b = free_point()"
        point3_line = "let c = free_point()"
        line_line = "let l1 = 2_point_line(a, b)"
        circ_line = "let circ = 3_point_circle(a, b, c)"
        point1.produce_code(CompletedDescriptions(), point_code)
        line.produce_code(CompletedDescriptions(), line_code)
        circle.produce_code(CompletedDescriptions(), circle_code)
        self.assertEqual(point_code, [point1_line])
        self.assertEqual(line_code, [point1_line, point2_line, line_line])
        self.assertEqual(circle_code, [point1_line, point2_line, point3_line, circ_line])


if __name__ == '__main__':
    unittest.main()
