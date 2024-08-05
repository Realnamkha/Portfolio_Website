from django.db import models
from django.utils.text import slugify
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    headline = models.CharField(max_length=100)
    slug = models.SlugField(blank=True,null=True)
    body = models.TextField(null=True,blank=True)
    image = models.ImageField(default='placeholder.png',upload_to='images')
    created = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag,null=True)


    def __str__(self):
        return self.headline
    
    def save(self,*args,**kwargs):
        if self.slug == None:
            slug = slugify(self.headline)
            self.slug = slug
        super().save(*args,**kwargs)