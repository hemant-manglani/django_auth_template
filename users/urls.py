from django.urls import path, include, re_path
from users import views


urlpatterns = [
    path('', views.Login, name ='login'),
    path('logout/', views.log_out, name ='logout'),
    path('register/', views.register, name ='register'),
    path('index/', views.index, name ='index'),

]
