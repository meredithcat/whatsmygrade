from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=50)
  sid = models.CharField(max_length=50)
  assignments = models.ManyToManyField('Assignment', through='StudentAssignment')

  def __str__(self):
    return self.name

class Assignment(models.Model):
  name = models.CharField(max_length=50)
  max_points = models.IntegerField()

  def __str__(self):
    return self.name

class StudentAssignment(models.Model):
  student = models.ForeignKey('Student', on_delete=models.CASCADE)
  assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)
  points = models.DecimalField(max_digits=5, decimal_places=2)
  hours_late = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return f'Student {self.student} assignment {self.assignment}'