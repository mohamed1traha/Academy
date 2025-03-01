from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from academy_app.models import UserCourse
from .forms import PostForm,UserForm
from django.http import JsonResponse
from user.forms import ProfileForm
from user.models import Profile
from .models import Post

def blog_index(request):
    posts = Post.objects.all() 
    return render(request, 'blok_index.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  
            post.save()
            return redirect(blog_index)  
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.user in post.like.all():
        post.like.remove(request.user)  
        button_text = "الإعجاب"
    else:
        post.like.add(request.user)  
        button_text = "إزالة الإعجاب"

    like_count = post.like.count()  
    return JsonResponse({
        'like_count': like_count,
        'button_text': button_text,
    })


@login_required
def profile(request):
    user = request.user
    post = Post.objects.filter(user=user)
    user_courses = UserCourse.objects.filter(user=user)  

    courses = [uc.course for uc in user_courses]

    for course in courses:
        if hasattr(course, 'video_url') and course.video_url:
            video_id = course.video_url.split('youtu.be/')[1] if 'youtu.be/' in course.video_url else None
            course.video_id = video_id
    return render(request,'profile.html',{
        'post':post,
        'courses': courses
    })


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)  
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(profile)  
    else:
        form = PostForm(instance=post)
    
    return render(request, 'edit_post.html', {'form': form, 'post': post})







@login_required
def edit_profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user) 

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)  # تحميل الصورة

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile') 

    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})




def post_page(request,post_id):
    posts = Post.objects.get(id=post_id) 
    return render(request, 'post_page.html',{
        'post':posts
    })