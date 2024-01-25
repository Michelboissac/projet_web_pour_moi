from django.db import models

# Create your models here.

"""
    primary key
    unique
    default
    null
    blank

    CharField
    I tegerField
    DateTimeField
    FloatField
    EmailField
    BooleanField
"""
class Authors(models.Model):
    name = models.CharField(max_length = 64, unique = True)

class Book(models.Model):
    title = models.CharField(max_length = 32, unique = True)
    quantity = models.IntegerField(default = 1)
    author = models.ForeignKey(Authors, on_delete = models.DO_NOTHING)
    #sequence = models.TextField()

