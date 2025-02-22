from django.contrib.auth import views as auth_views 
from django.urls import include, path
from blog import views as view
from . import views 





urlpatterns=[
    path('cours_page/<int:course_id>/',views.course_page,name='course_page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('content/<int:course_id>/', views.content, name='content'),
    path('checkout/',include('checkout.urls'),name='checkout'),
    path('available/',views.available,name='available'),
    path('',views.academy_index,name='academy_index'),
    path('blog/', view.blog_index,name='blog_index'),
]


