class Unifersity:
    def __init__(self,name):
        self.name=name
        self.course=[]
        self.student=[]

    def add_student(self,student):
        self.student.append(student)

    def add_course(self,course):
        self.course.append(course)

    def add_student_course(self,student,course):
        student.enroll_course(course)

    def get_info_student(self):
        lst = [st.name for st in self.student]
        return f'{self.name} есть студенты: {", ".join(lst)}'

    def get_info_course(self):
        lst = [st.course_name for st in self.course]
        return f'{self.name} есть курсы: {", ".join(lst)}'

    def get_info(self):
        lst1 = [st.course_name for st in self.course]
        lst2 = [st.name for st in self.student]
        return f'{self.name} есть курсы: {", ".join(lst1)}, студенты: {", ".join(lst2)}'
class Course:
    CODE=0
    def __init__(self, name,hours):
        global UNIFERSITY
        Course.CODE+=1
        self.course_code=Course.CODE
        self.course_name=name
        self.course_hours=hours
        self.course_student=[]
        UNIFERSITY.add_course(self)


    def add_student(self,student):
        if not student in self.course_student:
           self.course_student.append(student)

    def get_info(self):
        lst=[st.name for st in self.course_student]
        return f'курс: {self.course_name}, кол-во часов: {self.course_hours}, студенты: {", ".join(lst)}'
class Student:
    ID=0
    def __init__(self,name):
        global UNIFERSITY
        Student.ID+=1
        self.id=Student.ID
        self.name=name
        self.enrolled_courses=[]
        UNIFERSITY.add_student(self)

    def __str__(self):
        return f'{self.name}'
    def enroll_course(self,course):
        if not course in self.enrolled_courses:
           self.enrolled_courses.append(course)
           course.add_student(self)

    def get_info(self):
        lst = [st.course_name for st in self.enrolled_courses]
        return f'Студент: {self.name}, курсы: {", ".join(lst)}'


UNIFERSITY=Unifersity('Академия')

kurs1=Course('python',250)
kurs2=Course('java',200)

stud1=Student('Я')
stud1.enroll_course(kurs1)
UNIFERSITY.add_student_course(stud1,kurs2)
print(stud1.get_info())
print(kurs1.get_info())
print(UNIFERSITY.get_info())