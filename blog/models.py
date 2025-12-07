from django.db import models

# Create your models here.
# reference an object by its URL template name 
from django.urls import reverse 
# assume each post has a title, author, and body 

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk}) # primary key, pk 
        

