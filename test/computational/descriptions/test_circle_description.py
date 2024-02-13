import unittest

from computational.descriptions.circle_description import CircleDescription
from computational.descriptions.point_description import PointDescription


class CircleDescriptionTests(unittest.TestCase):
    def test_from_two_points_creates_point_description(self):
        point1 = PointDescription("a")
        point2 = PointDescription("b")
        point3 = PointDescription("c")

        circle = CircleDescription("line", [point1, point2, point3])
        self.assertEqual(type(circle), CircleDescription)

    def test_can_not_create_line_from_same_point(self):
        point = PointDescription("a")
        point2 = PointDescription("b")
        try:
            CircleDescription("circle", [point, point, point])
            self.assertTrue(False)
        except:
            pass

        try:
            CircleDescription("circle", [point, point2, point])
            self.assertTrue(False)
        except:
            pass


if __name__ == '__main__':
    unittest.main()
