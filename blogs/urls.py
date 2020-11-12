from django.urls import path
from . import views

app_name ='blogs'

urlpatterns = [
	path('', views.blog_list, name='blog_list'),
	path('<str:slug>/', views.blog_detail, name='blog_detail'),
]