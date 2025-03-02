from django.contrib.auth.models import User
from django.db import models






class Category(models.Model):
    name = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100,default='no name')
    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255,default='لا يوجد عنوان')
    title_en = models.CharField(max_length=255,default='no title')
    descriptions = models.TextField(default='لايوجد')
    descriptions_en = models.TextField(default='no descriptions')
    price = models.DecimalField(max_digits=6,decimal_places=2)
    video_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses',null=True)
    def __str__(self):
        return self.title
    

class Track(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tracks')
    title = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255,default='no title')

def __str__(self):
    return f"{self.course.title} - {self.title}"

class Video(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255,default='no title')
    video_url = models.URLField()
    duration = models.PositiveIntegerField(help_text="Duration in seconds")

    def __str__(self):
        return self.title
    
class AcademyComment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="academy_comments")
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



