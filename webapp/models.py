from django.db import models


class University(models.Model):
    university_id = models.IntegerField()
    university_name = models.CharField(max_length=20)
    university_location = models.CharField(max_length=10)
    university_about = models.CharField(max_length=150)

    def __str__(self):
       return self.university_name