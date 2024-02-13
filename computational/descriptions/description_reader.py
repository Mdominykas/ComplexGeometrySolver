from computational.Parser import Parser
from computational.descriptions.all_descriptions import AllDescriptions


class DescriptionReader:
    @staticmethod
    def parse_arguments(template, line):
        pass

    @staticmethod
    def read_descriptions(filename):
        constructions = []
        parser = Parser()
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                parsed_object = parser.parse(line)
                if parsed_object is None:
                    raise Exception("Failed to read line: \"{}\"".format(line))
                constructions.append(parsed_object)
        return constructions
