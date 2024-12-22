"""
URL configuration for UrbanDjango project.

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
from django.contrib import admin
from django.urls import path, include
from task2.views import function_based_view, classBasedView
from django.contrib import admin
from django.urls import path
from task3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main_page'),
    path('shop/', views.shop_page, name='shop_page'),
    path('cart/', views.cart_page, name='cart_page'),
]

urlpatterns = [
	path('admin/', admin.site.urls),
	path('classtemplate/', classBasedView.as_view()),
	path('functemplate/', function_based_view),

]
