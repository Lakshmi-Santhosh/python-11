from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import home

app_name='schoolapp'
urlpatterns = [
  path('',views.home,name='home'),
  path('login/', views.login, name='login'),
  path('register/', views.register, name='register'),
  path('mypage/', views.mypage, name='mypage'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('new_page/', views.new_page, name='new_page'),
  path('confirmation_page/', views.confirmation_page, name='confirmation_page'),


]