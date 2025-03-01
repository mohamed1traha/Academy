from django.contrib.auth import views as auth_views 
from academy_app.views import academy_index
from django.urls import path
from . import views 
from user.views import register


urlpatterns = [
    path('',views.blog_index,name='blok_index'),
    path('edit_profile/<int:user_id>/', views.edit_profile, name='edit_profile'),
    path('post_edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('academy_index/',academy_index,name='academy_index'),
    path('profile/', views.profile, name='profile'),
    path('register/', register, name='register'),
    path('post_page/<int:post_id>', views.post_page, name='post_page'),
]