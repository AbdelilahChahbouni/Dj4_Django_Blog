from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=4000)
    create_date = models.DateTimeField(default=timezone.now())
    draft = models.BooleanField(default= True)
    tags = TaggableManager()
    auth = models.ForeignKey(User , on_delete=models.SET_NULL,null=True , blank=True , related_name="post_user")
    image = models.ImageField(upload_to='posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(max_length=300)
    create_at = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User ,on_delete= models.CASCADE, related_name="comment_user" )
    post = models.ForeignKey(Post , on_delete= models.CASCADE , related_name = "comment_post")

    def __str__(self):
        return str(self.user)



    


        

