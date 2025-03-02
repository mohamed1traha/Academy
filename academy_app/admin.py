from .models import Course,UserCourse,Category
from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import Course, Track, Video

class TrackInline(admin.TabularInline):
    model = Track
    extra = 1

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [TrackInline]

class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    inlines = [VideoInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Video)
admin.site.register(Category)
admin.site.register(UserCourse)