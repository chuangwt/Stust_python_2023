class Student:
    def __init__(self, school, department, Department_Chair, name, id, address, credits, gpa):
        self.school = school
        self.department = department
        self.Department_Chair = Department_Chair
        self.name = name
        self.id = id
        self.address = address
        self.credits = credits
        self.gpa = gpa

    def getSchool(self):
        return self.school
    def setSchool(self, value):
        self.school = value

p = Student ("南台科技大學","資訊工程系", "王一", "莊惟婷", "4B0G0178", "南台街1號", "125", "5%")

print (p.getSchool())
p.setSchool("南應科技大學")
print(p.getSchool())