from django.contrib.auth.models import User
from django.db import models





class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    title = models.CharField(max_length=255,default='no title')
    img = models.ImageField(upload_to='blog/', null=True, blank=True)
    content = models.TextField(default='no content')     
    created_at = models.DateTimeField(auto_now_add=True,null=True,) 

    def __str__(self):  
        return self.title
    



 

    