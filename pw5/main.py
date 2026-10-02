import zipfile
import os
import input
import output

def decompress():
    with zipfile.ZipFile("students.dat", "r") as archive:
        archive.extractall()
        
def compress():
    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as archive:
        archive.write("students.txt")
        archive.write("courses.txt")
        archive.write("marks.txt")
        
if os.path.exists("students.dat"):
    decompress()
    students = input.load_student()
    courses = input.load_course()
    Marks = input.load_mark()
else:
    Marks = {}
    students = input.input_student()
    courses = input.input_course()

    for i in courses: # cuz Marks{} is created here -> we can overwrite marks.txt
        input.input_mark(courses, students, Marks)

output.list_student(students)
output.list_course(courses)
output.student_marks(Marks)
output.student_ranking_gpa(students, courses, Marks)

# Save current data
compress()
