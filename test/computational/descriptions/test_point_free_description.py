import unittest

from computational.descriptions.point_free_description import PointFreeDescription


class PointFreeDescriptionTests(unittest.TestCase):
    def test_from_free_creates_point_description(self):
        point = PointFreeDescription("a")
        self.assertEqual(type(point), PointFreeDescription)


if __name__ == '__main__':
    unittest.main()
