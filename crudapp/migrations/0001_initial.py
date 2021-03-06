# Generated by Django 3.0.3 on 2020-03-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studentdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('class_name', models.IntegerField()),
                ('section', models.CharField(max_length=10)),
                ('school_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('telugu_marks', models.IntegerField()),
                ('hindi_marks', models.IntegerField()),
                ('english_marks', models.IntegerField()),
                ('math_marks', models.IntegerField()),
                ('science_marks', models.IntegerField()),
                ('social_marks', models.IntegerField()),
            ],
        ),
    ]
