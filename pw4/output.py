from domains.student import Student
from domains.course import Course
import numpy as np

def list_student(students):
    print('====STUDENTS INFO====')
    
    for i in students:
        print(f"Student name: {i.name} - Student ID: {i.student_id} - DoB: {i.dob}")
        
def list_course(courses):
    print('====COURSES INFO====')
    
    for i in courses:
        print(f"Course name: {i.name} - Course ID: {i.course_id} - Credits: {i.credit}")
        
def student_marks(Marks):
    print("VIEWING MARKS:")
    course = input("Course name for viewing marks: ")   
    
    if course in Marks:
        for student_name in Marks[course]: # Loop through each student inside that course
            print(f"Student: {student_name}, Mark: {Marks[course][student_name]}")
    else:
        print("No marks found for this course")
    
def calc_gpa(student_name, courses, Marks):

    # array for numpy
    marks = []
    credits = []
    
    for i in courses:
        course_name = i.name # obj
        credit = i.credit
        
        if course_name in Marks: # Check if course exist
            if student_name in Marks[course_name]: # check if student exist
                marks.append(Marks[course_name][student_name]) # append student's mark
                credits.append(credit) # student's credit
                
    # check if marks = 0
    if len(marks) == 0:
            return 0
        
    # convert to numpy arrays
    marks = np.array(marks)
    credits = np.array(credits)
    
    # calculate the GPA (weighted)
    return np.sum(marks * credits) / np.sum(credits) # gpa = sum of (mark * credit) / sum of credits

# tiny func for ranking gpa func
def get_gpa(student, courses, Marks):
    return calc_gpa(student.name, courses, Marks)

def student_ranking_gpa(students, courses, Marks):
    print("=======GPA COMPUTING=======")
    ranked = sorted(
        students, 
        key = lambda student: get_gpa(student, courses, Marks), # lambda = tiny func: etc(student): return getgpa
        reverse = True
    )
    
    print("RANKED STUDENT BASE ON GPA: ")
    for i in ranked:
        gpa = calc_gpa(i.name, courses, Marks)
        print(f"Name: {i.name} - Student ID: {i.student_id} - GPA: {gpa}")
