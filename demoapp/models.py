from django.db import models
import datetime

# Create your models here.

class Wishes(models.Model):
    place=models.CharField(max_length=100)
    priority=models.IntegerField()
    added_date=models.DateField(default=datetime.date.today)
    experience=models.CharField(max_length=400)
    def __str__(self):
        return self.place