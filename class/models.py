# NAME : OTIENO MOPHAT BEZYL
# REG NO : IN16/00003/20
# UNIT : OBJECT ORIENTED PROGRAMMING USING PYTHON
# UNIT CODE : SOEN 380

from django.db import models

# Create your models here.
# student model that houses student name reg no and course .

class Student (models.Model):
    std_name = models.CharField(max_length=200)
    std_regno = models.CharField(max_length=200)
    std_course = models.CharField(max_length=200)

    def __str__ (self):
     return self.std_name or ''
    
class ClassStudent (models.Model):
    std_name = models.CharField(max_length=200)
    std_regno = models.CharField(max_length=200)
    std_course = models.CharField(max_length=200)
    unit_code = models.CharField(max_length=200)

    def __str__ (self):
     return self.std_name or ''
    

# Unit model that houses unit code and unit title
class Unit (models.Model):
    unit_title = models.CharField(max_length=100)
    unit_code = models.CharField(max_length=100)

    def __str__ (self):
     return self.unit_title or ''
    
    
    
 # Marks model that houses student reg no , unit code and marks will go here 

class Class (models.Model):
    std_name = models.CharField( max_length=200, null=True , blank=True )
    unit_code = models.CharField(max_length=200, null=True , blank=True)
    cat1 = models.IntegerField(null=True , blank=True)
    cat2 = models.IntegerField(null=True , blank=True)
    cat3 = models.IntegerField(null=True , blank=True)
    final_exam_grade = models.IntegerField(default=0)

    def __str__ (self):
     return self.std_name or ''
    


class AddNewClass (models.Model):
    unit_code = models.CharField(max_length=200, null=True , blank=True)
    cat1 = models.IntegerField(null=True , blank=True)
    cat2 = models.IntegerField(null=True , blank=True)
    cat3 = models.IntegerField(null=True , blank=True)
    final_exam_grade = models.IntegerField(default=0)

    def __str__ (self):
     return self.unit_code or ''
    
    
    



