# Generated by Django 4.0 on 2021-12-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0002_alter_class_options_alter_department_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachingstafffiles',
            name='document_title',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
