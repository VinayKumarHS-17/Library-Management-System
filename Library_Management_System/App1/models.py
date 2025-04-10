from django.db import models

# Create your models here.

class AddBooks(models.Model):
    book_name=models.CharField(max_length=100)
    ISBN=models.IntegerField()
    Quantity=models.IntegerField()
    Author=models.CharField(max_length=70)


class IssueBook(models.Model):
    Student_name=models.CharField(max_length=100)
    Student_roll=models.IntegerField()
    Student_branch=models.CharField(max_length=100)
    book_name=models.CharField(max_length=100)
    ISBN=models.IntegerField()
    Issue_date=models.DateField()