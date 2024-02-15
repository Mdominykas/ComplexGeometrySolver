import unittest

from computational.descriptions.line_two_points_description import LineTwoPointsDescription
from computational.descriptions.point_free_description import PointFreeDescription
from computational.descriptions.point_from_two_lines_intersection_description import \
    PointFromTwoLinesIntersectionDescription


class PointFromTwoLinesIntersectionDescriptionTest(unittest.TestCase):
    def test_correct_construction(self):
        a, b, c, d = (PointFreeDescription("a"), PointFreeDescription("b"), PointFreeDescription("c"),
                      PointFreeDescription("d"))
        line1, line2 = LineTwoPointsDescription("l1", [a, b]), LineTwoPointsDescription("l2", [c, d])
        e = PointFromTwoLinesIntersectionDescription("e", [line1, line2])

    def test_incorrect_construction_when_passed_float(self):
        a, b = PointFreeDescription("a"), PointFreeDescription("b")
        with self.assertRaises(Exception):
            e = PointFromTwoLinesIntersectionDescription("e", [a, b])


if __name__ == '__main__':
    unittest.main()
