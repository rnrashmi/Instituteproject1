from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    sname=models.CharField(max_length=100)
    smobile=models.BigIntegerField()
    scourse=models.CharField(max_length=50)
    sloc=models.CharField(max_length=50)



import datetime as dt
date1= dt.datetime.now()

class FeedbackData(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    rating=models.IntegerField()
    date=models.DateTimeField(max_length=100)
    feedback=models.CharField(max_length=100)








