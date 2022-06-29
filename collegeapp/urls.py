from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('admin_login',views.admin_login,name="admin_login"),
    path('admin_home',views.admin_home,name="admin_home"),
    path('admin_logout',views.admin_logout,name="admin_logout"),
    path('add_course',views.add_course,name="add_course"),
    path('add_coursedb',views.add_coursedb,name="add_coursedb"),
    path('add_student',views.add_student,name="add_student"),
    path('add_studentdb',views.add_studentdb,name="add_studentdb"),
    path('show_details',views.show_details,name="show_details"),
    path('edit_page/<int:pk>',views.edit_page,name="edit_page"),
    path('edit_details/<int:pk>',views.edit_details,name="edit_details"),
    path('delete_page/<int:pk>',views.delete_page,name="delete_page"),
    path('teacher_signup',views.teacher_signup,name="teacher_signup"),
    path('add_teacherdb',views.add_teacherdb,name="add_teacherdb"),
    path('user_home',views.user_home,name="user_home"),
    path('edit',views.edit,name="edit"),
    path('profile',views.profile,name="profile"),
    path('show_teacher',views.show_teacher,name="show_teacher"),
    path('delete/<int:pk>',views.delete,name="delete")
]

