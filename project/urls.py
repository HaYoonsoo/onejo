"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('registration/signup', views.signup, name="signup"),
    path('registration/logout', views.logout, name="logout"),
    path('pig_new', views.pig_new, name="pig_new"),
    path('pig_detail/<int:pig_pk>', views.pig_detail, name="pig_detail"),
    path('schedule_new/<int:pig_pk>', views.schedule_new, name="schedule_new"),
    path('pig_bye', views.pig_bye, name="pig_bye"),
    path('landing/', views.landing, name="landing"),
    path('accounts/', include("allauth.urls")),
    path('bye_donate', views.bye_donate, name="bye_donate"),
    path('bye_winner', views.bye_winner, name="bye_winner"),
    path('bye_winner_complete', views.bye_winner_complete, name="bye_winner_complete"),
    path('bye_donate_complete', views.bye_donate_complete, name="bye_donate_complete"),
]

