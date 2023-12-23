from django.urls import path, include, re_path
from users import views
from django.contrib.auth import views as auth


urlpatterns = [
    path('', views.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='login.html'), name ='logout'),
    path('register/', views.register, name ='register'),
    path('index/', views.index, name ='index'),

]
