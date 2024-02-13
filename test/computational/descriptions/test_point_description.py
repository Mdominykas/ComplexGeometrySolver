import unittest

from computational.descriptions.point_description import PointDescription


class PointDescriptionTests(unittest.TestCase):
    def test_from_free_creates_point_description(self):
        point = PointDescription("a")
        self.assertEqual(type(point), PointDescription)


if __name__ == '__main__':
    unittest.main()
