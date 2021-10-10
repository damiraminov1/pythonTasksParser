import os
from docx import Document
from pathlib import Path

SAVE_PATH = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).joinpath('Documents')


class Saver:
    def __init__(self):
        if not SAVE_PATH.exists():
            os.mkdir(SAVE_PATH)

    def save_to_docx(self, filename: str, text: list):
        document = Document()
        for paragraph in range(1, 37):
            document.add_paragraph(text=text[paragraph])
        document.save(SAVE_PATH.joinpath(filename + '.docx'))
        return True
