from student import Student

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def read_students(self, filename):
        with open(filename) as f:
            for line in f:
                name, grade = line.strip().split(', ')
                grade = float(grade)

                if name in self.students:
                    s = self.students[name]
                    s.grades.append(grade)
                else:
                    s = Student(name)
                    s.grades.append(grade)
                    self.students[name] = s
                
    def calculate_averages(self):
        for name in self.students:
            s = self.students[name]
            s.update()
    
    def best(self):
        return max(self.students, key=lambda n: self.students[n].average)