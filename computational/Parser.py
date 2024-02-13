from computational.descriptions.all_descriptions import AllDescriptions


class Parser:
    PLACEHOLDER = "{}"

    def __init__(self):
        self.context = {}

    # very basic division, since I want to do simple language and as
    # quickly as possible
    @staticmethod
    def divide_to_lexemes(line):
        special_chars = ['=', '(', ')', ',', '.']
        split_chars = [' ', '\t']
        lexemes = []
        cur = []

        def append_cur(cr, lex):
            if len(cr) > 0:
                lex.append(''.join(cr))
            cr.clear()

        for c in line:
            if c in split_chars:
                append_cur(cur, lexemes)
            elif c in special_chars:
                append_cur(cur, lexemes)
                lexemes.append(''.join([c]))
            else:
                cur.append(c)
        append_cur(cur, lexemes)
        return lexemes

    @staticmethod
    def can_parse(template, line):
        line_parts, template_parts = Parser.divide_to_lexemes(line), Parser.divide_to_lexemes(template)
        if len(line_parts) != len(template_parts):
            return False
        for (line_part, template_part) in zip(line_parts, template_parts):
            if line_part != template_part and template_part != Parser.PLACEHOLDER:
                return False
        return True

    @staticmethod
    def parse_arguments(template, line):
        assert(Parser.can_parse(template, line))
        arguments = []
        line_parts, template_parts = Parser.divide_to_lexemes(line), Parser.divide_to_lexemes(template)
        for (line_part, template_part) in zip(line_parts, template_parts):
            if template_part == Parser.PLACEHOLDER:
                arguments.append(line_part)
        return arguments

    def parse(self, line):
        for description in AllDescriptions.get_all_descriptions():
            if self.can_parse(description.code_line_template, line):
                arguments = self.parse_arguments(description.code_line_template, line)
                name = arguments[0]
                arguments = arguments[1:]
                name_not_found = False
                for arg in arguments:
                    if arg not in self.context:
                        name_no_found = True
                if name_not_found:
                    return None
                dependencies = [self.context[arg] for arg in arguments]
                construction = description(name, dependencies)
                self.context[name] = construction
                return construction
