from collections import defaultdict
class School:
    def __init__(self):
        self.students = defaultdict(list)

    def add_student(self, name, grade):
        self.students[grade].append(name)

    def roster(self):
        res = []
        for grade in sorted(self.students.keys()):
            res.extend(sorted(self.students[grade]))
        return res

    def grade(self, grade_number):
        return sorted(self.students[grade_number])
