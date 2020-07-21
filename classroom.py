class Classroom:
    def __init__(self, name):
        self.name = name

    def read_students(self, filename):
        with open(filename) as f:
            for line in f:
                print('line:', line.strip())