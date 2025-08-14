from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll_no = models.CharField(max_length=50)
    university_number = models.CharField(max_length=50)
    college_name = models.CharField(max_length=150)
    passing_year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.roll_no})"
