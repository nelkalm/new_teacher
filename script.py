from roster import student_roster
from classroom_organizer import ClassroomOrganizer

student_roster_iterator = iter(student_roster)

for _ in range(10):
    print(next(student_roster_iterator))

my_class = ClassroomOrganizer()
for student in my_class:
    print(student)

print(my_class.get_two_student_combo())
print(my_class.get_math_science_fav_students())
