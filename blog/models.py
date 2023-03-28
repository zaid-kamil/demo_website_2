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
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category,
                    on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='articles')

    def __str__(self):
        return self.title