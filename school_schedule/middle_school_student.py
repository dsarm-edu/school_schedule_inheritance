from .student import Student


class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def summary(self):
        first_line = super().summary()
        second_line = f"{self.name} gets transportation: {self.gets_transportation}"
        return f"{first_line} {second_line}" 
        # this combines summary from student.py + MiddleSchool 