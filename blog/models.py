from django.db import models

from django.core.validators import MinLengthValidator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, related_name='posts', null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    image = models.ImageField(upload_to='posts', null=True)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments', null=True)
    text = models.TextField(max_length=500)
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Tag(models.Model):
    caption = models.CharField(max_length=30)
    
    def __str__(self):
        return self.caption