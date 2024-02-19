import string


class PointNamer:
    def __init__(self):
        self.single_letter = list(map(str, list(string.ascii_uppercase)))
        print(self.single_letter)
        self.two_letter = [a + b for a in self.single_letter for b in self.single_letter]
        print(self.two_letter)

    def get_name(self):
        if len(self.single_letter) > 0:
            return self.single_letter.pop(0)
        assert (len(self.two_letter) > 0)
        return self.two_letter.pop(0)
