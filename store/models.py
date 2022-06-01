from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=30)
    isbn = models.IntegerField()

    def __str__(self):
        return self.name

        
class MyModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

        
