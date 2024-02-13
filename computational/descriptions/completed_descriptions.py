class CompletedDescriptions:
    def __init__(self):
        self.completed = set()

    def complete(self, name):
        assert(not self.is_completed(name))
        self.completed.add(name)

    def is_completed(self, name):
        return name in self.completed
