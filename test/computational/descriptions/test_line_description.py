import unittest

from computational.descriptions.line_description import LineDescription
from computational.descriptions.point_description import PointDescription


class LineDescriptionTests(unittest.TestCase):
    def test_from_two_points_creates_point_description(self):
        point1 = PointDescription("a")
        point2 = PointDescription("b")
        line = LineDescription("line", [point1, point2])
        self.assertEqual(type(line), LineDescription)

    def test_can_not_create_line_from_same_point(self):
        point = PointDescription("a")
        try:
            line = LineDescription("line", [point, point])
            self.assertTrue(False)
        except:
            pass



if __name__ == '__main__':
    unittest.main()
