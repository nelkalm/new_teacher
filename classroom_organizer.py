from roster import student_roster
import itertools


class ClassroomOrganizer:
    def __init__(self):
        self.sorted_names = self._sort_alphabetically(student_roster)

    def _sort_alphabetically(self, students):
        names = []
        for student_info in students:
            name = student_info['name']
            names.append(name)
        return sorted(names)

    def get_students_with_subject(self, subject):
        selected_students = []
        for student in student_roster:
            if student['favorite_subject'] == subject:
                selected_students.append((student['name'], subject))
        return selected_students

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.sorted_names):
            name = self.sorted_names[self.index]
            self.index += 1
            return name
        else:
            raise StopIteration

    def get_two_student_combo(self):
        return list(itertools.combinations(iter(self.sorted_names), 2))

    def get_math_science_fav_students(self):
        math_fav_students = self.get_students_with_subject('Math')
        science_fav_students = self.get_students_with_subject('Science')
        math_and_science_list = itertools.chain(
            iter(math_fav_students), iter(science_fav_students))
        return list(itertools.combinations(iter(math_and_science_list), 4))
