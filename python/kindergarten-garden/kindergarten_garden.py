students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid',
            'Larry']
plants = {'C': 'Clover', 'G': 'Grass', 'R': 'Radishes', 'V': 'Violets'}


class Garden:
    def __init__(self, diagram, students=students):
        self.garden = [list(x) for x in diagram.split()]
        self.students = sorted(students)

    def plants(self, student):
        start_index = self.students.index(student) * 2
        front_row = [plants[x] for x in self.garden[0][start_index:start_index + 2]]
        second_row = [plants[x] for x in self.garden[1][start_index:start_index + 2]]
        return front_row + second_row
