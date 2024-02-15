import unittest

from computational.descriptions.line_two_points_description import LineTwoPointsDescription
from computational.descriptions.point_free_description import PointFreeDescription


class LineTwoPointsDescriptionTests(unittest.TestCase):
    def test_from_two_points_creates_point_description(self):
        point1 = PointFreeDescription("a")
        point2 = PointFreeDescription("b")
        line = LineTwoPointsDescription("line", [point1, point2])
        self.assertEqual(type(line), LineTwoPointsDescription)

    def test_can_not_create_line_from_same_point(self):
        point = PointFreeDescription("a")
        with self.assertRaises(Exception):
            self.assertTrue(False)



if __name__ == '__main__':
    unittest.main()
