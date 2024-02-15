import unittest

from computational.descriptions.circle_three_points_description import CircleThreePointsDescription
from computational.descriptions.description_writer import DescriptionWriter
from computational.descriptions.line_two_points_description import LineTwoPointsDescription
from computational.descriptions.point_free_description import PointFreeDescription


class DescriptionWriterTests(unittest.TestCase):
    def test_get_code_lines(self):
        point1 = PointFreeDescription("a")
        point2 = PointFreeDescription("b")
        line = LineTwoPointsDescription("l1", [point1, point2])
        point3 = PointFreeDescription("c")
        circle = CircleThreePointsDescription("circ", [point1, point2, point3])

        point1_line = "let a = free_point()"
        point2_line = "let b = free_point()"
        point3_line = "let c = free_point()"
        circ_line = "let circ = 3_point_circle(a, b, c)"
        line_line = "let l1 = 2_point_line(a, b)"

        self.assertEqual(DescriptionWriter.get_code_lines([line, circle]), [point1_line, point2_line, line_line,
                                                                            point3_line, circ_line])


if __name__ == '__main__':
    unittest.main()
