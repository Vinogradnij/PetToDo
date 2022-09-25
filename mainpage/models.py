from django.db import models


# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __str__(self):
        return self.name
