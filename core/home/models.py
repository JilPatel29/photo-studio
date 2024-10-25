# home/models.py

# from django.db import models

# class ModelName(models.Model):
#     # Define your fields here
#     field1 = models.CharField(max_length=100)
#     field2 = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.field1


from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100) 
    
    def __str__(self):
        return self.name
