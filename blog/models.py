from django.db import models
from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0) # Record how often a post is seen
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    image2 = models.ImageField(upload_to="images", blank=True, null=True)
    image3 = models.ImageField(upload_to="images", blank=True, null=True)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
# Create your models here.
