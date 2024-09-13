from django.db import models

# Create your models here.

class standard(models.Model):
    standard_number = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.standard_number

class classroom(models.Model):
    standard_id=models.ManyToManyField(standard,max_length=10)
    division=models.CharField(max_length=10)

    def __str__(self):
        return self.division

class students(models.Model):
    class_room=models.ManyToManyField(classroom)
    student_name=models.CharField(max_length=50)
    student_email=models.CharField(max_length=50)

    def __str__(self):
        return self.student_name