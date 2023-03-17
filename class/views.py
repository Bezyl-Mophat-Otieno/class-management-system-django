
# NAME : OTIENO MOPHAT BEZYL
# REG NO : IN16/00003/20
# UNIT : OBJECT ORIENTED PROGRAMMING USING PYTHON
# UNIT CODE : SOEN 380

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import StudentForm,UnitForm,ClassForm,ClassStudentForm,AddNewClassForm
from .models import Student,Unit,Class,ClassStudent,AddNewClass

def view_students(request):
    students = Student.objects.all()
    return render(request , 'class/view_Students.html',{'students':students})

def view_units(request):
    units = Unit.objects.all()
    return render(request , 'class/view_units.html',{'units':units})

def view_classes(request):
    classes = AddNewClass.objects.all()
    return render(request , 'class/view_classes.html',{'classes':classes})

def view_marksheet(request):
    markSheets = Class.objects.all()
    print(markSheets)
    return render(request , 'class/view_marksheet.html',{'markSheets':markSheets})
def update_marksheet(request,marksheet_id):
    markSheets = Class.objects.get( pk=marksheet_id)
    form = ClassForm(request.POST or None,instance=markSheets)
    if form.is_valid():
        form.save()
        return redirect('/class/view_marksheet')

    return render(request , 'class/update_marksheet.html',{'markSheets':markSheets,'form':form})

def view_class_list(request):
    classlist = ClassStudent.objects.all()
    return render(request , 'class/view_class_list.html',{'classlist':classlist})

def add_student_form(request):
    submitted = False
    if request.method == 'POST':
        form= StudentForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('view_students?submitted=True')
    else:
        form = StudentForm()
        print(form)
        if 'submitted' in request.GET:
            submitted = True
    return render(request , 'class/add_student.html' , {'form':form , 'submitted':submitted})

def add_new_class_form(request):
    submitted = False
    if request.method == 'POST':
        form= AddNewClassForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('view_classes?submitted=True')
    else:
        form = AddNewClassForm()
        print(form)
        if 'submitted' in request.GET:
            submitted = True
    return render(request , 'class/add_class.html' , {'form':form , 'submitted':submitted})

def add_std_class_form(request):
    submitted = False
    if request.method == 'POST':
        form= ClassStudentForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('view_class_list?submitted=True')
    else:
        form = ClassStudentForm()
        print(form)
        if 'submitted' in request.GET:
            submitted = True
    return render(request , 'class/add_student_class.html' , {'form':form , 'submitted':submitted})


def add_marks(request):
    submitted = False
    if request.method == 'POST':
        form= ClassForm(request.POST)
        print(form.errors)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('view_marksheet?submitted=True')
    else:
        form = ClassForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request , 'class/add_marks.html' , {'form':form , 'submitted':submitted})

def add_unit (request):
    submitted = False
    if request.method == 'POST':
        form= UnitForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('view_units?submitted=True')
    else:
        form = UnitForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request , 'class/add_unit.html' , {'form':form , 'submitted':submitted})


