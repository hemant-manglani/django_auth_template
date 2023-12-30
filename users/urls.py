from django.urls import path, include, re_path
from users import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    # For Candidate
    path('addprofile/', views.add_profile, name="add_profile"),
    path('showprofile/', views.show_profile, name="show_profile"),
    path('editprofile/<profile_id>/', views.edit_profile, name="edit_profile"),
    path('deleteprofile/<profile_id>', views.delete_profile, name="delete_profile"),
    # For Job posting
    path('addjobposting/', views.add_jobposting, name="add_jobposting"),
    path('showjobposting/', views.show_jobposting, name="show_jobposting"),
    path('editjobposting/<profile_id>/', views.edit_jobposting, name="edit_jobposting"),
    path('deletejobposting/<profile_id>', views.delete_jobposting, name="delete_jobposting"),
]
