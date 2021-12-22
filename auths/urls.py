from django.urls import path
from . import views, ajax_view


app_name = 'auths'

urlpatterns = [
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create_teacher_profile/', views.create_teacher_profile, name='create_teacher_profile'),
    path('display_teacher_profile/', views.display_teacher_profile, name='display_teacher_profile'),
    path('create_non_teacher_profile/', views.create_non_teacher_profile, name='create_non_teacher_profile'),
    path('display_non_teacher_profile/', views.display_non_teacher_profile, name='display_non_teacher_profile'),
    path('create_student_profile/', views.create_student_profile, name='create_student_profile'),
    path('display_student_profile/', views.display_student_profile, name='display_student_profile'),
    path('get_school_by_zone/', ajax_view.get_school_by_zone, name='get_school_by_zone'),
]