from classroom import Classroom

physics = Classroom(name='physics')

physics.read_students('grades.csv')

physics.calculate_averages()

for name in physics.students:
    s = physics.students[name]
    print(s)

best = physics.best()
print('best: ', best)

