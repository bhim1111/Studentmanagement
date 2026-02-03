from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)

    age = models.IntegerField()
    course = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name