from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeingKey(Post, on_delete=models.CASCADE)
    
class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField()
    body = models.TextField()
    tags = models.CharField()
    created_at = models.DateTimeField()