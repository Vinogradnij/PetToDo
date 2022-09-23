from django.db import models


# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
