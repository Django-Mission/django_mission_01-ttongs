"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from demos.views import calculator, lotto_basic, lotto_challenge, lotto_result #추가해줘야 path에서 사용가능

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', calculator),
    path('lotto1/', lotto_basic), # mission1 - basic
    path('lotto/', lotto_challenge), # mission1 - challenge
    path('lotto/result/', lotto_result), # mission1 - challenge
]
