from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Student, StudentFiles, School, Class, Level, Department


@login_required
def create_student_profile(request):
    all_schools = School.objects.order_by('name')
    all_departments = Department.objects.order_by('department')
    all_classes = Class.objects.order_by('name')
    all_levels = Level.objects.order_by('level')


    context = {
        'all_schools': all_schools,
        'all_departments': all_departments,
        'all_classes': all_classes,
        'all_levels': all_levels,
    }
    return render(request, 'auths/create_student_profile.html', context)


@login_required
def display_student_profile(request):
    student = Student.objects.get(user=request.user)
    student_file = StudentFiles.objects.filter(user=student)

    if student.middle_name is None:
        messages.info(request, 'You have no profile yet. Please create your profile.')
        return HttpResponseRedirect('/auths/create_student_profile/')
    else:
        context = {

        }
        return render(request, 'auths/display_student_profile.html', context)


