from django.db import models
#clsfrom django.contrib.auth.models import User
# Models are data inputs
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True, blank=True) #blank=True makes content field optional
    date_due = models.DateTimeField(null=True, blank=True) 
   

class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)
    review_title = models.CharField(max_length=100)
    review_date_due = models.DateTimeField(null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE) #foreign key links Task to Review