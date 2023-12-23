from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_admin = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email',  'password1', 'password2', 'is_admin']
        