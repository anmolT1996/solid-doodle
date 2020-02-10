from django.contrib import admin
from django.urls import path
from basicApp import views

app_name = 'basic_app'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('detail/',views.detail,name='detail')
]
