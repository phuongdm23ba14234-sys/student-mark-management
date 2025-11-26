def number_of_students () :
    n = int (input ("Enter number of students: "))
    return n

def inf_of_students (n) :
    students = []
    for i in range (n) :
        print ("Enter information of student")
        id = input ("Enter ID: ")
        name = input ("Enter Name: ")
        dob = input ("Enter Date of Birth: ")
        students.append({"id": id, "name": name, "dob": dob})
    return students

def number_of_courses () :
    m = int(input ("Enter number of courses: "))
    return m

def inf_of_courses (m) :
    course = []
    for i in range (m) :
        print ("Enter information of course")
        cid = input ("Enter ID of course :")
        cname = input ("Enter Name of course:")
        course.append ({"id": cid, "name": cname })
    return course

def inputmark(students, courses):
    
    print("Available courses:")
    for i, course in enumerate(courses):
        print(f"{i+1}. {course['name']} (ID: {course['id']})")
    
    cindex = int(input("Choose course by number: ")) - 1
    selected_course = courses[cindex]
    
    marks = {}
    for student in students:
        m = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
        marks[student['id']] = m
    
    return selected_course['id'], marks


def list_course (course)  :
    print ("List of courses:")
    for course in course :
        print (f"{course ['id']} : {course ['name']}")
    return

def list_students (students) :
    print ("List of students:")
    for student in students :
        print (f"{student ['id']} : {student ['name']} : {student ['dob']}")
    return

def show_marks(course_id, marks, students):
    print(f"Marks for course ID {course_id}:")
    for student in students:
        if student['id'] in marks:
            print(f"{student['name']} (ID: {student['id']}): {marks[student['id']]}")
    return

def main () :
    n = number_of_students()
    students = inf_of_students(n)
    m = number_of_courses()
    courses = inf_of_courses(m)

    while True:
        print("\nMenu:")
        print("1. List students")
        print("2. List courses")
        print("3. Input marks for a course")
        print("4. Show marks for a course")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            list_students(students)
        elif choice == '2':
            list_course(courses)
        elif choice == '3':
            course_id, marks = inputmark(students, courses)
        elif choice == '4':
            if 'marks' in locals() and 'course_id' in locals():
                show_marks(course_id, marks, students)
            else:
                print("No marks available. Please input marks first.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
            
            
if __name__ == "__main__":
    main()

        


