from django.shortcuts import render, redirect, reverse
from .models import School, Student, Staff # import our School class

my_school = School("Django School") # create a school instance

# Show link to view all staff and link to view all students
def index(request):
    content = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", content)

# Show all staff, and link to staff detail page
def list_staff(request):
    content = {
        "staff_list": my_school.staff,
    }
    return render(request, "pages/list_staff.html", content)

# Show all the staff data fields on page
def staff_detail(request, employee_id):
    employee = my_school.find_staff_by_id(employee_id)
    content = {
        "employee": employee, 
    }
    return render(request, "pages/staff_detail.html", content)

# list all students and link to students detail
def list_students(request):
    content = {
        "student_list": my_school.students,
    }
    return render(request, "pages/list_students.html", content)

# Show all student data fields
def student_detail(request, student_id):
    student = my_school.find_student_by_id(student_id)
    content = {
        "student": student,
    }
    return render(request, "pages/student_detail.html", content)

def student_add(request):
    if request.method == "POST":
        print(request.POST)

        input_data = {
            # key matches students data; value matches form data
            'name': request.POST['name'],
            'age': request.POST['age'],
            'school_id': request.POST['id'],
            'password': request.POST['password'],
            'role': 'student',
        }
        # creates new student instance
        new_student = Student(**input_data)

        # update school with new student
        my_school.add_student(new_student)
        return redirect(reverse('student-detail', args=[new_student.school_id]))

    return render(request, "pages/student_add.html")