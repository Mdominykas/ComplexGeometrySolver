import unittest

from computational.descriptions.point_free_description import PointFreeDescription
from computational.descriptions.point_from_segment_ratio_description import PointFromSegmentRatioDescription


class PointFromSegmentRatioTest(unittest.TestCase):
    def test_correct_construction(self):
        a = PointFreeDescription("a")
        b = PointFreeDescription("b")
        c = PointFromSegmentRatioDescription("c", [a, b, 2, 3])
        self.assertTrue(c.is_point())

    def test_incorrect_construction_when_passed_float(self):
        a = PointFreeDescription("a")
        b = PointFreeDescription("b")
        with self.assertRaises(Exception):
            PointFromSegmentRatioDescription("c", [a, b, 2, 3.5])


if __name__ == '__main__':
    unittest.main()
