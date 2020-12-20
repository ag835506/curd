from django.db import models
class Studentdata(models.Model):
    student_name=models.CharField(max_length=100)
    class_name=models.CharField(max_length=20)
    section=models.CharField(max_length=10)
    school_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    telugu_marks=models.IntegerField()
    hindi_marks=models.IntegerField()
    english_marks=models.IntegerField()
    math_marks=models.IntegerField()
    science_marks=models.IntegerField()
    social_marks=models.IntegerField()

