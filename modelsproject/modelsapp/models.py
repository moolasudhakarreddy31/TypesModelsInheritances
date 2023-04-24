from django.db import models

# Create your models here.

# Abstract Type
class ContactInfo(models.Model):
    name=models.CharField(max_length=233)
    email=models.EmailField()
    address=models.CharField(max_length=433)
    class Meta:
        abstract=True


class StudentInfo(ContactInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class TeacharsInfo(ContactInfo):
    subject=models.CharField(max_length=233)
    salary=models.BigIntegerField()



#Multiple Inhertance Type
class ContactInfo1(models.Model):
    name=models.CharField(max_length=233)
    email=models.EmailField()
    address=models.CharField(max_length=433)


class StudentInfo1(ContactInfo1):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class TeacharsInfo1(ContactInfo1):
    subject=models.CharField(max_length=233)
    salary=models.BigIntegerField()



# MultiLevel Inhertance Type
class Parent(models.Model):
    fd1=models.CharField(max_length=222)
    fd2=models.CharField(max_length=222)

class Child(Parent):
    fd3=models.CharField(max_length=222)
    fd4=models.CharField(max_length=222)



class SubChild(Child):
    fd5=models.CharField(max_length=222)













