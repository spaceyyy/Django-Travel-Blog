from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=50)
    Lat = models.FloatField(null=True)
    Lng = models.FloatField(null=True)
    mainphoto = models.ImageField(blank=True, null=True)
    publishedDate = models.DateTimeField(blank=True, null=True)
    modifiedDate = models.DateTimeField(blank=True, null=True)
    contents = models.TextField()
    tag = TaggableManager(blank=True)
    
    def __str__(self):
        return self.postname
