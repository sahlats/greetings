"""
URL configuration for greetings project.

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
from myapp.views import HelloWorldView
from myapp.views import GoodMorning
from myapp.views import GoodAfternoon
from myapp.views import GoodEvening,SelfIndroView,ActorsView,CourseView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("helloworld/",HelloWorldView.as_view()),
    path("goodmorning/",GoodMorning.as_view()),
    path("goodafter/",GoodAfternoon.as_view()),
    path("goodevening/",GoodEvening.as_view()),
    path("intro/",SelfIndroView.as_view()),
    path("actors/",ActorsView.as_view()),
    path("course/",CourseView.as_view()),




]
