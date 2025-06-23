from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts', include('accounts.urls')),
    path('articles/',include('articles.urls')),
    path('', views.homepage), 
    path('about/', views.about), 


]

#we are appending to the urlpattern
urlpatterns += staticfiles_urlpatterns()
#for serving of media files like images and other stuffs, appending the urlpatterns when  somebody hits '/media' should be able to see the media
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

