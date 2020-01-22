"""project8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from blog import views as blog
from authentification import views as auth
from search import views as search_views
from django.contrib.auth import views as auth_views
from addfav import views as add_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.home),
    path('index/', blog.index),
    path('base/', blog.base, name='home'),
    path('register/', auth.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='authentification/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='authentification/logout.html'), name='logout'),
    path('search/', search_views.SearchResultsView.as_view(), name='research'),
    path('rien/', add_views.add),
    path('nop/', add_views.favorite, name='favorite'),
    ]
