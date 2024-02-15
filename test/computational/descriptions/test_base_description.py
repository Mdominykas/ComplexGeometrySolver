import unittest

from computational.descriptions.circle_three_points_description import CircleThreePointsDescription
from computational.descriptions.completed_descriptions import CompletedDescriptions
from computational.descriptions.line_two_points_description import LineTwoPointsDescription
from computational.descriptions.point_free_description import PointFreeDescription


class BaseDescriptionTests(unittest.TestCase):
    def test_produce_code(self):
        point1 = PointFreeDescription("a")
        point2 = PointFreeDescription("b")
        line = LineTwoPointsDescription("l1", [point1, point2])
        point3 = PointFreeDescription("c")
        circle = CircleThreePointsDescription("circ", [point1, point2, point3])
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
