import math
import numpy as np

Students=[] # List of tuples cuz we dont need to change anything
Courses=[]  # List of tuples ___
Marks={}    #Dict


def input_student():
    print('====STUDENT INPUT====')
    total_student = int(input("Number of students in class: "))
    for i in range(total_student):
        Students.append((input("Student name: "), int(input("Student ID: ")), input("DoB: ")))  # Appending each tuple
    
def input_course():
    print('====COURSE INPUT====')
    total_course = int(input("Number of courses: "))
    for i in range(total_course):
        # update: adding credit into Courses[2]
        Courses.append((input("Course name: "), int(input("Course ID: ")), int(input("Course credit: ")))) # Appending each tuple

def input_mark():
    print('====MARK INPUT====')
    course = input("Course name to mark students: ")
    for i in Courses:
        if course == i[0]:      # First element of tuple i = name
            Marks[course]={}     # Nested dict -> Marks{} contains every course names
            for j in Students:
                # * 10 to floor to correct first 2 digit. then / 10 to get correct decimal.
                mark = math.floor(float(input(f"{i[0]} mark for {j[0]}: ")) * 10) / 10  #j[0] = student name. i[0] = course name
                Marks[course][j[0]] = mark   # j[0] (student name) = Key, mark = value
            return
    print("Not found")
    
def list_student():
    print("STUDENT INFO:")
    for i in Students:
        print(f"Student name: {i[0]} - Student ID: {i[1]} - Student DoB: {i[2]}")   #Listing each Student (using tuplrs)

def list_course():
    print("COURSE INFO:")
    for i in Courses: # update: credit
        print(f"Course name: {i[0]}, Course ID: {i[1]}, Course credit: {i[2]}")    # Listing each Course
        
def student_marks():
    print("VIEWING MARKS:")
    course = input("Course name for viewing marks: ")   
    
    if course in Marks:
        for student_name in Marks[course]: # Loop through each student inside that course
            print(f"Student: {student_name}, Mark: {Marks[course][student_name]}")
    else:
        print("No marks found for this course")
    
# update: gpa calc func
def calc_gpa(student_name):

    # array for numpy
    marks = []
    credits = []
    
    for i in Courses:
        course_name = i[0] # tuple
        credit = i[2]
        
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
def get_gpa(student):
    return calc_gpa(student[0])

def student_ranking_gpa():
    print("=======GPA COMPUTING=======")
    ranked = sorted(
        Students, key=get_gpa, reverse=True # reverse = True cuz sorted() = asc
    )
    
    print("RANKED STUDENT BASE ON GPA: ")
    for i in ranked:
        gpa = calc_gpa(i[0])
        print(f"Name: {i[0]} - Student ID: {i[1]} - GPA: {gpa}")
    
    
    
    
    
input_student()
input_course()

for i in Courses:
    input_mark()

list_student()
list_course()
student_marks()

student_ranking_gpa()
