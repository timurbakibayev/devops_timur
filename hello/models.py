from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=1000, default="Timur")

    def __str__(self):
        return self.name
