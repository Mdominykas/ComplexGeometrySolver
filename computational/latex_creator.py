import os
import subprocess
import uuid


class LatexCreator:
    def __init__(self):
        # in the future I might need to add types to elements or use enums to facilitate development of features
        self.elements = []
        self.add_standard_header()
        self.is_completed = False
        self.tex_file_name = None

    def produce_latex_code(self):
        if not self.is_completed:
            self.add_standard_footer()
        result = "\n\n".join(self.elements)
        return result

    def add_standard_header(self):
        self.elements.append("\\documentclass{article}\n\n\\begin{document}")

    def add_standard_footer(self):
        self.is_completed = True
        self.elements.append("\\end{document}")

    def add_expression(self, expression):
        assert not self.is_completed, "Cannot add expression after footer has been added"
        self.elements.append("\\[" + expression.to_latex_string() + "\\]")

    def compile_to_pdf(self, pdf_file_name):
        assert not pdf_file_name.endswith(".pdf"), ("pdf filename should not end with .pdf as this"
                                                    "will be appended automatically")
        if not self.is_completed:
            self.add_standard_footer()

        code = self.produce_latex_code()
        directory_name = os.path.dirname(pdf_file_name)
        creatable_file_name = pdf_file_name + "_latex_" + str(uuid.uuid4())
        tex_file_name = creatable_file_name + ".tex"
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!TEX_FILE_NAME = ", tex_file_name)
        with open(tex_file_name, 'w') as file:
            file.write(code)
        self.tex_file_name = tex_file_name
        ret = os.system(f"cd {directory_name} && pdflatex {tex_file_name}")
        assert ret == 0, "Pdf compilation failed"

        created_pdf_file_name = creatable_file_name + ".pdf"
        pdf_file_name = pdf_file_name + ".pdf"

        print(f"rasysiu: mv {created_pdf_file_name} {pdf_file_name}")
        ret = os.system(f"mv {created_pdf_file_name} {pdf_file_name}")
        assert ret == 0, "Copying of pdf file failed"

    def remove_compilation_file(self):
        assert self.tex_file_name is not None, "Can not remove file that has no name"
        os.remove(self.tex_file_name)
