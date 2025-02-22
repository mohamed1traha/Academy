from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255,null=True)
    title_en = models.CharField(max_length=255,null=True)
    descriptions = models.TextField(null=True)
    descriptions_en = models.TextField(null=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    video_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    def __str__(self):
        return self.title
    
class AcademyComment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="academy_comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="replies")
    
    def __str__(self):
        return self.content
    

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # العلاقة مع المستخدم
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # العلاقة مع الكورس
    purchase_date = models.DateTimeField(auto_now_add=True)  # تاريخ الشراء



