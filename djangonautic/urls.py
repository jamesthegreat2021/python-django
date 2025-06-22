from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',include('articles.urls')),
    path('', views.homepage), 
    path('about/', views.about), 


]

#we are appending to the urlpattern
urlpatterns += staticfiles_urlpatterns()

