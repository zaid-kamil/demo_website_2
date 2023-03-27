from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=122)
    mobile = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name