class GenomeFile:
    def __init__(self, path, mode):
        self.file = open(path, mode)
        self.mode = mode

    def close(self):
        pass