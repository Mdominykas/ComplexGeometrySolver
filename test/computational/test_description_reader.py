import os
import unittest

from computational.descriptions.completed_descriptions import CompletedDescriptions
from computational.descriptions.description_reader import DescriptionReader
from computational.descriptions.description_writer import DescriptionWriter
from computational.descriptions.line_description import LineDescription
from computational.descriptions.point_description import PointDescription


class TestDescriptionReading(unittest.TestCase):
    def test_something(self):
        point1 = PointDescription("a")
        point2 = PointDescription("b")
        line = LineDescription("line", [point1, point2])
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
