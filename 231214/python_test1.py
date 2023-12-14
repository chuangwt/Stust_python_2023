class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

def add_course(self, course_code, course_name, semester):
        if semester not in self.courses:
            self.courses[semester] = []
        self.courses[semester].append({"code": course_code, "name": course_name})
 
def query_course_info(self, semester):
        if semester in self.courses:
            courses_in_semester = self.courses[semester]
            return f"Courses taken by {self.name} in {semester}:", courses_in_semester
        else:
            return f"No courses found for {self.name} in semester {semester}.", None






obj1 = Student("大A", "S011", "資工")
obj2 = Student("小b", "S002", "電機")
print (obj1.name, obj2.name)