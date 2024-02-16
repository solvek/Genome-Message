import os
from nucleotide import nucleotide2code

class GenomeReader:

    def __init__(self, path):
        self.size = os.path.getsize(path)
        self.file = open(path, "r")
        self.line = 0
        self.column = 0
        self.is_head = True

    def __iter__(self):
        for n, raw in enumerate(self.file):
                self.line = n
                if raw[0]==">":
                    self.is_head = True
                    continue
                for i, ch in enumerate(raw):
                    if ord(ch) == 10:
                        continue
                    c = nucleotide2code(ch)
                    if c is None:
                        self.is_head = True
                    else:
                        self.column = i
                        yield c
                        self.is_head = False

