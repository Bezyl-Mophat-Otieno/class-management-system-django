# NAME : OTIENO MOPHAT BEZYL
# REG NO : IN16/00003/20
# UNIT : OBJECT ORIENTED PROGRAMMING USING PYTHON
# UNIT CODE : SOEN 380

from django import forms
from django.forms import ModelForm
from .models import Student,Unit,Class,ClassStudent,AddNewClass


        
class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ['unit_title','unit_code',]
        widgets = {
            'unit_title':forms.TextInput(attrs={'class':'form-control'}),
            'unit_code':forms.TextInput(attrs={'class':'form-control'}),
            
        }

        
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['std_name','std_regno','std_course',]
        widgets = {
            'std_name':forms.TextInput(attrs={'class':'form-control'}),
            'std_regno':forms.TextInput(attrs={'class':'form-control'}),
            'std_course':forms.TextInput(attrs={'class':'form-control'}),
         
        }
class ClassStudentForm(ModelForm):
    class Meta:
        model = ClassStudent
        fields = ['std_name','std_regno','std_course','unit_code']
        widgets = {
            'std_name':forms.TextInput(attrs={'class':'form-control'}),
            'std_regno':forms.TextInput(attrs={'class':'form-control'}),
            'std_course':forms.TextInput(attrs={'class':'form-control'}),
            'unit_code':forms.TextInput(attrs={'class':'form-control'}),
         
        }

class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['std_name','unit_code','cat1','cat2','cat3','final_exam_grade']
        widgets = {
            'std_name':forms.TextInput(attrs={'class':'form-control'}),
            'unit_code':forms.TextInput(attrs={'class':'form-control'}),
            'cat1':forms.TextInput(attrs={'class':'form-control'}),
            'cat2':forms.TextInput(attrs={'class':'form-control'}),
            'cat3':forms.TextInput(attrs={'class':'form-control'}),
            'final_exam_grade':forms.TextInput(attrs={'class':'form-control'}),
         
        }


class AddNewClassForm(ModelForm):
    class Meta:
        model = AddNewClass
        fields = ['unit_code','cat1','cat2','cat3','final_exam_grade']
        widgets = {
            'unit_code':forms.TextInput(attrs={'class':'form-control'}),
            'cat1':forms.TextInput(attrs={'class':'form-control'}),
            'cat2':forms.TextInput(attrs={'class':'form-control'}),
            'cat3':forms.TextInput(attrs={'class':'form-control'}),
            'final_exam_grade':forms.TextInput(attrs={'class':'form-control'}),
         
        }
        