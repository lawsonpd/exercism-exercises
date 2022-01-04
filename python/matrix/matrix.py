class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(n) for n in sub.split()] for sub in matrix_string.splitlines()]

    def row(self, index:int) -> list:
        return [sub for sub in self.matrix[index-1]]

    def column(self, index:int) -> list:
        return [sub[index-1] for sub in self.matrix]
