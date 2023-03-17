# NAME : OTIENO MOPHAT BEZYL
# REG NO : IN16/00003/20
# UNIT : OBJECT ORIENTED PROGRAMMING USING PYTHON
# UNIT CODE : SOEN 380

from django.urls import path
from . import views

app_name = 'class'

urlpatterns = [
path('add_student', views.add_student_form,name='studentform'),
path('add_new_class', views.add_new_class_form,name='newclass'),
path('view_classes', views.view_classes,name='viewclass'),
path('view_students', views.view_students,name='students'),
path('add_unit', views.add_unit,name='unitform'),
path('view_units', views.view_units,name='units'),
path('add_marks', views.add_marks,name='addmarks'),
path('view_marksheet', views.view_marksheet,name='marksheets'),
path('update_marksheet/<int:marksheet_id>', views.update_marksheet,name='updatemarksheets'),
path('add_std_class', views.add_std_class_form,name='addclassstudent'),
path('view_class_list', views.view_class_list,name='classList'),

]