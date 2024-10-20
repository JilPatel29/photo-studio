# home/models.py

from django.db import models

class ModelName(models.Model):
    # Define your fields here
    field1 = models.CharField(max_length=100)
    field2 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.field1
