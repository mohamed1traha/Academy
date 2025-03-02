from django.contrib.auth.decorators import login_required
from .models import Course, AcademyComment,UserCourse,Category
from django.shortcuts import get_object_or_404,render
from django.http import JsonResponse
from .forms import CommentForm

def academy_index(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        user = request.user
        user_courses = UserCourse.objects.filter(user=user).values_list('course', flat=True)
        courses = Course.objects.exclude(id__in=user_courses)
    else:
        courses = Course.objects.all()
    for course in courses:
        video_id = course.video_url.split('youtu.be/')[1] if 'youtu.be/' in course.video_url else None
        course.video_id = video_id 
    
    return render(request,'academy_index.html',{
        'courses':courses,
        'categories':categories,
        })


def course_page(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if course.video_url:
        video_url = course.video_url.replace("https://youtu.be/", "https://www.youtube.com/embed/")
        course.video_url = video_url  # تخزين الرابط المعدل
    
    return render(request, 'course_page.html', {'course': course})



@login_required
def available(request):
    user = request.user
    user_courses = UserCourse.objects.filter(user=user)  # جلب الكورسات التي اشتراها المستخدم

    # استخراج قائمة الكورسات من كائنات UserCourse
    courses = [uc.course for uc in user_courses]

    # إضافة video_id لكل كورس إذا كان لديه فيديو من يوتيوب
    for course in courses:
        if hasattr(course, 'video_url') and course.video_url:
            video_id = course.video_url.split('youtu.be/')[1] if 'youtu.be/' in course.video_url else None
            course.video_id = video_id  # إضافة معرف الفيديو إلى الكورس

    return render(request, 'available.html', {'courses': courses})




@login_required
def content(request,course_id,Video_id):
    course_id = Course.objects.get(id=course_id)
    track = Track.objects.filter(course=course_id)
    vido = get_object_or_404(Video, id=Video_id)

    # تعديل رابط الفيديو
    if vido.video_url:
        video_url = vido.video_url.replace("https://youtu.be/", "https://www.youtube.com/embed/")
        vido.video_url = video_url  

    comments = vido.academy_comments.filter(parent__isnull=True).order_by('-created_at')  
    form = CommentForm()

    if request.method == "POST":
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":  # 🔹 التأكد من أنه طلب AJAX
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.video = vido
                comment.user = request.user  

                
                parent_id = request.POST.get('parent_id')
                if parent_id:
                    parent_comment = AcademyComment.objects.get(id=parent_id)
                    comment.parent = parent_comment 

                comment.save()

               
                return JsonResponse({
                    "success": True,
                    "user": comment.user.username,
                    "text": comment.content,
                    "created_at": comment.created_at.strftime("%Y-%m-%d %H:%M"),
                    "comment_id": comment.id,
                    "parent_id": comment.parent.id if comment.parent else None,  # إذا كان هناك اقتباس
                    "parent_user": comment.parent.user.username if comment.parent else None,
                    "parent_content": comment.parent.content if comment.parent else None,
                })

        return JsonResponse({"success": False}, status=400)

    return render(request, 'content.html', {
        'course': vido,
        'comments': comments,
        'form': form,
        'track': track,
    })



def category_page(request,category_id):
    categories = Category.objects.all()
    category_id = Category.objects.get(id=category_id)
    course = Course.objects.filter(category=category_id)
    return render(request,'category_page.html',{
        'course':course,
        'categories':categories
        })



from django.shortcuts import render, get_object_or_404
from .models import Course, Track, Video



def track_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    track = Track.objects.filter(course=course)
    return render(request, 'track_detail.html', {
        'track': track,
        'course_id':course_id,
        })

def vidos(request, track_id):
    track = Track.objects.get(id=track_id)
    vido = Video.objects.filter(track=track)
    return render(request, 'vidos.html', {'vido': vido})