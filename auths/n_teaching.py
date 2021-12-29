from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import NonTeachingStaff, NonTeachingSTaffFiles, Zone, School


@login_required
def create_non_teacher_profile(request):
    all_zones = Zone.objects.all()
    all_schools = School.objects.order_by('zone')
    context = {
        'all_zones': all_zones,
        'all_schools': all_schools
    }

    if request.method == 'POST':
        # get all data
        title = request.POST['title']
        middle_name = request.POST['middle_name']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        age = request.POST['age']
        address = request.POST['address']
        religion = request.POST['religion']
        phone_number = request.POST['phone_number']
        picture = request.FILES['picture']
        about_me = request.POST['about_me']
        designation = request.POST['designation']
        grade_level = request.POST['grade_level']
        first_appointment = request.POST['first_appointment']
        years_in_service = request.POST['years_in_service']
        qualification = request.POST['qualification']
        discipline = request.POST['discipline']
        current_posting_zone_id = request.POST['current_posting_zone']
        current_posting_school_id = request.POST['current_posting_school']
        previous_posting_1_id = request.POST['previous_posting_1']
        previous_posting_2_id = request.POST['previous_posting_2']
        previous_posting_3_id = request.POST['previous_posting_3']

        current_posting_zone = Zone.objects.get(id=current_posting_zone_id)
        current_posting_school = School.objects.get(id=current_posting_school_id)
        previous_posting_1 = School.objects.get(id=previous_posting_1_id)
        previous_posting_2 = School.objects.get(id=previous_posting_2_id)
        previous_posting_3 = School.objects.get(id=previous_posting_3_id)

        n_teacher = NonTeachingStaff.objects.get(user=request.user)
        n_teacher.title = title
        n_teacher.middle_name = middle_name
        n_teacher.picture = picture
        n_teacher.gender = gender
        n_teacher.date_of_birth = date_of_birth
        n_teacher.age = age
        n_teacher.address = address
        n_teacher.religion = religion
        n_teacher.phone_number = phone_number
        n_teacher.about_me = about_me
        n_teacher.designation = designation
        n_teacher.grade_level = grade_level
        n_teacher.first_appointment = first_appointment
        n_teacher.years_in_service = years_in_service
        n_teacher.qualification = qualification
        n_teacher.discipline = discipline
        n_teacher.current_posting_zone = current_posting_zone
        n_teacher.current_posting_school = current_posting_school
        n_teacher.previous_posting_1 = previous_posting_1
        n_teacher.previous_posting_2 = previous_posting_2
        n_teacher.previous_posting_3 = previous_posting_3
        n_teacher.save()

        images = request.FILES.getlist('documents')
        #document_title = request.POST.getlist('document_title')

        for image in images:
            fs = FileSystemStorage()
            file_path = fs.save(image.name, image)

            teacher_files = NonTeachingSTaffFiles(user=n_teacher, documents=file_path)
            teacher_files.save()

        return redirect('/auths/display_non_teacher_profile/')
    return render(request, 'auths/create_non_teacher.html', context)


@login_required
def display_non_teacher_profile(request):
    n_teacher = NonTeachingStaff.objects.get(user=request.user)
    n_teacher_file = NonTeachingSTaffFiles.objects.filter(user=n_teacher)
    # count_files = len(teacher_file)

    if n_teacher.middle_name is None:
        messages.info(request, 'You have no profile yet. Please create your profile.')
        return HttpResponseRedirect('/auths/create_non_teacher_profile/')
    else:
        context = {
            'username': request.user.username, 'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email, 'status': request.user.status, 'file_no': request.user.file_no,
            'unique_id': request.user.unique_id, 'middle_name': n_teacher.middle_name, 'title': n_teacher.title,
            'picture': n_teacher.picture, 'gender': n_teacher.gender, 'date_of_birth': n_teacher.date_of_birth,
            'age': n_teacher.age, 'address': n_teacher.address, 'religion': n_teacher.religion,
            'phone_number': n_teacher.phone_number,
            'about_me': n_teacher.about_me, 'created_date': n_teacher.created_date, 'designation': n_teacher.designation,
            'grade_level': n_teacher.grade_level, 'first_appointment': n_teacher.first_appointment,
            'years_in_service': n_teacher.years_in_service, 'qualification': n_teacher.qualification,
            'discipline': n_teacher.discipline,
            'published_work': n_teacher.published_work, 'current_posting_zone': n_teacher.current_posting_zone,
            'current_posting_school': n_teacher.current_posting_school, 'previous_posting_1': n_teacher.previous_posting_1,
            'previous_posting_2': n_teacher.previous_posting_2, 'previous_posting_3': n_teacher.previous_posting_3,
            'current_subject': n_teacher.current_subject, 'previous_subjects': n_teacher.previous_subjects,
        }
        return render(request, 'auths/display_non_teacher.html', context)


@login_required
def update_non_teacher_profile(request):
    teacher = NonTeachingStaff.objects.get(user=request.user)
    all_zones = Zone.objects.all()
    all_schools = School.objects.order_by('zone')
    context = {
        'teacher': teacher,
        'all_zones': all_zones,
        'all_schools': all_schools
    }

    if request.method == 'POST':
        title = request.POST['title']
        middle_name = request.POST['middle_name']
        gender = request.POST['gender']
        age = request.POST['age']
        address = request.POST['address']
        religion = request.POST['religion']
        phone_number = request.POST['phone_number']
        about_me = request.POST['about_me']
        designation = request.POST['designation']
        grade_level = request.POST['grade_level']
        years_in_service = request.POST['years_in_service']
        qualification = request.POST['qualification']
        discipline = request.POST['discipline']
        previous_posting_1_id = request.POST['previous_posting_1']
        previous_posting_2_id = request.POST['previous_posting_2']
        previous_posting_3_id = request.POST['previous_posting_3']

        previous_posting_1 = School.objects.get(id=previous_posting_1_id)
        previous_posting_2 = School.objects.get(id=previous_posting_2_id)
        previous_posting_3 = School.objects.get(id=previous_posting_3_id)

        y = teacher.picture
        picture = None
        try:
            if request.FILES['picture']:
                picture = request.FILES['picture']
        except:
            picture = None

        # change date format to yyyy-mm-dd for date of birth
        x = teacher.date_of_birth
        reg = x.strftime('%Y-%m-%d')

        # change date format to yyyy-mm-dd for date of appointment
        d = teacher.first_appointment
        d_reg = d.strftime('%Y-%m-%d')

        teacher.title = title
        teacher.middle_name = middle_name
        teacher.gender = gender

        try:
            if request.POST['update_date_of_birth']:
                updated_date = request.POST['update_date_of_birth']
                teacher.date_of_birth = updated_date
        except:
            teacher.date_of_birth = reg

        if picture is None:
            teacher.picture = y
        else:
            teacher.picture = picture

        teacher.age = age
        teacher.address = address
        teacher.religion = religion
        teacher.phone_number = phone_number
        teacher.about_me = about_me
        teacher.designation = designation
        teacher.grade_level = grade_level

        try:
            if request.POST['update_first_appointment']:
                update_first_appointment = request.POST['update_first_appointment']
                teacher.first_appointment = update_first_appointment
        except:
            teacher.first_appointment = d_reg

        teacher.years_in_service = years_in_service
        teacher.qualification = qualification
        teacher.discipline = discipline

        try:
            if request.POST['current_posting_zone'] and request.POST['current_posting_school']:
                if request.POST['current_posting_zone'] == None and request.POST['current_posting_school'] == None:
                    teacher.current_posting_zone = teacher.current_posting_zone
                    teacher.current_posting_school = teacher.current_posting_school
                else:
                    current_posting_zone = Zone.objects.get(id=request.POST['current_posting_zone'])
                    current_posting_school = School.objects.get(id=request.POST['current_posting_school'])
                    teacher.current_posting_zone = current_posting_zone
                    teacher.current_posting_school = current_posting_school
        except:
            teacher.current_posting_zone = teacher.current_posting_zone
            teacher.current_posting_school = teacher.current_posting_school
        teacher.previous_posting_1 = previous_posting_1
        teacher.previous_posting_2 = previous_posting_2
        teacher.previous_posting_3 = previous_posting_3
        teacher.save()
        return redirect('/auths/display_non_teacher_profile/')
    return render(request, 'auths/update_non_teacher.html', context)