
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
  

    def __str__(self):
        return self.name

class Card(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)
    desc = models.TextField()
    img = models.ImageField(upload_to='uploads/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    tags = models.ManyToManyField(Tag, blank=True)
   

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-publish_date"]

    
    def tag_name(self):
        return ','.join([ str(t) for t in self.tags.all()])






