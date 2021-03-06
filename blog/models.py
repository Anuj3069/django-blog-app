from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class CustomManager(models.Manager):
  def get_queryset(self):
      return super().get_queryset().filter(status='publish')

class Post(models.Model):
    STATUS_CHOICE=(('draft','Draft'),('publish','Publish'))
    title=models.CharField(max_length=264)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    author=models.ForeignKey(User,on_delete=CASCADE, related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICE,default='draft')
    objects=CustomManager()
    class Meta:
      ordering=('-publish',)

    def __str__(self):
       return self.title        
    
    def get_absolute_url(self):
     return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])