"""
URL configuration for Blogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views


admin.site.site_header = "Blog Post Admin"
admin.site.site_title = "Blog Post Admin Portal"
admin.site.index_title = "Welcome to Blog Post Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name= 'home'),
    path("category", views.category, name= 'category'),
    path("about", views.about, name= 'about'),
    path("post", views.post, name= 'post')
    
]
