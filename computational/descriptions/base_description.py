from computational.descriptions.completed_descriptions import CompletedDescriptions


class BaseDescription:
    def __init__(self, name, code_line, dependencies):
        self.name = name
        self.code_line = code_line
        self.dependencies = dependencies

    def produce_code(self, completed_descriptions: CompletedDescriptions, output: list):
        if completed_descriptions.is_completed(self.name):
            return
        for dep in self.dependencies:
            if not completed_descriptions.is_completed(dep):
                dep.produce_code(completed_descriptions, output)
        output.append(self.code_line)
        completed_descriptions.complete(self.name)



