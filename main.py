from classroom import Classroom

physics = Classroom(name='physics')

physics.read_students('grades.csv')

for student in physics.students:
    print(student)

