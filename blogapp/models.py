from django.db import models

# Create your models here.
class BlogPost(models.Model):
    Title = models.CharField(max_length=70)
    Author = models.CharField(max_length=50)
    Post = models.CharField(max_length=7000)
    Date = models.DateField()

    def __str__(self) -> str:
        return self.Title
    
class User(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.BigIntegerField()
    Message = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return self.Firstname