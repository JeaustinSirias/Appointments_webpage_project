"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from application.views import sample
from application import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


# Do no forget to add the '/' in paths' names
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage, name='homepage'),
    path('newcite/', views.new_appointment, name='new'),
    path('modify-cite/<id>/', views.modify_appointment, name='modify'),
    path('deletecite/', views.sample, name='delete'),
    path('checkout/', views.show_appointment, name='show'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('delete-cite/<id>', views.delete_appointment, name='delete')
]

