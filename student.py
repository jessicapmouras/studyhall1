class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.average = 0
    
    def __str__(self):
        return "{} {} {}".format(self.name, self.grades, self.average)
    def __repr__(self):
        return self.__str__()
    
    def update(self):
        self.average = sum(self.grades) / len(self.grades)

