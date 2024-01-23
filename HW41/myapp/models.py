from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def str(self):
         return self.name