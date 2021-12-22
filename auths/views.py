from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Zone, School, TeachingSTaff, TeachingSTaffFiles

# Create your views here.

User = get_user_model()


def home(request):
    return render(request, 'auths/base.html')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        file_no = request.POST['file_no']
        status = request.POST['status']
        password = request.POST['password']
        password2 = request.POST['password2']

        # validate username
        check_users = ['admin', 'css', 'js', 'authenticate', 'login', 'logout', 'administrator', 'root', 'email',
                       'user', 'join', 'sql', 'static', 'python', 'delete', 'sex', 'sexy']

        if username in check_users:
            messages.error(request, 'Your Username, ' + username + ', Is Not Acceptable. Please Use Another Username')
            return render(request, 'auths/user_signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Your Username, ' + username + ', Already Exists. Please Try Another Username')
            return render(request, 'auths/user_signup.html')

        # validate email
        email = email.strip().lower()
        if ("@" not in email) or (email[-4:] not in ".com.org.edu.gov.net"):
            messages.error(request, 'Your Email, ' + email + ', Is Invalid!!!')
            return render(request, 'auths/user_signup.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Your Email, ' + email + ', Already Exists. Please Try Another Email')
            return render(request, 'auths/user_signup.html')

        # validate password
        if password != password2:
            messages.error(request, "Your Passwords Don't match")
            return render(request, 'auths/user_signup.html')

        User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name,
                                 status=status, file_no=file_no)
        user = User.objects.get(username=username)

        context = {
            'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name, 'status': status,
            'file_no': file_no, 'unique_id': user.unique_id
        }
        return render(request, 'auths/signup_success.html', context)
    return render(request, 'auths/user_signup.html')


# login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'This Username, ' + username + ', Does Not Exist...')
            return render(request, 'auths/login.html')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    print(request.user.status)
                    if request.user.is_superuser:
                        return redirect('/auths/display_teacher_profile/')
                    if request.user.status == 'administrator':
                        return redirect('/auths/display_teacher_profile/')
                    elif request.user.status == 'staff - teaching':
                        return redirect('/auths/display_teacher_profile/')
                    elif request.user.status == 'staff - non-teaching':
                        return redirect('/auths/display_non_teacher_profile/')
                    elif request.user.status == 'student':
                        return redirect('/auths/display_student_profile/')
    return render(request, 'auths/login.html')


# logout view
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def create_teacher_profile(request):
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
        current_posting_zone = request.POST['current_posting_zone']
        current_posting_school = request.POST['current_posting_school']
        published_work = request.POST['published_work']
        current_subject = request.POST['current_subject']
        previous_posting_1 = request.POST['previous_posting_1']
        previous_posting_2 = request.POST['previous_posting_2']
        previous_posting_3 = request.POST['previous_posting_3']
        previous_subjects = request.POST['previous_subjects']

        print(current_posting_zone)

        images = request.FILES.getlist('documents')

        teacher = TeachingSTaff(
            title=title, middle_name=middle_name, picture=picture, gender=gender, date_of_birth=date_of_birth, age=age,
            address=address, religion=religion, phone_number=phone_number, about_me=about_me, designation=designation,
            grade_level=grade_level, first_appointment=first_appointment, years_in_service=years_in_service,
            qualification=qualification, discipline=discipline, published_work=published_work,
            current_posting_zone=current_posting_zone, current_posting_school=current_posting_school,
            previous_posting_1=previous_posting_1, previous_posting_2=previous_posting_2, previous_posting_3=previous_posting_3,
            current_subject=current_subject, previous_subjects=previous_subjects
        )
        teacher.save()

        for image in images:
            fs = FileSystemStorage()
            file_path = fs.save(image.name, image)

            teacher_files = TeachingSTaffFiles(user=teacher, documents=file_path)
            teacher_files.save()

        return redirect('/auths/display_teacher_profile/')

    return render(request, 'auths/create_teacher_profile.html', context)


@login_required
def display_teacher_profile(request):
    teacher = TeachingSTaff.objects.get(user=request.user)
    teacher_file = TeachingSTaffFiles.objects.filter(user=teacher)

    if teacher.middle_name is None:
        messages.info(request, 'You have no profile yet. Please create your profile.')
        return HttpResponseRedirect('/auths/create_teacher_profile/')
    else:
        context = {

        }
        return render(request, 'auths/display_teacher_profile.html', context)


def create_non_teacher_profile(request):
    pass


def display_non_teacher_profile(request):
    pass


def create_student_profile(request):
    pass


def display_student_profile(request):
    pass
'''
# user Profile
def user_profile(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'users/user_profile.html', {'user': user})



'''