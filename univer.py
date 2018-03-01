from abc import ABCMeta

class Course():
    def __init__(self, name, price):
        self.name = name
        self.teacher = None
        self.price = price

    def get_name(self):
        return self.name

    def add_teacher(self, teacher):
        self.teacher = teacher.get_name()

    def __str__(self):
        return ('\nCourse: {}  \nPrice: {} \nTeacher: {}').format(self.name, self.price, self.teacher)


class Group():
    def __init__(self, name):
        self.name = name
        self.teacher = None
        self.course  = None
        self.students = []

    def get_name(self):
        return self.name

    def add_teacher(self, teacher):
        self.teacher = teacher.get_name()

    def add_course(self, course):
        self.course = course.get_name()

    def add_student(self, student):
        self.students.append (student.get_name())

    def __str__(self):
        return ('\nGroup: {} \nCourse: {} \nTeacher: {}   \nStudents: {} ').format(self.name, self.course, self.teacher, self.students)


class Teacher():
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def get_name(self):
        return self.name


class Student():
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def get_name(self):
        return self.name


student_one = Student("Petrov Petr", 20, "C++")
student_two = Student("Ivanov Ivan", 22, "English")
student_three = Student("Maksimov Maksim", 23, "C++")
student_four = Student("Andreev Andrey", 21, "C++")
student_fife = Student("Romanov Roman", 23, "English")

teacher_one = Teacher("Linus Torvalds", ["C++","Java"])
teacher_two = Teacher("Grigoriev Grigoriy",["Sport","Money"]) 

course_one = Course( "C++", "666 $")
course_one.add_teacher(teacher_one)

group1 = Group("1")
group1.add_teacher(teacher_one)
group1.add_course(course_one)
group1.add_student(student_one)
group1.add_student(student_three)
group1.add_student(student_four)

print(course_one)
print(group1)

course_two = Course( "English", "9999 $")
course_two.add_teacher(teacher_two)

group2 = Group("2")
group2.add_teacher(teacher_two)
group2.add_course(course_two)
group2.add_student(student_two)
group2.add_student(student_fife)

print(course_two)
print(group2)
