# Generated by Django 4.0 on 2021-12-21 13:17

import auths.models
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('unique_id', models.CharField(default=auths.models.random_code, max_length=10, unique=True)),
                ('status', models.CharField(choices=[('administrator', 'administrator'), ('staff - teaching', 'staff - teaching'), ('staff - non-teaching', 'staff - non-teaching'), ('student', 'student')], default=('administrator', 'administrator'), max_length=20)),
                ('file_no', models.CharField(max_length=100, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NonTeachingStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs')], max_length=10, null=True)),
                ('middle_name', models.CharField(help_text='Enter your middle name here if any', max_length=25, null=True)),
                ('picture', models.ImageField(null=True, upload_to='Non_Teachers_Photo/%Y/%m/%d/')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('date_of_birth', models.DateField(help_text='Format: YYYY-MM-DD', null=True)),
                ('age', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('religion', models.CharField(choices=[('Christianity', 'Christianity'), ('Islam', 'Islam')], max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('about_me', models.TextField(help_text='Write something about yourself, not more than 300 words', max_length=300, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('designation', models.CharField(choices=[('Office Assistant', 'Office Assistant'), ('Secretary', 'Secretary'), ('Librarian', 'Librarian'), ('Others', 'Others')], max_length=100)),
                ('grade_level', models.CharField(help_text='E.g, Level 8 Step 2', max_length=20)),
                ('first_appointment', models.DateField(blank=True, null=True)),
                ('years_in_service', models.CharField(max_length=15, null=True)),
                ('qualification', models.CharField(choices=[('SSCE', 'SSCE'), ('OND', 'OND'), ('HND', 'HND'), ('PGDE', 'PGDE'), ('B.Sc', 'B.Sc'), ('B.Arts', 'B.Arts')], max_length=10, null=True)),
                ('discipline', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Non Teaching Staff',
                'verbose_name_plural': 'Non Teaching Staffs',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(help_text='Enter your middle name here if any', max_length=25, null=True)),
                ('picture', models.ImageField(null=True, upload_to='Student_Photo/%Y/%m/%d/')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('date_of_birth', models.DateField(help_text='Format: YYYY-MM-DD', null=True)),
                ('age', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('religion', models.CharField(choices=[('Christianity', 'Christianity'), ('Islam', 'Islam')], max_length=20, null=True)),
                ('student_phone_number', models.CharField(max_length=20, null=True)),
                ('father_name', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True, verbose_name="Father's Full Name")),
                ('father_phone', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True, verbose_name="Father's Phone Number")),
                ('mother_name', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True, verbose_name="Mother's Full Name")),
                ('mother_number', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True, verbose_name="Mother's Phone Number")),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('current_school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school', to='auths.school', verbose_name='Name of current school')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auths.department')),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auths.level')),
                ('prev_school_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_1', to='auths.school', verbose_name='Former school 1')),
                ('prev_school_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_2', to='auths.school', verbose_name='Former school 1')),
                ('prev_school_3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_3', to='auths.school', verbose_name='Former school 1')),
                ('std_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auths.class', verbose_name='Class')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auths.customuser')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeachingSTaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Dr', 'Dr'), ('Prof', 'Prof')], max_length=10, null=True)),
                ('middle_name', models.CharField(help_text='Enter your middle name here if any', max_length=25, null=True)),
                ('picture', models.ImageField(null=True, upload_to='Teachers_Photo/%Y/%m/%d/')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('date_of_birth', models.DateField(help_text='Format: YYYY-MM-DD', null=True)),
                ('age', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('religion', models.CharField(choices=[('Christianity', 'Christianity'), ('Islam', 'Islam')], max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('about_me', models.TextField(help_text='Write something about yourself, not more than 300 words', max_length=300, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('designation', models.CharField(choices=[('Principal', 'Principal'), ('Vice Principal', 'Vice Principal'), ('Head of Department', 'Head of Department'), ('Subject Teacher', 'Subject Teacher')], max_length=100)),
                ('grade_level', models.CharField(help_text='E.g, Level 8 Step 2', max_length=20, null=True)),
                ('first_appointment', models.DateField(null=True)),
                ('years_in_service', models.CharField(max_length=15, null=True)),
                ('qualification', models.CharField(choices=[('NCE', 'NCE'), ('HND', 'HND'), ('B.Sc', 'B.Sc'), ('PGDE', 'PGDE'), ('B.Arts', 'B.Arts'), ('M.Sc', 'M.Sc'), ('PhD', 'PhD')], max_length=10, null=True)),
                ('discipline', models.CharField(max_length=200, null=True)),
                ('published_work', models.URLField(help_text='Start with "http://" or https://', null=True)),
                ('current_subject', models.CharField(max_length=100, null=True)),
                ('previous_subjects', models.CharField(max_length=200, null=True)),
                ('current_posting_school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current', to='auths.school')),
            ],
            options={
                'verbose_name': 'Teaching Staff',
                'verbose_name_plural': 'Teaching Staffs',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeachingSTaffFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.FileField(upload_to=auths.models.teachers_directory)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auths.teachingstaff')),
            ],
        ),
        migrations.AddField(
            model_name='teachingstaff',
            name='current_posting_zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zone', to='auths.zone'),
        ),
        migrations.AddField(
            model_name='teachingstaff',
            name='previous_posting_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posting_1', to='auths.school'),
        ),
        migrations.AddField(
            model_name='teachingstaff',
            name='previous_posting_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posting_2', to='auths.school'),
        ),
        migrations.AddField(
            model_name='teachingstaff',
            name='previous_posting_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posting_3', to='auths.school'),
        ),
        migrations.AddField(
            model_name='teachingstaff',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auths.customuser'),
        ),
        migrations.CreateModel(
            name='StudentFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.FileField(upload_to=auths.models.students_directory)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auths.student')),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auths.zone'),
        ),
        migrations.CreateModel(
            name='NonTeachingSTaffFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.FileField(upload_to=auths.models.non_teachers_directory)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auths.nonteachingstaff')),
            ],
        ),
        migrations.AddField(
            model_name='nonteachingstaff',
            name='current_posting_school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='currents', to='auths.school'),
        ),
        migrations.AddField(
            model_name='nonteachingstaff',
            name='current_posting_zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zones', to='auths.zone'),
        ),
        migrations.AddField(
            model_name='nonteachingstaff',
            name='previous_posting_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postings_1', to='auths.school'),
        ),
        migrations.AddField(
            model_name='nonteachingstaff',
            name='previous_posting_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postings_2', to='auths.school'),
        ),
        migrations.AddField(
            model_name='nonteachingstaff',
            name='previous_posting_3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postings_3', to='auths.school'),
        ),
        migrations.AddField(
            model_name='nonteachingstaff',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auths.customuser'),
        ),
    ]
