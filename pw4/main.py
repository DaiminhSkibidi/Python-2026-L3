import input
import output

Marks = {}
students = input.input_student()
courses = input.input_course()

for i in courses:
    input.input_mark(courses, students, Marks)

output.list_student(students)
output.list_course(courses)
output.student_marks(Marks)
output.student_ranking_gpa(students, courses, Marks)
