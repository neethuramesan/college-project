from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=255)
    fee=models.IntegerField()
class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    student_name=models.CharField(max_length=255)
    student_address=models.CharField(max_length=255)
    student_age=models.IntegerField(default=0)
    joining_date=models.DateField()
    
class Usermember(models.Model):
  
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255,null=True)
    age=models.IntegerField(null=True)
    number=models.CharField(max_length=255,null=True)
    image=models.ImageField(blank=True,upload_to="image/", null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
class Usermember(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    number=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to="image/", null=True)