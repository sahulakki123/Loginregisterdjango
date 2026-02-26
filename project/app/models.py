from django.db import models

# Create your models here.

class Employee(models.Model):
    Name=models.CharField(max_length=40)
    Email=models.EmailField()
    Contact=models.BigIntegerField()
    Password=models.CharField(max_length=20)
    CPassword=models.CharField(max_length=20,null=True)
    Photo=models.ImageField(upload_to='image')
    Audio=models.FileField(upload_to='audio')
    Video=models.FileField(upload_to='video')
    Resume=models.FileField(upload_to='document')
    City=models.CharField(max_length=20)
    Qualification=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    
class Department(models.Model):
    Dep_name = models.CharField(max_length=20)
    Dep_desc = models.CharField(max_length=20)
    Dep_head = models.CharField(max_length=20)
    
    
class AddEmployee(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.BigIntegerField()
    Images=models.ImageField(upload_to='image')
    Code=models.CharField(max_length=20)
    Departments=models.CharField(max_length=20, null=True)

class Query(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Departments = models.CharField(max_length=40)
    Query = models.TextField()
    Status = models.CharField(default="pending")
    Reply = models.TextField(null=True)
    