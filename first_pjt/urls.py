"""
URL configuration for first_pjt project.

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

from first_app import views
# first_app 폴더 내부의 views.py

urlpatterns = [
    # '경로/'가 들어오면, `함수`를 실행해줘
    path('admin/', admin.site.urls),
    path('index/', views.index), 
    path('hello/', views.hello),
    path('lunch/', views.lunch),
    path('lotto/', views.lotto),

    # vaiable routing (변수화된 주소)
    path('profile/<username>/', views.profile),
    # 127.0.0.1:8000/profile/username/
    path('cube/<int:number>/', views.cube),
    # django식 해결법 int: -> str이 기본
    
    path('articles/', views.articles),
    path('ping/', views.ping),
    path('pong/', views.pong),
]   

# 경로 설정