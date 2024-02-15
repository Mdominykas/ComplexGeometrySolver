import unittest

from computational.descriptions.circle_three_points_description import CircleThreePointsDescription
from computational.descriptions.point_free_description import PointFreeDescription


class CircleThreePointsDescriptionTests(unittest.TestCase):
    def test_from_two_points_creates_point_description(self):
        point1 = PointFreeDescription("a")
        point2 = PointFreeDescription("b")
        point3 = PointFreeDescription("c")

        circle = CircleThreePointsDescription("line", [point1, point2, point3])
        self.assertEqual(type(circle), CircleThreePointsDescription)

    def test_can_not_create_line_from_same_point(self):
        point = PointFreeDescription("a")
        point2 = PointFreeDescription("b")
        with self.assertRaises(Exception):
            CircleThreePointsDescription("circle", [point, point, point])

        with self.assertRaises(Exception):
            CircleThreePointsDescription("circle", [point, point2, point])


if __name__ == '__main__':
    unittest.main()
