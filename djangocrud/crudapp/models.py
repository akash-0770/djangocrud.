from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=100,verbose_name="student name")
    email = models.EmailField(max_length=227,verbose_name="student email")

    def __str__(self):
        return str(self.id)