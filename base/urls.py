from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('posts/',views.posts,name='posts'),
    path('post/<slug:slug>/',views.post,name='post'),
    #CRUD URLS
    path('create-post/',views.createPost,name='create-post'),
    path('update-post/<slug:slug>/',views.updatePost,name='update-post'),
    path('delete-post/<slug:slug>/',views.deletePost,name='delete-post'),
    path('send-email/',views.sendEmail,name='send-email'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
