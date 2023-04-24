from django.db import models

# Create your models here.
class User(models.Model):
    def __str__(self):
        return self.name +' ' + self.surname

    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    birth_date = models.DateField('Birth Date')