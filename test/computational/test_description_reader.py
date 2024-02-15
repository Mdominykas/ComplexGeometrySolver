import os
import unittest

from computational.descriptions.completed_descriptions import CompletedDescriptions
from computational.descriptions.description_reader import DescriptionReader
from computational.descriptions.description_writer import DescriptionWriter
from computational.descriptions.line_two_points_description import LineTwoPointsDescription
from computational.descriptions.point_free_description import PointFreeDescription


class TestDescriptionReading(unittest.TestCase):
    def test_something(self):
        point1 = PointFreeDescription("a")
        point2 = PointFreeDescription("b")
        line = LineTwoPointsDescription("line", [point1, point2])
        temporary_file_name = "temporary_file.txt"
        DescriptionWriter.write_descriptions(temporary_file_name, [point1, line])
        constructions = DescriptionReader.read_descriptions(temporary_file_name)

        completed_descriptions = CompletedDescriptions()
        output = []
        line.produce_code(completed_descriptions, output)
        self.assertEqual(DescriptionWriter.get_code_lines(constructions), output)
        os.remove(temporary_file_name)


if __name__ == '__main__':
    unittest.main()
