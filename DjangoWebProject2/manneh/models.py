from django.db import models

# Create your models here.
class Manneh(models.Model):
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    member_choice = [
        ('father','John'),
        ('mother', 'Sarah'),
        ('baby', 'Emmanuel'),
        ]
    member_fields = models.CharField(
        max_length=30,
        choices=member_choice,
        default = 'null'
        )
    emptyList = [('1','egg'),('2','banana')]
    emptyList_fields = models.CharField(
        max_length=50,
        choices = emptyList,
        default = 'null')