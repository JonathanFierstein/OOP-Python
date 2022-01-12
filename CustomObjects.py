class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


rolf = Student('Rolf', 'MIT')

rolf.marks.append(68)
rolf.marks.append(97)
rolf.marks.append(92)
rolf.marks.append(89)
rolf.marks.append(76)

print(rolf)
print(rolf.average)

