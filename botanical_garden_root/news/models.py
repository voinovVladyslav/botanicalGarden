from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    preview = models.ImageField(null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.title