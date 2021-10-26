class Students:
    
    def __init__(self, name, grades):

        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Students("Thiago",(1,2,3,4))

print(student.average_grade())