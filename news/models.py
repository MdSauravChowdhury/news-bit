from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic  = models.ImageField(upload_to='img/author/')

    def __str__(self):
        return self.user.username

class category(models.Model):
    name = models.CharField(max_length=15)     

    def __str__(self):
        return self.name   

class Post(models.Model):

    title = models.CharField(max_length=150)  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  
    thumbnail = models.ImageField(upload_to='post/img')  
    timestamp = models.DateTimeField(auto_now_add=True) 
    view_count = models.PositiveIntegerField(default=0) 
    comment_count = models.PositiveIntegerField(default=0) 
    text = models.TextField()
    category = models.ManyToManyField(category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.thumbnail.path)

        if img.width > 350 and img.height > 212:
            output_size = (350, 212)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)


class EmailSubcribe(models.Model):
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.email
