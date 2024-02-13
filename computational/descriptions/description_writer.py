from computational.descriptions.completed_descriptions import CompletedDescriptions


class DescriptionWriter:
    @staticmethod
    def get_code_lines(descriptions):
        completed = CompletedDescriptions()
        output = []

        for description in descriptions:
            description.produce_code(completed, output)
        return output

    @staticmethod
    def write_descriptions(filename, descriptions):
        code = DescriptionWriter.get_code_lines(descriptions)

        with open(filename, 'w') as file:
            for line in code:
                file.write(line + "\n")

