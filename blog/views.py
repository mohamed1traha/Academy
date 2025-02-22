from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .forms import PostForm,UserForm
from .models import Post1

@login_required
def blog_index(request):
    posts = Post1.objects.all()  # لا حاجة لـ id__isnull=False
    return render(request, 'blok_index.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # تعيين المستخدم الحالي كمالك المنشور
            post.save()
            return redirect(blog_index)  # إعادة التوجيه إلى قائمة المنشورات
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post1, id=post_id)
    
    if request.user in post.like.all():
        post.like.remove(request.user)  # إزالة الإعجاب
        button_text = "الإعجاب"
    else:
        post.like.add(request.user)  # إضافة الإعجاب
        button_text = "إزالة الإعجاب"

    like_count = post.like.count()  # عدد الإعجابات الحالي
    return JsonResponse({
        'like_count': like_count,
        'button_text': button_text,
    })


@login_required
def profile(request):
    user = request.user
    post = Post1.objects.filter(user=user)
    return render(request,'profile.html',{
        'post':post,
    })


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post1, id=post_id, user=request.user)  
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
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect(profile)  
    else:
        form = UserForm(instance=user)
    
    return render(request, 'edit_profile.html', {'form': form, 'user': user})
