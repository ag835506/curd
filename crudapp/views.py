from django.shortcuts import render,redirect
from .models import Studentdata
def home(request):
    students=Studentdata.objects.all()
    context={'students':students}
    return render(request,'students/home.html',context)
def add_students(request):
    return render(request,'students/add_student.html')
def save_data(request):
    sname=request.POST.get('sname')
    cls=request.POST.get('cls')
    section=request.POST.get('section')
    school=request.POST.get('school')
    email=request.POST.get('email')
    mobile=request.POST.get('mobile')
    telugu=request.POST.get('telugu')
    hindi=request.POST.get('hindi')
    english=request.POST.get('english')
    math=request.POST.get('math')
    science=request.POST.get('science')
    social=request.POST.get('social')
    data=Studentdata(
        student_name=sname,
        class_name=cls,
        section=section,
        school_name=school,
        email=email,
        mobile=mobile,
        telugu_marks=telugu,
        hindi_marks=hindi,
        english_marks=english,
        math_marks=math,
        science_marks=science,
        social_marks=social
    )
    data.save()
    return redirect('/')
def update_data(request,pk):
    student=Studentdata.objects.get(id=pk)
    context={'student':student}
    return render(request,'students/update.html',context)
def save_update_data(request,pk):
    student=Studentdata.objects.get(id=pk)
    student.student_name = request.POST.get('sname')
    student.class_name = request.POST.get('cls')
    student.section = request.POST.get('section')
    student.school_name = request.POST.get('school')
    student.email = request.POST.get('email')
    student.mobile = request.POST.get('mobile')
    student.telugu_marks = request.POST.get('telugu')
    student.hindi_marks = request.POST.get('hindi')
    student.english_marks = request.POST.get('english')
    student.math_marks = request.POST.get('math')
    student.science_marks = request.POST.get('science')
    student.social_marks = request.POST.get('social')
    student.save()
    return redirect('/')
def delete_data(request,pk):
    student=Studentdata.objects.get(id=pk)
    student.delete()
    return redirect('/')

