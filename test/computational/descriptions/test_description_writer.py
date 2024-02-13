import unittest

from computational.descriptions.circle_description import CircleDescription
from computational.descriptions.description_writer import DescriptionWriter
from computational.descriptions.line_description import LineDescription
from computational.descriptions.point_description import PointDescription


class DescriptionWriterTests(unittest.TestCase):
    def test_get_code_lines(self):
        point1 = PointDescription("a")
        point2 = PointDescription("b")
        line = LineDescription("l1", [point1, point2])
        point3 = PointDescription("c")
        circle = CircleDescription("circ", [point1, point2, point3])

        point1_line = "let a = free_point()"
        point2_line = "let b = free_point()"
        point3_line = "let c = free_point()"
        circ_line = "let circ = 3_point_circle(a, b, c)"
        line_line = "let l1 = 2_point_line(a, b)"

        self.assertEqual(DescriptionWriter.get_code_lines([line, circle]), [point1_line, point2_line, line_line,
                                                                            point3_line, circ_line])


if __name__ == '__main__':
    unittest.main()
