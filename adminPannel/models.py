from pickle import TRUE
from pyexpat import model
from django.db import models

# Create your models here.
class books_info(models.Model):
    book_id = models.IntegerField()
    book_name = models.CharField(blank=False , max_length=150)
    author = models.CharField(blank=False , max_length=150)
    isbn_no = models.CharField(blank=False , max_length=100)
    current_stock = models.IntegerField(null=TRUE)
    category = models.CharField(blank=False , max_length=300, default="NULL")

class stu_info(models.Model):
    stu_name =  models.CharField(max_length=150, blank=False)
    stu_roll = models.IntegerField()



    
        