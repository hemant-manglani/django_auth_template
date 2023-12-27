from django.urls import path, include, re_path
from users import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('addprofile/', views.add_profile, name="add_profile"),
    path('showprofile/', views.show_profile, name="show_profile"),
    path('editprofile/<profile_id>/', views.edit_profile, name="edit_profile"),
    path('deleteprofile/<profile_id>', views.delete_profile, name="delete_profile"),

]
