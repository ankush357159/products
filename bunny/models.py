from django.db import models

class MyPet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    weight = models.IntegerField()
    photo = models.ImageField(upload_to='pets/')

    def __str__(self):
        return self.name
