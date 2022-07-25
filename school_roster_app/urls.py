from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("staff/", views.list_staff, name="list-staff"),
    path("staff/<int:employee_id>/", views.staff_detail, name="staff-detail"),
    path("students/", views.list_students, name="list-students"),
    path("students/<int:student_id>/", views.student_detail, name="student-detail"),
    path("students/add", views.student_add, name="student-add"),
]